import os
import pymysql
from urllib.parse import urlparse

def get_connection():
    url = urlparse(os.getenv("MYSQL_URL"))

    return pymysql.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path.lstrip('/'),
        port=url.port or 3306,
        cursorclass=pymysql.cursors.Cursor
    )