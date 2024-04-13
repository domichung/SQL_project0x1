import MySQLdb

def get_department_names():
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
        
        cursor = conn.cursor()
        
        cursor.execute("SELECT department_name FROM department")
        
        department_names = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()
        
        return department_names
        
    except Exception as e:
        print("Error:", e)
        return None

def get_class_names():
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
        
        cursor = conn.cursor()
        
        cursor.execute("SELECT classname FROM class_list")
        
        class_names = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()
        
        return class_names
        
    except Exception as e:
        print("Error:", e)
        return None

def get_grade_names():
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
        
        cursor = conn.cursor()
        
        cursor.execute("SELECT grade FROM grade_list")
        
        grade_names = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()
        
        return grade_names
        
    except Exception as e:
        print("Error:", e)
        return None