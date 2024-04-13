import MySQLdb

def get_students_names():
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
        
        cursor = conn.cursor()
        
        cursor.execute("SELECT username FROM user_box")
        
        department_names = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()
        
        return department_names
        
    except Exception as e:
        print("Error:", e)
        return None