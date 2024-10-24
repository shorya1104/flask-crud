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
        return make_response({"message":"CREATED SUCCESSFULLY"},201)
    def fetch_all_users(self):
         self.db.cursor.execute("SELECT * FROM users")
         result=self.db.cursor.fetchall()
         if len(result)>0:
            return make_response({"payload":result},200)
         else: return make_response({"message":"NO DATA FOUND"},204)
    def fetch_single_user(self, id):
         self.db.cursor.execute(f"SELECT * FROM users where id ={id}")
         result=self.db.cursor.fetchall()
         if len(result)>0:
            return make_response({"payload":result},200)
         else: return make_response({"message":"NO DATA FOUND"},204)
    def update_user_mode(self, data):
        self.db.cursor.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', age='{data['age']}',password='{data['password']}',role='{data['role']}' WHERE id = {data['id']}")
        if self.db.cursor.rowcount>0:
            return make_response({"message":"UPDATED SUCCESSFULLY"},201)
        else: return make_response({"message":"NOTHING TO UPDATE"},202)
    def delete_user_model(self, id):
        print(id)
        self.db.cursor.execute(f"DELETE FROM users WHERE id ={id}")
        if self.db.cursor.rowcount>0:
            return make_response({"message":"User deleted successfully"},200)
        else: return make_response({"message":"Nothing to delete"},202)
    def patch_user_model(self, data, id):
        qry = "UPDATE users SET "
        for key in data:
            qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id={id}"
        self.db.cursor.execute(qry)
        if self.db.cursor.rowcount>0:
            return make_response({"message":"User details updated successful"},201)
        else: return make_response({"message":"NOTHING TO UPDATE"},202)
    def user_pagination_model(self,limit,page_no):
        limit = int(limit)
        page_no = int(page_no)
        start_pont=(page_no*limit)-limit
        qry=f"SELECT * FROM users LIMIT {start_pont}, {limit}"
        self.db.cursor.execute(qry)
        result = self.db.cursor.fetchall()
        if len(result)>0:
            res = make_response({"payload":result, "page_no":page_no, "limit":limit}, 200)
            return res
        else: return make_response({"message":"NO DATA FOUND"},204)
    def uploaded_file_save_db(self, uid, path):
        self.db.cursor.execute(f"UPDATE users SET avatar='{path}' WHERE id = {uid}")
        if self.db.cursor.rowcount>0:
            return make_response({"message": "File uploaded and path saved in db"},201)
        else: make_response({"message": "Nothing to update"},202)