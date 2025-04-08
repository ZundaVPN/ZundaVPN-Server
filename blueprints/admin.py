from flask import Blueprint, request, jsonify
import logging, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # WTF
import modules


bp = Blueprint('admin', __name__)

@bp.route("/api/admin/register", methods=["POST"])
def register():
    logging.log(logging.DEBUG, "requested register")
    data = request.get_json()
    logging.debug(data)
    username = data["username"]
    password = data["password"]
    if username == "" or password == "":
        logging.error(f"username or password is empty\n{data}")
        return jsonify({"message":"username or password is empty"}), 400
    password = modules.encrypt(password)
    logging.debug(password)
    if modules.db_manager.search("username", username): return jsonify({"message":"user already exists"}), 400
    if modules.db_manager.reg_request(username, password) == True:
        return jsonify({"message":"register success"}), 200
    logging.log(logging.DEBUG, "auth endpoint")
    logging.error(f"register failed\nusername : {username}\npassword : {password}")
    return jsonify({"message":"Failed"}),500