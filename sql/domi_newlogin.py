import MySQLdb
import domi_account , domi_addclass

def insert_newaccount(id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userclass_create",
                           passwd="create123",
                           db="user_class")
    
    cursor = conn.cursor()

    id = str(id) + "_classlist"
    
    create_table_query = """
    CREATE TABLE `{}` (
        TODAY   INT(50) PRIMARY KEY,
        class1 VARCHAR(255),
        class2 VARCHAR(255),
        class3 VARCHAR(255),
        class4 VARCHAR(255),
        class5 VARCHAR(255),
        class6 VARCHAR(255),
        class7 VARCHAR(255),
        class8 VARCHAR(255),
        class9 VARCHAR(255),
        class10 VARCHAR(255),
        class11 VARCHAR(255),
        class12 VARCHAR(255),
        class13 VARCHAR(255),
        class14 VARCHAR(255),
        class15 VARCHAR(255)
    );
    """.format(id)
    cursor.execute(create_table_query)

    for i in range(1, 8):
        insert_query = """
        INSERT INTO `{}` (TODAY) VALUES({});
        """.format(id, i)
        cursor.execute(insert_query)

    conn.commit()
    conn.close()

def newclasslist_main(id):
    try:
        insert_newaccount(id)
        domi_account.set_newloginstatus(id)
        print('帳號創建成功')
        print('載入課表'+LDDclass(id))
    except:
        domi_account.set_newloginstatus(id)
        print('已存在帳號 註冊失敗')
        

#insert_newaccount('lulu')


def LD_dclasslist(class_name):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="read_defaultclass",
                           passwd="read123",
                           db="default_curriculum")
    
    cursor = conn.cursor()

    try:
        sql = """SELECT class_id FROM """ + class_name 
        # 執行查詢
        cursor.execute(sql)
        conn.commit()
        people_data = cursor.fetchall()
        #print(people_data)
        return people_data
        #print(LD_dclasslist('defaultclass_1_1_2'))
    except:
        return 'faild'

def LDDclass(id):
    # 建立讀取資料庫連線
    
    search_class = domi_account.find_user_classlist_name(id)

    print(search_class+"\n")
    #print(LD_dclasslist(search_class))
    inlist = LD_dclasslist(search_class)
    #print(len(LD_dclasslist(search_class)))
    
    if (inlist == 'faild'):
        print('load class faild')
        return 'faild'
    
    for i in range(len(LD_dclasslist(search_class))):
        print(inlist[i][0])
        domi_addclass.add_userclass(id,inlist[i][0])
    
    return 'success'

#LDDclass(3)
