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


def comclasschose(checkclass,userid):
    ld = givemeclasssclearalreadychoose(int(userid))
    flag = 1
    #print(ld)
    for i in range (len(ld)):
        #print(checkclass)
        #print(ld[i])
        if (checkclass == ld[i]):
            flag = 0
        
    if (flag==0):
        return "faild"
    else:
        return "success"

#print(comclasschose("IECS0004",2))

#givemeclasssclearalreadychoose(3)

#givemecalsscleardeparment(10)
def simplify_courses(data):
    # 定義中文數字映射
    chinese_numbers = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '日'}
    hex_to_dec = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    
    sorted_data = sorted(data, key=lambda x: len(x[0]))

    return [f'{course[0]} {course[1]} 學分: {course[4]} 上課時間: {"".join([f"({chinese_numbers[course[6][i]]}{hex_to_dec.get(course[6][i+1], course[6][i+1])})" for i in range(0, len(course[6]), 2)])}' for course in sorted_data]

# // 課程說明: {course[5]} //
#print('\n'.join(simplify_courses(givemeallcalss())))
#print(simplify_courses(givemeallcalss())[0].split()[0])