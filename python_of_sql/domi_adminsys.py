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

def find_people_data(name):
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="userlogin_read",
                               passwd="read123",
                               db="user_login")
        
        cursor = conn.cursor()
        
        # 修改 SQL 查詢，只選擇指定名字的資料
        cursor.execute("SELECT * FROM user_box WHERE username = %s", (name,))
        
        # 取得所有符合條件的資料
        people_data = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        people_data_array = [list(item) for item in people_data]
        
        return people_data_array
        
    except Exception as e:
        print("Error:", e)
        return None

def change_user_info(settinguserid, username, pw, email, birthday, grade, photo, Department, moreclass, newusercheck ,abcdclass):
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="userlogin_reput",
                               passwd="reput123",
                               db="user_login")
        
        #print("changeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

        cursor = conn.cursor()
        
        sql = """UPDATE user_box SET 
                 username = %s,
                 password = %s,
                 mail = %s,
                 birthday = %s,
                 grade = %s,
                 user_photo = %s,
                 Department = %s,
                 MORECLASS = %s,
                 newusercheck = %s,
                 ABCDclass = %s
                 WHERE id = %s"""
        
        cursor.execute(sql, (username, pw, email, birthday, grade, photo, Department, moreclass, newusercheck, abcdclass, settinguserid))
         
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return True
        
    except Exception as e:
        print("Error:", e)
        return False
