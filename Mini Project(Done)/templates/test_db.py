import pymysql

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YES',  # Replace with your actual MySQL password
    'db': 'risk_assessment',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

try:
    connection = pymysql.connect(**db_config)
    print("Successfully connected to the database!")
    connection.close()
except pymysql.MySQLError as e:
    print(f"Error connecting to the database: {e}")