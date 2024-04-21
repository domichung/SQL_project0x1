import MySQLdb ,random ,domi_addclass
import domi_addclass,domi_classinfo,domi_account,domi_loadcanichoose,domi_checkclasssys,domi_timmercut
import domi_dice_classlist


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


def leavewillclass(userid,courseid):
    try:
        user_dbname = str(userid) + '_classlist'
        #print(user_dbname)
        if (1):
        
            _classinfo = domi_classinfo.find_class_info(courseid)
            #_userinfo_canchosemoredepartment = domi_account.find_canmoredepartment_byid(userid)
            _time_str_cut = domi_timmercut.dm_time_cut(_classinfo[0][6])
        
        
            domi_addclass._insert_into_classlist( None , _time_str_cut , user_dbname)
            domi_addclass.adduserclasspoint(userid,-(_classinfo[0][4]))
            domi_dice_classlist.killuser_instorge(userid,courseid)
            killuser_inselfstorge(userid,courseid)
            return 'success'
    except:
        return "你尚未選擇要退預選課程"
#print(leavewillclass("2","STAT0087"))

#print(leavewillclass("9","IECS0003"))

def change_name_to_id(name):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="class_info_read",
                           passwd="read123",
                           db="class_info")

    cursor = conn.cursor()
        
    query = "SELECT course_id FROM course WHERE course_name = %s"
    
    cursor.execute(query, (name,))  # 在 execute 中传递元组作为参数，以避免 SQL 注入攻击

    class_names = cursor.fetchone()

    cursor.close()
    conn.close()

    return class_names

#print(change_name_to_id("統計學"))