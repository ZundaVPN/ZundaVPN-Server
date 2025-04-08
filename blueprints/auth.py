from flask import Flask, jsonify, Blueprint, request
from dotenv import load_dotenv
import os, jwt, bcrypt, logging, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # WTF
import modules

database = 'user.db'
load_dotenv()
bp = Blueprint('auth', __name__)

test = {
    "message":"test"
}


@bp.route("/api/auth", methods=["POST"])
def auth():
    logging.log(logging.DEBUG, "requested auth")

    logging.log(logging.DEBUG, "auth endpoint")
    logging.log(logging.DEBUG, f"final return value is ")
    return jsonify(test), 200


