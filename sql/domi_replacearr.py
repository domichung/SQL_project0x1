def replace(a):
    new_array = [[None for _ in range(len(a[0]))] for _ in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] is None:
                new_array[i][j] = " "
            else:
                new_array[i][j] = a[i][j]
    
    return new_array

#old_array = [[1, None, 3], [4, None, 6], [7, 8, None]]
#new_array = replace(old_array)
#print(new_array)