import hashlib
import sqlite3

class User(object):
    def __init__(self, tablename = "Users", Id = "Id", email = "email", password = "password", firstname = "firstname"):
        self.__tablename = tablename
        self.__Id = Id
        self.__email = email
        self.__password = password
        self.__firstname = firstname

        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__Id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__email + " TEXT    NOT NULL ,"
        str += " " + self.__password + " TEXT    NOT NULL, "
        str += " " + self.__firstname + " TEXT    NOT NULL) "
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename
    def select_all_users(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_users = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + str(row[2])
                arr_users.append(str_rows)
            print(arr_users)
            return arr_users
        except:
            return False
    def insert_user(self, email,  password, firstname):
        try:
            conn = sqlite3.connect('test.db')
            salt = 'ABCD'
            salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            print(salt_password)
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__email + "," + self.__password + "," + self.__firstname + ") VALUES (" + "'" + email + "'" + "," + "'" + password + "'" + "," + "'" + firstname + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert user")
            return False
    def delete_by_firstname(self, email):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__email + "=" + "'"+str(email)+"'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def is_exist(self, email, password):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        salt = 'ABCD'
        salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
        str_check = "SELECT * from " + self.__tablename + " where " + self.__email + " = '" +email +"' and " +self.__password+" = '"+str(password)+"'"
        print(str_check)
        cursor = conn.execute(str_check)
        row = cursor.fetchall()
        if row:
            print("Exist")
            return True
        else:
            print("Not exist")
            return False
    def return_user_by_email(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            salt = 'ABCD'
            salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            print(salt_password)
            strsql = "SELECT * from " + self.__tablename + " where " + self.__email + "=" + "'" + str(email) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            if row:
                return [row[0], row[1], row[2]]
            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False
    def __str__(self):
        return "table  name is ", self.__tablename


#u=User()
#u.insert_user("u@x.com", "oron", 'yaron')
#u.insert_user("v@y.com", "dvidi", 'davidi')
#u.insert_user("t@a.com", "aba", 'origin')
#u.select_all_users()
#u.check_user_by_username("Asaf")
#u.delete_username("Asaf")
#u.check_user_by_username("Asaf")
#user=u.return_user_by_email('u@x.com')
#print(user[0])
#print(user)