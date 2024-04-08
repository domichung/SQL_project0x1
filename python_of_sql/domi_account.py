import MySQLdb

def check_createsuccessful(username ,pw ,repw ,email ,birthday ,grade ,Department ,photo):
    if not (username and pw and repw and email and birthday and grade != "請選擇你的年級" and Department != "請選擇你的系所"):
        return "有欄位未填寫"
    elif check_newaccount(username):
        return "已存在的用戶"
    elif check_newmail(email):
        return "已存在的電子郵件"
    elif pw != repw:
        return "兩次密碼不相同"
    else:
        return 1

def check_newaccount(name):

    # 建立讀取資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 欲查詢的 query 指令
    query = "SELECT id FROM user_box where username LIKE '{}%';".format(name)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def check_newmail(mail):

    # 建立讀取資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 欲查詢的 query 指令
    query = "SELECT id FROM user_box where mail LIKE '{}%';".format(mail)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def insert_newaccount(username, pw, email, birthday, grade, Department, photo):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_write",
                           passwd="write123",
                           db="user_login")
    
    cursor = conn.cursor()
    query = "INSERT INTO user_box (username, password, mail, birthday, grade, Department, MORECLASS, user_photo , user_class_count, newusercheck) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (username, pw, email, birthday, grade, Department, 0, photo, 0, 1))
    conn.commit()


def set_newloginstatus(id):
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="userlogin_reput",
                               passwd="reput123",
                               db="user_login")
        
        print("")

        cursor = conn.cursor()
        
        sql = """UPDATE user_box SET 
                 newusercheck = %s
                 WHERE id = %s"""
        
        cursor.execute(sql, (0,id))
         
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return True
        
    except Exception as e:
        print("Error:", e)
        return False


def find_id(name):
    import MySQLdb
    
    # 建立讀取資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 欲查詢的 query 指令
    query = "SELECT id FROM user_box where username LIKE '{}%';".format(name)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    # 取得結果
    result = cursor.fetchone()
    if result:
        return result[0]  # 返回 id
    else:
        return None  # 如果沒有找到，返回 None
