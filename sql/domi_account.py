import MySQLdb , domi_listmyclass 

def check_createsuccessful(username ,pw ,repw ,email ,birthday ,grade ,Department ,photo ,myABCD_class):
    if not (username and pw and repw and email and birthday and grade != "請選擇你的年級" and Department != "請選擇你的系所" and myABCD_class != "請選擇你的班級"):
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


def insert_newaccount(username, pw, email, birthday, grade, Department, photo ,myABCD_class):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_write",
                           passwd="write123",
                           db="user_login")
    
    cursor = conn.cursor()
    query = "INSERT INTO user_box (username, password, mail, birthday, grade, Department, MORECLASS, user_photo , user_class_count, newusercheck, ABCDclass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (username, pw, email, birthday, grade, Department, 0, photo, 0, 1, myABCD_class))
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

def find_grade_id(grade):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 執行查詢

    cursor = conn.cursor()

    sql = "SELECT * FROM grade_list WHERE grade = '" + grade + "'"

    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    
    if (result):
        return result[0][0]
    else:
        return 'faild'

    
#print(find_grade_id("大二"))

def find_department_id(department):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 執行查詢

    cursor = conn.cursor()

    sql = "SELECT * FROM department WHERE department_name = '" + department + "'"

    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    
    if (result):
        return result[0][0]
    else:
        return 'faild'


def find_classABCDname_id(classABCDname):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 執行查詢

    cursor = conn.cursor()

    sql = "SELECT class_id FROM class_list WHERE classname = '" + classABCDname + "'"

    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()

    if (result):
        return result[0][0]
    else:
        return 'faild'


#print(find_classABCDname_id('丁班'))
#print(find_department_id('電子工程學系'))


def find_user_classlist_name(id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 欲查詢的 query 指令
    cursor = conn.cursor()

    sql = """SELECT * FROM user_box WHERE id = %s"""
    # 執行查詢
    cursor.execute(sql,(str(id)))
    conn.commit()
    people_data = cursor.fetchall()
    #print(people_data)
    #print(domi_account.find_grade_id(people_data[0][5]))
    #print(domi_account.find_classABCDname_id(people_data[0][11]))
    #print(domi_account.find_department_id(people_data[0][6]))
    #defaultclass_1_1_2
    search_class = ('defaultclass_' + 
                    str(find_department_id(people_data[0][6])) + "_" +
                    str(find_grade_id(people_data[0][5]))      + "_" +
                    str(find_classABCDname_id(people_data[0][11])))
    
    return search_class

#print(find_user_classlist_name(2))

def find_name_id(id):
    
    # 建立讀取資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 欲查詢的 query 指令
    query = "SELECT username FROM user_box where id LIKE '{}%';".format(id)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    # 取得結果
    result = cursor.fetchone()
    if result:
        return result[0]  # 返回 
    else:
        return None  # 如果沒有找到，返回 None
    
#print(find_name_id(2))

def find_moreclass_byid(id):
    
    # 建立讀取資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 欲查詢的 query 指令
    query = "SELECT moreclass FROM user_box where id LIKE '{}%';".format(id)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    # 取得結果
    result = cursor.fetchone()
    if result:
        return result[0]  # 返回
    else:
        return None  # 如果沒有找到，返回 None
    
def find_userclasscount_byid(id):
    
    # 建立讀取資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userlogin_read",
                           passwd="read123",
                           db="user_login")
    # 欲查詢的 query 指令
    query = "SELECT user_class_count FROM user_box where id LIKE '{}%';".format(id)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    # 取得結果
    result = cursor.fetchone()
    if result:
        return result[0]  # 返回
    else:
        return None  # 如果沒有找到，返回 None
    
#print(find_userclasscount_byid(2))