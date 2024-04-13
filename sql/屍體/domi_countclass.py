import domi_listmyclass

def count(a):
    w = 0

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] is None:
                w=w
            else:
                w+=1
    
    return w-7

#old_array = [[1, None, 3], [4, None, 6], [7, 8, None]]
#new_array = count(old_array)
#print(new_array)