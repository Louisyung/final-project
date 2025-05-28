# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 模擬使用者資料
users = {"test": "1234"}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify(message="登入成功")
    else:
        return jsonify(message="帳號或密碼錯誤"), 401

if __name__ == '__main__':
    app.run(port=3000)
