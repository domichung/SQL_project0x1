import domi_listmyclass , MySQLdb


def find_studentalreadychoose(studentid):
    two_dim_array = domi_listmyclass.get_students_classlist(studentid)

    # 使用set來去除重複值
    unique_values = set()
    for row in two_dim_array:
        for item in row:
            unique_values.add(item)

    # 將set轉換為一維陣列
    one_dim_array = list(unique_values)

    values_to_remove = {1, 2, 3, 4, 5, 6, 7, None}
    one_dim_array = [item for item in one_dim_array if item not in values_to_remove]

    return(one_dim_array)

def unchoose_list(studentid):

    willsearch = find_studentalreadychoose(studentid)

    conn = MySQLdb.connect(host="127.0.0.1",
                           user="class_info_read",
                           passwd="read123",
                           db="class_info")

    cursor = conn.cursor()
        
    query = "SELECT * FROM course WHERE course_id IN %s"
    
    cursor.execute(query, (willsearch,))  # 在 execute 中传递元组作为参数，以避免 SQL 注入攻击

    class_names = cursor.fetchall()

    cursor.close()
    conn.close()

    return class_names

#print(unchoose_list(2))