import MySQLdb

def get_department_names():
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="read_bot",
                               passwd="readbot123",
                               db="course_selection")
        
        cursor = conn.cursor()
        
        cursor.execute("SELECT department_name FROM department")
        
        department_names = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()
        
        return department_names
        
    except Exception as e:
        print("Error:", e)
        return None