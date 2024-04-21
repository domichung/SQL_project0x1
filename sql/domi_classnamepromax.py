import MySQLdb

def unchoose_list(classname):


    conn = MySQLdb.connect(host="127.0.0.1",
                           user="class_info_read",
                           passwd="read123",
                           db="class_info")

    cursor = conn.cursor()
        
    query = "SELECT * FROM course WHERE course_id = %s"
    
    cursor.execute(query, (classname,))  # 在 execute 中传递元组作为参数，以避免 SQL 注入攻击

    class_names = cursor.fetchone()

    cursor.close()
    conn.close()

    return class_names


#print(unchoose_list("IECS0003"))

def promax_input(arr):
    new_array = [[None for _ in range(len(arr[0]))] for _ in range(len(arr))]
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            try:
                new_array[i][j] = unchoose_list(arr[i][j])[1]
            except:
                new_array[i][j] = arr[i][j]

    return new_array


#old_array = [[1, "IECS0003", 3], [4, None, "IECS0002"], [7, 8, None]]
#new_array = promax_input(old_array)
#print(new_array)

def promax_input_string(arr):
    
    result_string = ''

    for row in arr:
        for cell in row:
            result_string += str(cell) + '/'

    result_string = result_string[:-1]

    if (result_string == "尚/未/預/選"):
        result_string = "尚未預選"
    if (result_string == ""):
        result_string = "尚未預選"

    return result_string

#old_array = [[1, "IECS0003", 3], [4, None, "IECS0002"], [7, 8, None]]
#new_array = promax_input_string(old_array)
#print(new_array)

def flatten_2d_array(array_2d):
    flattened_array = []
    for row in array_2d:
        for element in row:
            flattened_array.append(element)
    return flattened_array

#array_2d = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#print(flatten_2d_array(array_2d))