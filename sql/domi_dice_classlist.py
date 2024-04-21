import MySQLdb ,random ,domi_addclass ,domi_diceleave_classlist
import domi_addclass,domi_classinfo,domi_account,domi_loadcanichoose,domi_checkclasssys,domi_timmercut


def killuser_inselfstorge(userid,class_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="willchoose_root",
                           passwd="root123",
                           db="willchooseclass")
    
    cursor = conn.cursor()

    storgename = str(userid) + "_wait_class_list"
    
    create_table_query = """DELETE FROM `{}` WHERE `classid` = %s;""".format(storgename)

    cursor.execute(create_table_query,(class_id,))
    
    conn.commit()
    conn.close()


def check_class_willchoose(userid,_time_str):
    user_dbname = str(userid) + "_classlist"
    _time_str_cut = domi_timmercut.dm_time_cut(str(_time_str))
    #print("a")
    try:
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="userclass_read",
                               passwd="read123",
                               db = 'user_class')
        
        cursor = conn.cursor()

        for i in  range(len(_time_str)//2):
            
            today_value = _time_str_cut[i][0]
            #print(today_value)

            query = f"SELECT * FROM {user_dbname} WHERE TODAY = %s"
            cursor.execute(query, (today_value,))
        
            classinfo = cursor.fetchall()
        
            classinfo_array = [list(item) for item in classinfo]


            #print(classinfo_array[0][_time_str_cut[i][1]])

            if (classinfo_array[0][_time_str_cut[i][1]] != None):
                if (classinfo_array[0][_time_str_cut[i][1]] != "預選"):
                    return "faild"
        

        cursor.close()
        conn.close()

        return "success"
        
    except Exception as e:
        print("Error:", e)
        return None


#print(check_class_willchoose("10","6c6d7e"))


def dice_add_userclass(userid,courseid):
    user_dbname = str(userid) + '_classlist'
    #print(user_dbname)
    try:
        # 建立資料庫連線
        
        _classinfo = domi_classinfo.find_class_info(courseid)
        _userinfo_canchosemoredepartment = domi_account.find_canmoredepartment_byid(userid)

        if (domi_loadcanichoose.comclasschose(_classinfo[0][0],userid) == "faild"):
            return "你已選擇此課程"

        #改
        if (check_class_willchoose(userid,_classinfo[0][6]) == "faild"):
            return "你這節課已經有選課囉"
        
        #學分數上限
        if (domi_checkclasssys.check_classpint_inrange(userid , _classinfo[0][4]) == "faild"):
            #print(str(_classinfo[0][4]) + "<===學分數")
            return "你已抵達學分上限 整個深淵都為你撼動"
        
        #選課人數超過上限
        if (_classinfo[0][8]+1>_classinfo[0][7]):
            return "滿人囉 可以考慮前往預選"

        if (_userinfo_canchosemoredepartment == 0):
            #print(str(userid)+ " "+ str(_classinfo[0][2]))
            if (domi_account.comp_userdepartment_departmentid(int(userid),int(_classinfo[0][2])) != "success" ):
                return "你尚未獲得外系選修資格"

        _time_str_cut = domi_timmercut.dm_time_cut(_classinfo[0][6])

        #print(_classinfo[0][4])
        
        if (1):
            domi_addclass._insert_into_classlist(_classinfo[0][0],_time_str_cut,user_dbname)
            domi_addclass.adduserclasspoint(userid,_classinfo[0][4])
            domi_addclass.addstudentnuminclass(_classinfo[0][0])
            return 'success'
        
    except:
        return '你尚未選擇任何課程'

#print(dice_add_userclass("10","STAT0087"))

def check_class_full(class_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                               user="class_info_read",
                               passwd="read123",
                               db="class_info")
    
    cursor = conn.cursor()
        
    sql = """SELECT * FROM course WHERE course_id = %s;"""
        
    cursor.execute(sql, (class_id,))
         
    output = cursor.fetchall()
        
    cursor.close()
    conn.close()

    if (output == () ):
        print("警告 搜不到課程")
        return -999
    #print(output)

    return (output[0][7] == output[0][8])

#print(check_class_full("IECS0001"))

def create_new_storge(class_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="dice_root",
                           passwd="root123",
                           db="dice_of_class")
    
    cursor = conn.cursor()

    storgename = str(class_id) + "_wait_list"
    
    create_table_query = """
    CREATE TABLE `{}` (
        storge_id INT AUTO_INCREMENT PRIMARY KEY,
        userid VARCHAR(255)
    );
    """.format(storgename)

    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

#create_new_storge("aaa")

def adduser_instorge(userid,class_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="dice_root",
                           passwd="root123",
                           db="dice_of_class")
    
    cursor = conn.cursor()

    storgename = str(class_id) + "_wait_list"
    
    create_table_query = """INSERT INTO `{}` (userid) VALUES (%s);""".format(storgename)

    cursor.execute(create_table_query,(userid,))
    
    conn.commit()
    conn.close()

#adduser_instorge("www","aaa")

def readuser_instorge(class_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="dice_root",
                           passwd="root123",
                           db="dice_of_class")
    
    cursor = conn.cursor()

    storgename = str(class_id) + "_wait_list"
    
    create_table_query = """SELECT * FROM `{}`;""".format(storgename)

    cursor.execute(create_table_query)
    result = cursor.fetchall()
    
    conn.close()
    return result

#print(readuser_instorge("aaa"))

def choose_luck_user(class_id):
    
    arr = readuser_instorge(class_id)
    
    if not arr:
        return None  
    
    lucky_user = random.choice(arr)
    
    return lucky_user

#print(choose_luck_user("aaa"))

def killuser_instorge(userid,class_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="dice_root",
                           passwd="root123",
                           db="dice_of_class")
    
    cursor = conn.cursor()

    storgename = str(class_id) + "_wait_list"
    
    create_table_query = """DELETE FROM `{}` WHERE `storge_id` = %s;""".format(storgename)

    cursor.execute(create_table_query,(userid,))
    
    conn.commit()
    conn.close()

def someone_leaveclass(class_id):
    _classinfo = domi_classinfo.find_class_info(class_id)
    try:
        user = choose_luck_user(class_id)
        killuser_instorge(user[0],class_id)
        dice_add_userclass(user[1],class_id)
        domi_addclass.adduserclasspoint(user[1],-(_classinfo[0][4]))
        domi_diceleave_classlist.killuser_inselfstorge(user[1],class_id)
    except:
        print("FUCKKKKKKKKKKKKKKKKKKKK")

#someone_leaveclass("STAT0087")

def add_user_instorge(userid,class_id):
    if (check_class_full(class_id) != True ):
        print("預選失敗")
        return "error 尚未額滿 未開放預選"
    else:
        try:
            create_new_storge(class_id)
            adduser_instorge(userid,class_id)
        except:
            adduser_instorge(userid,class_id)

        print("完成預選")
        return "預選成功!"
    
#add_user_instorge("16","STAT0087")

def create_new_userstorge(user_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="willchoose_root",
                           passwd="root123",
                           db="willchooseclass")
    
    cursor = conn.cursor()

    storgename = str(user_id) + "_wait_class_list"
    
    create_table_query = """
    CREATE TABLE `{}` (
        storge_id INT AUTO_INCREMENT PRIMARY KEY,
        classid VARCHAR(255)
    );
    """.format(storgename)

    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

#create_new_userstorge("aaa")

def addclass_inuserstorge(userid,class_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="willchoose_root",
                           passwd="root123",
                           db="willchooseclass")
    
    cursor = conn.cursor()

    storgename = str(userid) + "_wait_class_list"
    
    create_table_query = """INSERT INTO `{}` (classid) VALUES (%s);""".format(storgename)

    cursor.execute(create_table_query,(class_id,))
    
    conn.commit()
    conn.close()

#addclass_inuserstorge("aaa","123")

def rebuild_userstorge(userid,classid):
    try:
        create_new_userstorge(userid)
        addclass_inuserstorge(userid,classid)
    except:
        addclass_inuserstorge(userid,classid)

def dic_main(userid,courseid):

    user_dbname = str(userid) + '_classlist'
    #print(user_dbname)
    if (1):
        # 建立資料庫連線
        
        _classinfo = domi_classinfo.find_class_info(courseid)
        _userinfo_canchosemoredepartment = domi_account.find_canmoredepartment_byid(userid)

        if (domi_loadcanichoose.comclasschose(_classinfo[0][0],userid) == "faild"):
            return "你已選擇此課程"


        if (domi_checkclasssys.check_class_empty(userid , _classinfo[0][6] ) == "faild"):
            return "你這節課已經有選課囉"
        
        #學分數上限
        if (domi_checkclasssys.check_classpint_inrange(userid , _classinfo[0][4]) == "faild"):
            #print(str(_classinfo[0][4]) + "<===學分數")
            return "你已抵達學分上限 整個深淵都為你撼動"
        
        #改!!!!!!!!!!!!!!!!!!
        if (check_class_full(courseid) == False):
            return "未滿人 可以考慮前往選課"

        if (_userinfo_canchosemoredepartment == 0):
            #print(str(userid)+ " "+ str(_classinfo[0][2]))
            if (domi_account.comp_userdepartment_departmentid(int(userid),int(_classinfo[0][2])) != "success" ):
                return "你尚未獲得外系預選修資格"

        _time_str_cut = domi_timmercut.dm_time_cut(_classinfo[0][6])
        
        if (1):
            domi_addclass._insert_into_classlist("預選",_time_str_cut,user_dbname)
            domi_addclass.adduserclasspoint(userid,_classinfo[0][4])
            add_user_instorge(userid,courseid)
            rebuild_userstorge(userid,courseid)
            return 'success'
    #except:
    #    return '你尚未選擇任何課程'

#print(dic_main(3,"STAT0087"))
    


def read_userwillchooselist(userid):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="willchoose_root",
                           passwd="root123",
                           db="willchooseclass")
    
    storgename = str(userid) + "_wait_class_list"

    cursor = conn.cursor()

    sql = """SELECT classid FROM """ +  storgename 


    cursor.execute(sql)
        
    department_names = cursor.fetchall()
        
    cursor.close()
    conn.close()
        
    return department_names

#print(read_userwillchooselist("2"))