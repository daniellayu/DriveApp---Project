import sqlite3


class Restaurant(object):
    def __init__(self, tableName="restaurant", restaurantId="restaurantId", restaurantType="restaurantType",
                 numOfWorkers="numOfWorkres", cityId="cityId"):
        self.__tableName = tableName
        self.__restaurantId = restaurantId
        self.__restaurantType = restaurantType
        self.__numOfWorkers = numOfWorkers
        self.__cityId = cityId
        conn = sqlite3.connect('test.db')
        str = "CREATE TABLE IF NOT EXISTS " + self.__tableName + "(" + self.__restaurantId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__restaurantType + " TEXT    NOT NULL ,"
        str += " " + self.__numOfWorkers + " TEXT    NOT NULL, "
        str += " " + self.__cityId + " INTEGER    NOT NULL) "
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_restaurant(self, restaurantType, numOfWorkers, cityId):
        conn = sqlite3.connect('test.db')
        str_insert = "INSERT INTO " + self.__tableName + " (" + self.__restaurantType + "," + self.__numOfWorkers + "," + self.__cityId + ") VALUES (" + "'" + restaurantType + "'" + "," + "'" + numOfWorkers + "'" + "," + "'" + str(
            cityId) + "');"
        print(str_insert)
        c = conn.execute(str_insert)
        print(c)
        conn.commit()
        conn.close()
        print("Record created successfully")
        return True

    def get_table_name(self):
        return self.__tableName

    def get_all_restaurant(self):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "select*from " + self.__tableName
        print(str1)
        cursor = conn.execute(str1)
        rows = cursor.fetchall()
        arr_restaurant = []
        for row in rows:
            str_rows = str(row[0]) + " " + row[1] + " " + str(row[2])
            arr_restaurant.append(str_rows)
        print(arr_restaurant)
        return arr_restaurant

    def delete_all_restaurant_by_id(self, restaurantId):
        conn = sqlite3.connect('test.db')
        str_delete = "DELETE  from " + self.__tableName + " where " + self.__restaurantId + "=" + "'" + str(restaurantId) + "'"
        print(str_delete)
        conn.execute(str_delete)
        conn.commit()
        conn.close()
        print("Record deleted successfully")
        return "seccuss deleted"

    def update_restaurant(self, restaurantId, restaurantType, numOfWorkers, cityId):
        try:
            conn = sqlite3.connect('test.db')
            str_update = " UPDATE " + self.__tableName
            str_update += " set " + " " + self.__restaurantType + "=" + "'" + restaurantType + "',"
            str_update += self.__numOfWorkers + "=" + "'" + numOfWorkers + "',"
            str_update += self.__cityId + "=" + "'" + str(cityId) + "'"
            str_update += " WHERE " + self.__restaurantId + "=" + "'" + str(restaurantId) + "'"
            print(str_update)
            conn.execute(str_update)
            conn.commit()
            conn.close()
            return "Success"
        except:
            print("error")
            return "Failed to restaurant"
        conn.close()


class Cities(object):
    def __init__(self, tablename="City", Id="Id", cityname="cityname"):
        self.__tablename = tablename
        self.__Id = Id
        self.__cityname = cityname
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__Id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__cityname + " TEXT NOT NULL) "
        print(str)
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def get_table_name(self):
        return self.__tablename

    def select_all_cities(self):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "select*from " + self.__tablename
        # strsql = "SELECT question, category,botAnswer, nextID from  " + self._tablename + " where " + self._category + "=" + "'"+str(category)+"'"
        print(str1)
        cursor = conn.execute(str1)
        rows = cursor.fetchall()
        arr = []
        for row in rows:
            str_rows = str(row[0]) + " " + row[1]
            arr.append(str_rows)
        print(arr)
        return arr

    def insert_city(self, cityname):
        conn = sqlite3.connect('test.db')
        str_insert = "INSERT INTO " + self.__tablename + " (" + self.__cityname + ") VALUES (" + "'" + cityname + "');"
        print(str_insert)
        c = conn.execute(str_insert)
        print(c)
        conn.commit()
        conn.close()
        print("Record created successfully")
        return True

    def delete_username(self, cityname):
        conn = sqlite3.connect('test.db')
        str_delete = "DELETE  from " + self.__tablename + " where " + self.__cityname + "=" + "'" + str(cityname) + "'"
        print(str_delete)
        conn.execute(str_delete)
        conn.commit()
        conn.close()
        print("Record deleted successfully")

    def check_city_by_cityname(self, cityname):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        strsql = "SELECT * from " + self.__tablename + " where " + self.__cityname + "=" + "'" + str(cityname) + "'"
        print(strsql)
        cursor = conn.execute(strsql)
        row = cursor.fetchone()
        if row:
            print("exist")
            return True
        else:
            print("not exist")
            return False
        conn.commit()
        conn.close()

    def _str_(self):
        return "table  name is ", self.__tablename


def inner():
    conn = sqlite3.connect('test.db')
    str1 = (
        """ SELECT restaurantId, restaurantType, numOfWorkres, City.cityname FROM City INNER JOIN flights ON flights.cityId = City.Id """)
    print(str1)
    x = conn.execute(str1)
    for row in x:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
    conn.commit()
    conn.close()


r = Restaurant()
r.insert_restaurant("dairy", "32", "2")
r.insert_restaurant("meat", "20", "1")
r.insert_restaurant("vegetarian", "30", "3")
r.insert_restaurant("vegetarian", "15", "2")
r.insert_restaurant("dairy", "28", "1")
r.get_all_restaurant()
