import sqlite3

class TeacherDb(object):
    def __init__(self, tablename = "TeacherDb", teacherId = "teacherId", firstname = "firstname", lastname = "lastname", email = "email", phonenumber = "phonenumber", Id = "Id", password = "password", price = "price", experience = "experience"):
        self.__tablename = tablename
        self.__teacherId = teacherId
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__phonenumber = phonenumber
        self.__Id = Id
        self.__price = price
        self.__experience = experience
        self.create_table()

    def create_table(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {self.__tablename} (
                    {self.__teacherId} INTEGER PRIMARY KEY,
                    {self.__firstname} TEXT NOT NULL,
                    {self.__lastname} TEXT NOT NULL,
                    {self.__email} TEXT NOT NULL UNIQUE,
                    {self.__password} TEXT NOT NULL,
                    {self.__phonenumber} TEXT NOT NULL,
                    {self.__Id} INTEGER NOT NULL,
                    {self.__price} INTEGER NOT NULL,
                    {self.__experience} INTEGER NOT NULL
                );
                        """
        cursor.execute(create_table_query)
        connection.commit()
        connection.close()

    def insert(self, firstname, lastname, email, password, phonenumber, Id, price, experience):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        insert_query = f"INSERT INTO {self.__tablename} ({self.__firstname}, {self.__lastname}," \
                       f" {self.__email}, {self.__password}, {self.__phonenumber}, {self.__Id}, {self.__price}," \
                       f" {self.__experience}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(insert_query, (firstname, lastname, email, password, phonenumber, Id, price, experience))

        connection.commit()#release db
        connection.close()

    def get_all_teachers(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        select_query = f"SELECT * FROM {self.__tablename}"
        cursor.execute(select_query)

        teachers = cursor.fetchall()

        connection.close()

        return teachers

    def delete_by_id(self, teacher_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()

            delete_query = f"DELETE FROM {self.__tablename} WHERE {self.__teacherId} = ?"
            cursor.execute(delete_query, (teacher_id,))

            connection.commit()
            connection.close()
            print("success")
            return True
        except:
            print("failed to delete by id")
            return  False

    def update_by_id(self, teacher_id, firstname, lastname, email, password, phonenumber, Id, price, experience):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        update_query = f"UPDATE {self.__tablename} SET {self.__firstname} = ?, {self.__lastname} = ?, {self.__email} = ?, {self.__password} = ?, {self.__phonenumber} = ?, {self.__Id} = ?, {self.__price} = ?, {self.__experience} = ? WHERE {self.__teacherId} = ?"
        cursor.execute(update_query,
                       (firstname, lastname, email, password, phonenumber, Id, price, experience, teacher_id))

        connection.commit()
        connection.close()




t = TeacherDb()
#t.insert("dani1", "yusu1", "danngi23", "p1", "34551", "1231", "1501", "31")
x = t.get_all_teachers()
print(x)
print(x[0][0])#1
t.delete_by_id(1)
