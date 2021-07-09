import mysql.connector

mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'otheruser',
            password = 'swordfish',
            database = 'records'
        )
mycursor = mydb.cursor()  
    

def insert_data():
    sql = "INSERT INTO register(id_number, name) VALUES (%s, %s)"
    id_number = input("Enter ID number: ")
    name = input("Enter name: ")        
    values = (f"{id_number}", f"{name}")
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "Records Inserted!")

def insert_multiple_data():
    count = 0
    while True:
        
        sql = "INSERT INTO register(id_number, name) VALUES (%s, %s)"
        id_number = input("Enter ID number: ")
        if id_number == 'done':
            break
        else:
            name = input("Enter name: ")        
            values = (f"{id_number}", f"{name}")
            mycursor.execute(sql, values)
            mydb.commit()
            count += 1
    print(count, "record inserted") 
        

def view_all():
    mycursor.execute("SELECT * FROM register")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def search_name():
    user_search = input("Enter name you want to search: ")
    mycursor.execute(f"SELECT * FROM register WHERE name= {user_search}")
    myresult = mycursor.fetchone()
    print(myresult)

def search_id():
    user_search = input("Enter ID number you want to search: ")
    mycursor.execute(f"SELECT * FROM register WHERE id_number = {user_search}")
    myresult = mycursor.fetchone()
    print(myresult)  

def search_phrase_name():
    user_search = input("Enter phrase or letter to search: ")
    mycursor.execute(f"SELECT * FROM register WHERE name LIKE  '%{user_search}%'")
    myresult =mycursor.fetchone()
    print(myresult)

def search_phrase_id():
    user_search = input("Enter phrase or letter to search: ")
    mycursor.execute(f"SELECT * FROM register WHERE id_number LIKE  '%{user_search}%'")
    myresult =mycursor.fetchone()
    print(myresult)

def sort_alpha_names():
    mycursor.execute("SELECT * FROM register ORDER BY name")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def sort_id():
    mycursor.execute("SELECT * FROM register ORDER BY id_number")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def sort_name_decending():
    mycursor.execute("SELECT * FROM register ORDER BY name DESC")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def sort_id_decending():
    mycursor.execute("SELECT * FROM register ORDER BY id_number DESC")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def delete_record_by_name():
    name = input("Enter name to delete: ")         
    mycursor.execute(f"DELETE FROM register WHERE name = '{name}'")
    mydb.commit()
    print(mycursor.rowcount, "Records Deleted!")

def delete_record_by_id():
    id = input("Enter ID number to delete: ")         
    mycursor.execute(f"DELETE FROM register WHERE id_number = '{id}'")
    mydb.commit()
    print(mycursor.rowcount, "Records Deleted!")

def update_id():
    id = input("Enter ID number to update: ")
    new_id = input("Enter new ID number: ")         
    mycursor.execute(f"UPDATE register SET id_number = '{new_id}' WHERE id_number = '{id}'")
    mydb.commit()
    print(mycursor.rowcount, "Records updated!")

def update_name():
    name= input("Enter name to update: ")
    new_name = input("Enter new name: ")         
    mycursor.execute(f"UPDATE register SET name = '{new_name}' WHERE name = '{name}'")
    mydb.commit()
    print(mycursor.rowcount, "Records updated!")

def view_first5_rows():
    mycursor.execute("SELECT * FROM register LIMIT 5")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def view_user_5rows():
    num = int(input("Enter the position where to start: "))
    num = num - 1
    mycursor.execute(f"SELECT * FROM register LIMIT 5 OFFSET {num}")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def main():

    print("Welcome to PythonDatabase!")
    try:
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'otheruser',
            password = 'swordfish',
            database = 'records'
        )
        mycursor = mydb.cursor()
        print(mydb, " Connected succesfully!!")
    except:
        mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'otheruser',
        password = 'swordfish'
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS records")




    print("""-----Menu-------\n
    1 - To insert Multiple record into Table
    2 - To Insert one data record into a Table
    3 - To view all Data in table
    4 - To search and print specific data
    5 - Select records that starts, includes, or ends with a given letter or prhase
    6 - To sort data in alphabetical order
    7 - To sort data in decending alphabetical order
    8 - To delete a record
    9 - To update existing record
    10 - To select the first 5 records
    11 - To select 5 records that start at a certian position
    99 - To Exit 
    """)
    user_input = ''
    while user_input != '99':
        user_input = input("Enter one of the menu options here: ")
        if user_input == '1':
            insert_multiple_data()

        elif user_input == '2':
            insert_data()
        elif user_input == '3':
            view_all()
        elif user_input == '4':
            count = 0
            while count < 3:

                select = input("""1 - to search by ID number
                2 - to search by name""")
                if select == '1':
                    search_id()
                    break
                elif select == '2':
                    search_name()
                    break
                else:
                    count+= 1
                    print("Not a valid entry")
            if count >= 3:
                print("sorry to many invalid options")

        elif user_input == '5':
            count= 0
            while count < 3:
                select = input("""
                1 - to search ID numbers
                2 - to search names""")
                if select == '1':
                    search_phrase_id()
                    break
                elif select == '2':
                    search_phrase_name()
                    break
                else:
                    count+= 1
                    print("Not a valid entry")
            if count >= 3:
                print("sorry to many invalid options")

        elif user_input == '6':
            count= 0
            while count < 3:

                select = input("""
                1 - to sort ID numbers: 
                2 - to sort names: """)
                if select == '1':
                    sort_id()
                    break
                elif select == '2':
                    sort_alpha_names()
                    break
                else:
                    count+= 1
                    print("Not a valid entry")
            if count >= 3:
                print("sorry to many invalid options")

        elif user_input == '7':
            count= 0
            while count < 3:

                select = input(""" 
                1 - to sort ID numbers in Decending order: 
                2 - to sort names in decending order: """)
                if select == '1':
                    sort_id_decending()
                    break
                elif select == '2':
                    sort_name_decending()
                    break
                else:
                    count+= 1
                    print("Not a valid entry")
            if count >= 3:
                print("sorry to many invalid options")

        elif user_input == '8':
            count= 0
            while count < 3:
                select = input("""
                1 - to Delete record with ID number:
                2 - to Delete record with name: """)
                if select == '1':
                    delete_record_by_id()
                    break
                elif select == '2':
                    delete_record_by_name()
                    break
                else:
                    count+= 1
                    print("Not a valid entry")
            if count >= 3:
                print("sorry to many invalid options")

        elif user_input == '9':
            count= 0
            while count < 3:
                select = input("""
                1 - to update a ID number: 
                2 - to update a name: """)
                if select == '1':
                    update_id()
                    break
                elif select == '2':
                    update_name()
                    break
                else:
                    count+= 1
                    print("Not a valid entry")
            if count >= 3:
                print("sorry to many invalid options")


        elif user_input == '10':
            view_first5_rows()


        elif user_input == '11':
            view_user_5rows()


        elif user_input == '99':
            print("Thank you!!\nGoodbye!!")
            break

        else:
            print("Invalid Option!")
            continue
        




if __name__ == "__main__":
    main()