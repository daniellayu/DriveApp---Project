import sqlite3

class StudentDb(object):
    def __init__(self, tablename="StudentDb", studentId="teacherId", firstname="firstname", lastname="lastname", email="email", phonenumber="phonenumber", Id="Id", password="password"):
        self.__tablename = tablename
        self.__studentId = studentId
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__phonenumber = phonenumber
        self.__Id = Id
        self.create_table()

    def create_table(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {self.__tablename} (
                        {self.__studentId} INTEGER PRIMARY KEY,
                        {self.__firstname} TEXT NOT NULL,
                        {self.__lastname} TEXT NOT NULL,
                        {self.__email} TEXT NOT NULL UNIQUE,
                        {self.__password} TEXT NOT NULL,
                        {self.__phonenumber} TEXT NOT NULL,
                        {self.__Id} INTEGER NOT NULL
                    );
                            """
            cursor.execute(create_table_query)
            connection.commit()
            connection.close()
            print("succeed to create table StudentDb")
            return True
        except:
            print("failed to create table StudentDb")
            return False

    def insert(self, firstname, lastname, email, password, phonenumber, Id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            insert_query = f"INSERT INTO {self.__tablename} ({self.__firstname}, {self.__lastname}," \
                           f" {self.__email}, {self.__password}, {self.__phonenumber}, {self.__Id}" \
                           f" ) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_query, (firstname, lastname, email, password, phonenumber, Id))
            connection.commit()#release db
            connection.close()
            print("succeed to insert student")
            return True
        except:
            print("failed to insert student")
            return False

    def get_all_students(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT * FROM {self.__tablename}"
            cursor.execute(select_query)
            teachers = cursor.fetchall()
            connection.close()
            print("succeed to get all students")
            return teachers
        except:
            print("failed to get all students")
            return False

    def delete_by_id(self, student_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            delete_query = f"DELETE FROM {self.__tablename} WHERE {self.__studentId} = ?"
            cursor.execute(delete_query, (student_id,))
            connection.commit()
            connection.close()
            print("succeed to delete student by id")
            return True
        except:
            print("failed to delete student by id")
            return False

    def is_exist(self, id, password):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str_check = "SELECT * from " + self.__tablename + " where " + self.__Id + " = '" +id +"' and " +self.__password+" = '"+str(password)+"'"
        print(str_check)
        cursor = conn.execute(str_check)
        row = cursor.fetchall()
        if row:
            print("student exist")
            return True
        else:
            print("student not exist")
            return False


# s = StudentDb()
# s.insert("ana", "cohen", "anacgmail", "ana123", "05224", "32456")
#x = s.get_all_students()
#print(x)
#s.delete_by_id(1)
