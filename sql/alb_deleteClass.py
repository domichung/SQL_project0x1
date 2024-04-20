# coding=utf-8
# -*- coding: UTF-8 -*-

import MySQLdb
import domi_timmercut ,domi_classinfo ,domi_newlogin ,domi_account ,domi_adminsys


def update_user_class(user_ID,delete_course_ID):
        
    user_dbname = str(user_ID) + "_classlist"

    conn = MySQLdb.connect(host="127.0.0.1",
                        user="userclass_update",
                        passwd="update123",
                        db="user_class")
        
    cursor = conn.cursor()


        
    info = domi_classinfo.find_class_info(delete_course_ID)
    time = domi_timmercut.dm_time_cut(info[0][6])
    for i in range(len(time)):
        sql = """UPDATE """ + user_dbname + """ SET """ + 'class'+ str(time[i][1]) + """ = NULL """ + """WHERE TODAY = """ + str(time[i][0])
        # print(sql)
        cursor.execute(sql)
        conn.commit()

    return True
    
# update_user_class('lulu',"IECS0002")

def is_default_or_not(course_ID,user_ID):
    
    search = domi_account.find_user_classlist_name(user_ID)
    # print(search)
    default_class = domi_newlogin.LD_dclasslist(search)
    # print(default_class)
    default_data = set(default_class)
    # print(default_data)
    if default_data is None:
        print("Failed to load default class data")
        # print("無法獲取課程數據!")
        return False
    
    if (course_ID,) in default_data:
        print("Course {} is a default course".format(course_ID))
        # print("{} 是必修課".format(course_ID))
        return True
    else:
        print("Course {} is not a default course".format(course_ID))
        # print("{} 不是必修課".format(course_ID))
        return False

# is_default_or_not("IECS0666","2")

def killstudentnuminclass(class_id):

    conn = MySQLdb.connect(host="127.0.0.1",
                               user="classinfo_change",
                               passwd="change123",
                               db="class_info")

    cursor = conn.cursor()
        
    sql = """UPDATE course SET 
             nowstudent = nowstudent - 1
             WHERE course_id = %s """
        
    cursor.execute(sql, (class_id,))
         
    conn.commit()
        
    cursor.close()
    conn.close()

def minus_classpoint(user_ID,point):

    conn = MySQLdb.connect(host="127.0.0.1",
                            user="userlogin_reput",
                            passwd="reput123",
                            db="user_login")

    cursor = conn.cursor()
        
    sql = """UPDATE user_box SET 
             user_class_count = user_class_count - %s
             WHERE id = %s"""
        
    cursor.execute(sql, (point,str(user_ID)))
         
    conn.commit()
        
    cursor.close()
    conn.close()
    

def delete_user_class(course_ID,user_ID):

    conn = MySQLdb.connect(host="127.0.0.1",
                               user="class_info_read",
                               passwd="read123",
                               db="class_info")
        
    cursor = conn.cursor()
        
    # 修改 SQL 查詢，只選擇指定名字的資料
    cursor.execute("SELECT class_point FROM course WHERE course_id = %s", (course_ID,))
        
    # 取得所有符合條件的資料
    classpoint = cursor.fetchall()
    classpoint_value = int(classpoint[0][0])
    
    cursor.close()
    conn.close()
    
    conn = MySQLdb.connect(host="127.0.0.1",
                               user="userlogin_read",
                               passwd="read123",
                               db="user_login")
        
    cursor = conn.cursor()
        
    # 修改 SQL 查詢，只選擇指定ID的資料
    cursor.execute("SELECT user_class_count FROM user_box WHERE id = %s", (user_ID,))
        
    # 取得所有符合條件的資料
    userpoint = cursor.fetchall()
    userpoint_value = int(userpoint[0][0])

    cursor.close()
    conn.close()

    if(userpoint_value - classpoint_value < 9):
        print("can't lower than 9 classpoint !!!")

    else:
        if(is_default_or_not(course_ID, user_ID)):
            print("Required course can not drop !!!")    
        else:
            update_user_class(user_ID, course_ID)
            minus_classpoint(user_ID, classpoint_value)
            killstudentnuminclass(course_ID)
        
        
# delete_user_class('IECS0003','3')
