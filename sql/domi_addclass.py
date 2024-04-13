import MySQLdb 
import domi_classinfo , domi_checkclasssys ,domi_timmercut

def add_userclass(userid,courseid):
    user_dbname = str(userid) + '_classlist'
    #print(user_dbname)
    if (1):
        # 建立資料庫連線
        
        _classinfo = domi_classinfo.find_class_info(courseid)

        _checkself_class_empty = domi_checkclasssys.check_class_empty(userid , _classinfo[0][6] )

        _classinfo = domi_classinfo.find_class_info(courseid)
        _time_str_cut = domi_timmercut.dm_time_cut(_classinfo[0][6])
        print(_checkself_class_empty)
        print(_classinfo[0][4])
        
        if (_checkself_class_empty == 'success'):
            _insert_into_classlist(_classinfo[0][0],_time_str_cut,user_dbname)
            adduserclasspoint(userid,_classinfo[0][4])
            return 'success'
        else:
            return 'faild'

        
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