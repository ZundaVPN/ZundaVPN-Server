from flask import Flask, jsonify
from dotenv import load_dotenv
import blueprints.auth as auth
import blueprints.admin as admin
import os, logging

load_dotenv()
if os.getenv("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Debug enabled")
else:
    logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.register_blueprint(auth.bp)
app.register_blueprint(admin.bp)

@app.route("/")
def teapot():
    logging.debug("requested teapot")
    return "I'm a teapot!", 418

@app.errorhandler(405)
def method_not_allowed(e):
    logging.warning(f"requested 405\n{e}")
    return jsonify({"message":"method_not_allowed"}), 405

@app.errorhandler(404)
def not_found(e):
    logging.warning(f"requested 404\n{e}")
    return jsonify({"message":"not_found"}), 404


if __name__ == "__main__": app.run(debug=os.getenv("DEBUG"), port=os.getenv("PORT"))