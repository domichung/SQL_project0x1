import MySQLdb 
import domi_classinfo , domi_checkclasssys ,domi_timmercut , domi_loadcanichoose 
import domi_account


def add_userclass(userid,courseid):
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
        
        #選課人數超過上限
        if (_classinfo[0][8]+1>_classinfo[0][7]):
            return "滿人囉 可以考慮前往預選"

        if (_userinfo_canchosemoredepartment == 0):
            print(str(userid)+ " "+ str(_classinfo[0][2]))
            if (domi_account.comp_userdepartment_departmentid(int(userid),int(_classinfo[0][2])) != "success" ):
                return "你尚未獲得外系選修資格"

        _time_str_cut = domi_timmercut.dm_time_cut(_classinfo[0][6])

        #print(_classinfo[0][4])
        
        if (1):
            _insert_into_classlist(_classinfo[0][0],_time_str_cut,user_dbname)
            adduserclasspoint(userid,_classinfo[0][4])
            addstudentnuminclass(_classinfo[0][0])
            return 'success'
        
    else:
        return 'a'


def _insert_into_classlist(classname ,time ,userdbname):

    conn = MySQLdb.connect(host="127.0.0.1",
                               user="userclass_update",
                               passwd="update123",
                               db = "user_class")

    cursor = conn.cursor()

    for i in range(len(time)):
        #print(time[i][1])
        #print(classname)
        #print(userdbname)
        #print()


        #fuck of request of sql cant input %s

        sql = """UPDATE """ + userdbname + """ SET """ + 'class'+ str(time[i][1]) + """ = %s WHERE TODAY = %s"""
        #sql = """UPDATE """ + %s` + """SET `%s` = "%s" WHERE `TODAY` = %s"""
        #sql = """SELECT * FROM """ + userdbname + """ WHERE TODAY = %s"""
        #print(sql, (userdbname, 'class' + str(time[i][0]) , classname , time[i][1]))

        #cursor.execute(sql, ('lulu_classlist', 'class4', 'IECS0002', 7))

        #cursor.execute(sql, (userdbname, 'class' + str(time[i][0]) , classname , time[i][1]))
        cursor.execute(sql,(classname,str(time[i][0])))
        conn.commit()

        #people_data = cursor.fetchall()
        #print(people_data)

    cursor.close()
    conn.close()

#add_userclass('lulu',"IECS0002")

def adduserclasspoint(id,num):
    conn = MySQLdb.connect(host="127.0.0.1",
                               user="userlogin_reput",
                               passwd="reput123",
                               db="user_login")
        
    #print("changeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

    cursor = conn.cursor()
        
    sql = """UPDATE user_box SET 
             user_class_count = %s + user_class_count
             WHERE id = %s"""
        
    cursor.execute(sql, (num,id))
         
    conn.commit()
        
    cursor.close()
    conn.close()
        
#adduserclasspoint(3,10)

def addstudentnuminclass(class_id):
    conn = MySQLdb.connect(host="127.0.0.1",
                               user="classinfo_change",
                               passwd="change123",
                               db="class_info")

    cursor = conn.cursor()
        
    sql = """UPDATE course SET 
             nowstudent = nowstudent + 1
             WHERE course_id = %s """
        
    cursor.execute(sql, (class_id,))
         
    conn.commit()
        
    cursor.close()
    conn.close()


#addstudentnuminclass('IECS0666')

#print(add_userclass(3,"IECS0003"))