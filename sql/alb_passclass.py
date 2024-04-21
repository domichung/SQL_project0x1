import MySQLdb


# def create_user_pass_classlist(user_ID):

#     userdbname = str(user_ID) + "_passclass"

#     conn = MySQLdb.connect(host="127.0.0.1",
#                             user="userpass_root",
#                             passwd="root123",
#                             db="user_pass_classlist")
    
#     cursor = conn.cursor()

#     sql = """
#     CREATE TABLE `{}` (
#     `course_id` VARCHAR (500) PRIMARY KEY,
#     `course_status` VARCHAR (500))
#     """.format(userdbname)
    
#     cursor.execute(sql)
#     conn.commit()

#     cursor.close()
#     conn.close()

# create_user_pass_classlist('3')

# is subordinate or not
def is_pass_or_not(course_ID):

    try:

        conn = MySQLdb.connect(host="127.0.0.1",
                                user="class_info_read",
                                passwd="read123",
                                db="class_info")
        
        cursor = conn.cursor()
        
        sql = """SELECT subordinate FROM course WHERE course_id = %s"""
        # print(sql)

        cursor.execute(sql,(course_ID,))

        subordinate = cursor.fetchall()
        # print(subordinate)

        cursor.close()
        conn.close()

        # need to pass the before course
        # NEXT STEP:find the course you need to pass (find_after_pass)
        if subordinate and subordinate[0][0] == "yes":
            #print("yes")
            return True
        # can choose this course immediately
        else:
            #print("no")
            return False
    
    except:
        return 'failed'

#print(is_pass_or_not('IECS0666'))

# find what course should pass first
def find_after_pass(course_ID):

    try:
        conn = MySQLdb.connect(host="127.0.0.1",
                             user="afterpass_root",
                             passwd="root123",
                             db="after_course_pass")
        
        cursor = conn.cursor()
 
        sql = """SELECT course_id_pass FROM after_pass WHERE course_id = %s"""

        cursor.execute(sql,(course_ID,))

        class_pass = cursor.fetchall()
        # print(class_pass[0][0])
        
        cursor.close()
        conn.close()

        # course_id that you need to pass first
        return class_pass[0][0]
    except:
        return 'failed'
    
#print(find_after_pass('IECS0666'))



def check_if_pass_or_not(pass_course_ID,user_ID):

    try:
        userdblist = str(user_ID) + "_passclass"
        # print(userdblist)
        conn = MySQLdb.connect(host="127.0.0.1",
                             user="userpass_root",
                             passwd="root123",
                             db="user_pass_classlist")
        cursor = conn.cursor()

        sql = """SELECT course_status FROM {} WHERE course_id = %s""".format(userdblist)
        cursor.execute(sql, (pass_course_ID,))
        pass_status = cursor.fetchall()

        cursor.close()
        conn.close()

        # if pass return true 
        # CAN NOT CHOOSE "THIS" COURSE AGAIN!!!
        # can choose the after one (subordinate)
        if pass_status and pass_status[0][0] == "pass":
            #print("pass")
            return True
        # if not pass return false
        # CAN CHOOSE THIS COURSE 
        # can not choose after one
        else:
            #print("not pass")
            return False
    except:
        return False
    
#print(check_if_pass_or_not('IECS0002',"3"))



# # test code
#if (is_pass_or_not('IECS0666')):
    #a = find_after_pass('IECS0666')
    #check_if_pass_or_not(a,'3')
#else:
    #print("wwwww")
# # test code