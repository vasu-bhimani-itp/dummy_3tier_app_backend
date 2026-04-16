import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=<your-server>.database.windows.net;"
        "DATABASE=<your-db>;"
        "UID=<username>;"
        "PWD=<password>"
    )
    return conn