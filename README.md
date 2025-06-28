
# 🛡️ Cybersecurity Risk Assessment Web App

This is a mini project for a **Cybersecurity Risk Assessment System**, built using **Flask (Python)**. The application allows users to perform a simplified risk assessment, interact with a backend database, and view the results through a user-friendly web interface.

## 💡 Features

- 🌐 Web-based interface using HTML templates
- 🔐 Risk analysis and classification based on input
- 📂 Integration with external platforms (e.g., MISP)
- 🗃️ MySQL database support (via `schema.sql`)
- 📊 Result display with dynamic rendering

## 🛠️ Technologies Used

- Python 3.x with Flask
- HTML/CSS (Jinja2 templates)
- MySQL / SQL for database
- MISP integration (for threat intel)

## 📁 Folder Structure (Simplified)

```
.
├── app.py                    # Main Flask app
├── database/
│   └── schema.sql           # Database schema
├── templates/               # HTML pages (Jinja2 templates)
│   ├── index.html
│   ├── risks.html
│   └── scan_result.html
```

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt  # (Create this file if not yet available)
   ```

4. Set up the database using `schema.sql`.

5. Run the app:
   ```bash
   python app.py
   ```

## 📌 Note

This project was developed as part of a university cybersecurity course and serves as an academic demonstration of risk assessment integration using Flask and basic database connectivity.
