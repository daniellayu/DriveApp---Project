import sqlite3

class LessonsDb(object):
    def __init__(self, tablename="LessonsDb", lessonId="lessonId", teacherId="teacherId", studentId="studentId", date="date", time="time", price="price"):
        self.__tablename = tablename
        self.__lessonId = lessonId
        self.__teacherId = teacherId
        self.__studentId = studentId
        self.__date = date
        self.__time = time
        self.__price = price
        self.create_table()

    def create_table(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {self.__tablename} (
                        {self.__lessonId} INTEGER PRIMARY KEY,
                        {self.__teacherId} INTEGER NOT NULL,
                        {self.__studentId} INTEGER NOT NULL,
                        {self.__date} TEXT NOT NULL,
                        {self.__time} INTEGER NOT NULL,
                        {self.__price} INTEGER NOT NULL,
                    );
                            """
            cursor.execute(create_table_query)
            connection.commit()
            connection.close()
            print("succeed to create table LessonsDb")
            return True
        except:
            print("failed to create table LessonsDb")
            return False


    def get_date_and_time_by_id(self):
        pass

    def delete_lesson_by_id(self, lesson_id):
        pass

    def get_price(self):
        pass

    def insert_lesson(self):
        pass