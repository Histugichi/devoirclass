import _mysql_connector as mysql

def connect_db():
    return mysql.connect(
        user='root',
        host='localhost',
        password='',
        database='agence'
    )
