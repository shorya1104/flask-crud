#router
from app import app
from model.user_model import user_model
from flask import request, jsonify, abort, send_file,make_response
from db_connect import db_connect
from datetime import datetime
from  validators import validate_user, ValidationError, validate_user_update

obj=user_model()
@app.route('/users')
def get_all_users():
    return obj.fetch_all_users()

@app.route('/users/<id>')
def get_single_users(id):
    return obj.fetch_single_user(id)

@app.route("/user/signup", methods=["POST"])
def signup():
    try:
        validated_data = validate_user(request.form)
    except ValidationError as err:
        return make_response({"message":err.messages}), 400
    return obj.add_new_users(request.form)

@app.route("/user/update", methods=["PUT"])
def update_user():
    return obj.update_user_mode(request.form)

@app.route("/users/delete/<id>", methods=["DELETE"])
def delete_users(id):
    return obj.delete_user_model(id)

@app.route("/users/patch/<id>", methods=["PATCH"])
def patch_users(id):
    try:
        validated_data = validate_user_update(request.form)
    except ValidationError as err:
        return make_response({"message":err.messages}), 400
    return obj.patch_user_model(request.form,id)

# data table pagination
@app.route("/user/getall/limit/<limit>/page/<page_no>",methods=["GET"])
def user_pagination(limit, page_no):
    return obj.user_pagination_model(limit, page_no)

#File uploading
@app.route("/user/<uid>/upload/avatar",methods=["PUT"])
def upload_file(uid):
    upload_file=request.files['avatar']
    unique_file_name=datetime.now().timestamp()
    unique_file_name=(str(unique_file_name)).replace(".", "")
    ext=str(upload_file.filename).split('.')
    ext=ext[len(ext)-1]
    path=f"uploads/{unique_file_name}.{ext}"
    upload_file.save(path)
    return obj.uploaded_file_save_db(uid,path)
@app.route("/uploads/<filename>")
def user_get_file(filename):
    return send_file(f"uploads/{filename}")