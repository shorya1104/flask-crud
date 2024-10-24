import mysql.connector
from dotenv import load_dotenv
import os
class db_connect():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'),password=os.getenv('DB_PASSWORD'),database=os.getenv('DB_DATABASE'))
            self.cursor = self.con.cursor(dictionary=True)
            self.con.autocommit=True
            print("Connection Successfull")
        except mysql.connector.Error as err:
            print("Connection error",err)
    def close(self):
        if self.con:
            self.cursor.close()
            self.con.close()
            print("Connection closed")