from flask import Flask
import pyodbc

app = Flask(__name__)

# Database connection function
def get_db_connection():
    try:
        conn_str = (
            'Driver={ODBC Driver 18 for SQL Server};'
            'Server=python-webapp-sqlserver-canada.database.windows.net;'
            'Database=appdb;'
            'Uid=Dbserver123;Pwd=Dbserver@123;'
            'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.route("/")
def home():
    return "<h1>Hello from Azure Cloud!</h1><p>My first cloud app is working!</p>"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/db-test")
def db_test():
    try:
        conn_str = (
            'Driver={ODBC Driver 18 for SQL Server};'
            'Server=python-webapp-sqlserver.database.windows.net;'
            'Database=free-sql-db-7468683;'
            'Uid=Dbserver123;Pwd=Shamnas@123!;'
            'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        )
        conn = pyodbc.connect(conn_str)
        conn.close()
        return {"status": "Database connected successfully!"}
    except Exception as e:
        return {"status": "Failed", "error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)