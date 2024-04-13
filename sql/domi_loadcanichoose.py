import MySQLdb
import domi_listmyclass

def givemeallcalss():
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="class_info_read",
                           passwd="read123",
                           db="class_info")

    cursor = conn.cursor()
        
    cursor.execute("SELECT * FROM course")
        
    class_names = cursor.fetchall()
        
    cursor.close()
    conn.close()
        
    return class_names

def givemecalsscleardeparment(departmentid):
    a = list(givemeallcalss())
    i = 0
    while i < len(a):
        if a[i][2] != departmentid:
            del a[i]
        else:
            i += 1
    print(a)

def givemeclasssclearalreadychoose(userid):
    willchange = domi_listmyclass.get_students_classlist(userid)
    
    change = []
    for row in willchange:
        for j in range(1, len(row)):
            change.append(row[j])
    
    change = list(set(change))
    change.remove(None)

    print(change)
    return change  # 返回去重后的列表





givemeclasssclearalreadychoose(3)

#givemecalsscleardeparment(10)