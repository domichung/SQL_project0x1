import MySQLdb
import domi_account

def insert_newaccount(id):
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="userclass_create",
                           passwd="create123",
                           db="user_class")
    
    cursor = conn.cursor()

    id = str(id) + "_classlist"
    
    create_table_query = """
    CREATE TABLE `{}` (
        TODAY   INT(50),
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
    insert_newaccount(id)
    domi_account.set_newloginstatus(id)

    #insert_newaccount('lulu')