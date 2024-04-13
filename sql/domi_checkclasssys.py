import MySQLdb 
import domi_timmercut

def check_class_empty(userid,_time_str):
    user_dbname = str(userid) + "_classlist"
    _time_str_cut = domi_timmercut.dm_time_cut(_time_str)

    #print(len(_time_str))
    #print(_time_str_cut[0])

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

            if (classinfo_array[0][_time_str_cut[i][1]] != None ):
                return "faild"
        

        cursor.close()
        conn.close()

        return "success"
        
    except Exception as e:
        print("Error:", e)
        return None
    
#print(check_class_empty("lulu","1b3d5a7861"))