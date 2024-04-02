import MySQLdb

def check_login(login_id ,password):

    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="read_bot",
                           passwd="readbot123",
                           db="course_selection")
    # 欲查詢的 query 指令
    query = "SELECT password FROM user_box where username LIKE '{}%';".format(login_id)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)

    results = "none"

    # 取得並列出所有查詢結果
    for (password, ) in cursor.fetchall():
        results = "{}".format(password)

    if (results == "none"):
        print("警告 : 帳號不存在\n輸入帳號:" + login_id + "\n輸入密碼:" + password)
    elif (results != password):
        print("警告 : 密碼錯誤\n帳號:" + login_id + "\n輸入密碼:" + password + "\n實際密碼:" + results + "\n")
    else:
        print("用戶 : " + login_id + "登入成功\n")

    if results != password:
        return 0
    else:
        return 1