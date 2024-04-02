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

    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="read_bot",
                           passwd="readbot123",
                           db="course_selection")
    # 欲查詢的 query 指令
    query = "SELECT password FROM user_box where username LIKE '{}%';".format(name)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def check_newmail(mail):

    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="read_bot",
                           passwd="readbot123",
                           db="course_selection")
    # 欲查詢的 query 指令
    query = "SELECT password FROM user_box where mail LIKE '{}%';".format(mail)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def insert_newaccount(username, pw, email, birthday, grade, Department, photo):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="read_write_bot",
                           passwd="writebot123",
                           db="course_selection")
    
    cursor = conn.cursor()
    query = "INSERT INTO user_box (username, password, mail, birthday, grade, Department, MORECLASS, user_photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (username, pw, email, birthday, grade, Department, 0, photo))
    conn.commit()