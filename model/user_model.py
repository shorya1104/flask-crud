from flask import make_response
class user_model():
    def __init__(self):
        self.users=[]
    def add_new_users(self,data):
            self.users.append(data)
            print(self.users)
            return make_response({"message":"CREATED SUCCESSFULLY"})
    def fetch_all_users(self):
        if len(self.users)>0:
            return self.users
        else: return "NO DATA FOUND"
    def delete_user_model(self, id):
        print(id)
        self.users=[]
        # self.users.pop(1)
        return ({"message":"User deleted successfully"})