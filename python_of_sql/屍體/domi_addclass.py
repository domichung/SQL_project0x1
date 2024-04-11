import MySQLdb 
import domi_classinfo , domi_checkclasssys ,domi_timmercut

def add_userclass(userid,courseid):
    user_dbname = userid + '_classlist'
    print(user_dbname)
    try:
        # 建立資料庫連線
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="userclass_update",
                               passwd="update123",
                               db = "user_class")
        
        
        _classinfo = domi_classinfo.find_class_info(courseid)

        _checkself_class_empty = domi_checkclasssys.check_class_empty(userid , _classinfo[0][6] )

        if (_checkself_class_empty == 'faild'):
            reason = "與以選課表時間衝堂"
        else:
            _time_str_cut = domi_timmercut.dm_time_cut(_classinfo[0][6])

            for i in  range(len(_classinfo[0][6])//2):
                
                cursor = conn.cursor()

                indbclassname = 'class' + str(_time_str_cut[i][1])

                sql = """UPDATE `%s` SET `%s` = '%s' WHERE TODAY = %s"""
                cursor.execute(sql, (str(user_dbname), str(indbclassname) , str(_classinfo[0][0]) ,int(_time_str_cut[i][0])) )

                #幹你娘

                conn.commit()
                reason = "success"
        
                cursor.close()
                conn.close()
            
        return reason
        
    except Exception as e:
        print("Error:", e)
        return False


print(add_userclass('lulu',"IECS0002"))

