from flask import make_response
from db_connect import db_connect
import json
class user_model():
    def __init__(self):
        self.db=db_connect()
        self.users=[]
    def add_new_users(self,data):
        print(data['name'])
        self.db.cursor.execute(f"INSERT INTO users(name, email, phone, age, password, role) VALUES('{data['name']}', '{data['email']}', '{data['age']}', '{data['phone']}','{data['password']}', '{data['role']}')")
        return make_response({"message":"CREATED SUCCESSFULLY"})
    def fetch_all_users(self):
         self.db.cursor.execute("SELECT * FROM users")
         result=self.db.cursor.fetchall()
         if len(result)>0:
            return {"payload":result}
         else: return "NO DATA FOUND"
    def fetch_single_user(self, id):
         self.db.cursor.execute(f"SELECT * FROM users where id ={id}")
         result=self.db.cursor.fetchall()
         if len(result)>0:
            return json.dumps(result)
         else: return "NO DATA FOUND"
    def update_user_mode(self, data):
        self.db.cursor.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', age='{data['age']}',password='{data['password']}',role='{data['role']}' WHERE id = {data['id']}")
        if self.db.cursor.rowcount>0:
            return make_response({"message":"UPDATED SUCCESSFULLY"})
        else: return make_response({"message":"NOTHING TO UPDATE"})
    def delete_user_model(self, id):
        print(id)
        self.db.cursor.execute(f"DELETE FROM users WHERE id ={id}")
        if self.db.cursor.rowcount>0:
            return ({"message":"User deleted successfully"})
        else: return ({"message":"Nothing to delete"})