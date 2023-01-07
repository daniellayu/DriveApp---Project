import sqlite3

class TeacherStudentDb(object):
    def __init__(self, tablename="TeacherStudentDb", teacherStudentId="teacherStudentId", teacherId="teacherId", studentId="studentId"):
        self.__tablename = tablename
        self.__teacherStudentId = teacherStudentId
        self.__teacherId = teacherId
        self.__studentId = studentId
        self.create_table()

    def create_table(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {self.__tablename} (
                        {self.__teacherStudentId} INTEGER PRIMARY KEY,
                        {self.__teacherId} INTEGER NOT NULL,
                        {self.__studentId} INTEGER NOT NULL,
                    );
                            """
            cursor.execute(create_table_query)
            connection.commit()
            connection.close()
            print("succeed to create table TeacherStudentDb")
            return True
        except:
            print("failed to create table TeacherStudentDb")
            return False