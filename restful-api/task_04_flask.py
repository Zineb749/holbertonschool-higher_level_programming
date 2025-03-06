#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}


ERROR_USER_NOT_FOUND = {"error": "User not found"}
ERROR_USERNAME_REQUIRED = {"error": "Username is required"}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify(ERROR_USER_NOT_FOUND), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify(ERROR_USERNAME_REQUIRED), 400


    users.clear()


    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
