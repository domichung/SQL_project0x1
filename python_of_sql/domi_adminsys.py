import MySQLdb

def check_is_admin(name):

    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="adminlogin_read",
                           passwd="read123",
                           db="admin_login")
    # 欲查詢的 query 指令
    query = "SELECT admin_id FROM adminlist where name LIKE '{}%';".format(name)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()