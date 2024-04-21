import MySQLdb
import domi_listmyclass,domi_classnamepromax

def check_same_name(course_ID, user_ID):

    conn = MySQLdb.connect(host="127.0.0.1",
                               user="class_info_read",
                               passwd="read123",
                               db="class_info")
        
    cursor = conn.cursor()
    # find the chinese class name of the course
    cursor.execute("SELECT course_name FROM course WHERE course_id = %s", (course_ID,))
        
    course_name = cursor.fetchall()
    course_name_pro = domi_classnamepromax.promax_input(course_name)
    
    # print(course_name_pro)
    cursor.close()
    conn.close()
   
    user_class = domi_listmyclass.get_students_classlist(user_ID)
    # change user class name to chinese
    user_class_pro = domi_classnamepromax.promax_input(user_class)
    # print(user_class_pro)

    for course in user_class_pro:
        if course_name_pro[0][0] in course:
            print("already had a same name course !!!")
            return False
    
    print("++++")
    return True
    
# check_same_name('IECS0333' , '3')
