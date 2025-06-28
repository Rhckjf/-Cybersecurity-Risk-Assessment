from flask import Flask, render_template, request, redirect, url_for
import pymysql.cursors
import requests
import base64

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Ganti dengan password MySQL kamu
    'db': 'risk_assessment',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# VirusTotal Configuration
VIRUSTOTAL_API_KEY = 'efacfdd9ddf321fad868598c38cae5755dcd81e14312de009dc01d72ae7f788c'
VIRUSTOTAL_URL = 'https://www.virustotal.com/api/v3'

def calculate_risk(likelihood, impact):
    if likelihood == 'Low' and impact == 'Low':
        return 'Low'
    elif likelihood == 'High' and impact == 'High':
        return 'High'
    else:
        return 'Medium'

def scan_with_virustotal(url):
    headers = {'x-apikey': VIRUSTOTAL_API_KEY}
    submit_url = f'{VIRUSTOTAL_URL}/urls'
    payload = {'url': url}
    response = requests.post(submit_url, headers=headers, data=payload)
    
    if response.status_code == 200:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        response = requests.get(f'{VIRUSTOTAL_URL}/urls/{url_id}', headers=headers)
    
    return response.json() if response.status_code == 200 else None

@app.route('/')
def index():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM assets")
        assets = cursor.fetchall()
    connection.close()
    return render_template('index.html', assets=assets)

@app.route('/add_asset', methods=['POST'])
def add_asset():
    name = request.form['asset_name']
    description = request.form['asset_description']
    criticality = request.form['criticality']
    
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO assets (name, description, criticality) VALUES (%s, %s, %s)", (name, description, criticality))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))

@app.route('/edit_asset/<int:asset_id>', methods=['POST'])
def edit_asset(asset_id):
    name = request.form['asset_name']
    description = request.form['asset_description']
    criticality = request.form['criticality']
    
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE assets SET name=%s, description=%s, criticality=%s WHERE id=%s", (name, description, criticality, asset_id))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))

@app.route('/delete_asset/<int:asset_id>')
def delete_asset(asset_id):
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM assets WHERE id=%s", (asset_id,))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))

@app.route('/risks')
def show_risks():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("SELECT t.id, a.name AS asset, t.name AS threat, t.likelihood, t.impact FROM threats t JOIN assets a ON t.asset_id = a.id")
        risks = cursor.fetchall()
        for risk in risks:
            risk['risk_level'] = calculate_risk(risk['likelihood'], risk['impact'])
    connection.close()
    return render_template('risks.html', risks=risks)

@app.route('/delete_risk/<int:risk_id>')
def delete_risk(risk_id):
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM threats WHERE id=%s", (risk_id,))
    connection.commit()
    connection.close()
    return redirect(url_for('show_risks'))

@app.route('/process_link', methods=['POST'])
def process_link():
    link = request.form['link']
    vt_result = scan_with_virustotal(link)
    result_message = vt_result.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}) if vt_result else None
    return render_template('scan_result.html', link=link, result=result_message)

if __name__ == '__main__':
    app.run(debug=True)
