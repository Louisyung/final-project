from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

USERS_FILE = 'users.json'

# 載入使用者資料
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# 儲存使用者資料
def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

@app.route('/')
def intro_screen():
    return render_template('introScreen.html')

# 登入
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if username in users and users[username] == password:
            return jsonify(message="登入成功")
        else:
            return jsonify(message="帳號或密碼錯誤"), 401
    # GET 請求時回傳登入頁面
    return render_template('login.html')

# 註冊
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = load_users()
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify(message="帳號和密碼不能為空"), 400
        if username in users:
            return jsonify(message="帳號已存在"), 409
        users[username] = password
        save_users(users)
        return jsonify(message="註冊成功")
    # GET 請求時回傳註冊頁面
    return render_template('register.html')

if __name__ == '__main__':
    app.run(port=3000)