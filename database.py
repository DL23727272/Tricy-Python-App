import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="twa"
        )
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def register_user(self, username, password):
        try:
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            values = (username, password)
            self.cursor.execute(sql, values)
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def login_user(self, username, password):
        try:
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            values = (username, password)
            self.cursor.execute(sql, values)
            user = self.cursor.fetchone()
            if user:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
        
    def insert_booking(self, name, address, contact_number, pickup_area, destination, num_persons):
        try:
            sql = "INSERT INTO bookings (name, address, contact_number, pickup_area, destination, num_persons) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, address, contact_number, pickup_area, destination, num_persons)
            self.cursor.execute(sql, values)
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False