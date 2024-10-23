#router
from app import app
from model.user_model import user_model
from flask import request, jsonify, abort
from db_connect import db_connect
obj=user_model()

@app.route('/users')
def get_all_users():
    return obj.fetch_all_users()

@app.route('/users/<id>')
def get_single_users(id):
    return obj.fetch_single_user(id)

@app.route("/user/adduser", methods=["POST"])
def adduser():
    if not request.form or 'name' not in request.form or 'age' not in request.form or 'email' not in request.form:
            abort(400)  # Bad request if any field is missing
    return obj.add_new_users(request.form)

@app.route("/user/update", methods=["PUT"])
def updateuser():
    return obj.update_user_mode(request.form)

@app.route("/users/delete/<id>", methods=["DELETE"])
def delete_users(id):
    return obj.delete_user_model(id)