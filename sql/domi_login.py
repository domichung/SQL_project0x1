import MySQLdb
import domi_adminsys

def check_login(login_id ,login_password):

    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 欲查詢的 query 指令
    query = "SELECT password FROM user_box where username LIKE '{}%';".format(login_id)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    # 取得搜尋結果
    results = cursor.fetchone()[0]


    check_status = "SELECT newusercheck FROM user_box where username LIKE '{}%';".format(login_id)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(check_status)
    # 取得搜尋結果
    check_firstlogin = cursor.fetchone()[0]

    if (results == "none"):
        print("警告 : 帳號不存在\n輸入帳號:" + login_id + "\n輸入密碼:" + login_password)
    elif (results != login_password):
        print("警告 : 密碼錯誤\n帳號:" + login_id + "\n輸入密碼:" + login_password + "\n實際密碼:" + str(results) + "\n")
    else:
        print("第一次登入狀態 : "+ str(check_firstlogin) +"\n")
        print("用戶 : " + login_id + " 登入成功\n")

    if results != login_password:
        return 0
    elif (domi_adminsys.check_is_admin(login_id)):
        return 1
    else:
        return 2 + int(check_firstlogin)
    