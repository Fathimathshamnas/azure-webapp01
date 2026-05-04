from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Azure Cloud!</h1><p>My first cloud app is working!</p>"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
import pyodbc
conn_str=(
    'Driver={ODBC Driver 18 for SQL Server};'
    'Server=python-webapp-sqlserver.database.windows.net;'
    'Database=appdb;'
    'Uid=Dbserver123;Pwd=Dbserver@123;'
)
conn_str=pyodbc.connect(conn_str)



