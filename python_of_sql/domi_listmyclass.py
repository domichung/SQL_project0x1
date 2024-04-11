import MySQLdb

def get_students_classlist(id):
    try:
        # 建立資料庫連線
        _listwho = str(id) + '_classlist'

        conn = MySQLdb.connect(host="127.0.0.1",
                           user="userclass_read",
                           passwd="read123",
                           db="user_class")
        
        cursor = conn.cursor()
        
        sql = """SELECT * FROM """ + _listwho


        cursor.execute(sql)
        
        department_names = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return department_names
        
    except Exception as e:
        print("Error:", e)
        return None
    
#print(get_students_classlist(3))