import MySQLdb

def find_class_info(classname):
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="class_info_read",
                               passwd="read123",
                               db="class_info")
        
        cursor = conn.cursor()
        
        # 修改 SQL 查詢，只選擇指定名字的資料
        cursor.execute("SELECT * FROM course WHERE course_id = %s", (classname,))
        
        # 取得所有符合條件的資料
        classinfo = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        classinfo_array = [list(item) for item in classinfo]
        
        return classinfo_array
        
    except Exception as e:
        print("Error:", e)
        return None
    

#print(find_class_info('IECS0003')[0][6])
