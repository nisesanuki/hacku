from flask import Flask, jsonify, abort, make_response, render_template, request, redirect, url_for, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
import qrcode

api = Flask(__name__)
CORS(api)  # CORS有効化
api.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# ログイン API
@api.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # SQL 実行
    connection = MySQLdb.connect(
        host = 'localhost',
        user = 'hacku',
        password = 'hacku',
        db = 'hacku')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM hacku.users WHERE email='" + email + "';" )

    connection.commit()
    connection.close()

    cnt = len(list(cursor.fetchall()))

    # ログイン可否判定
    if cnt >= 1:
        # ログイン成功時: 通知とセッション開始
        session[email] = email
        return session[email]
    else:
        return "NO"

# ログアウト API
@api.route('/logout', methods=['POST'])
def logout():
    session.pop(request.form[email])
    return redirect('http://localhost/~skomatsu')
        

# ユーザ登録 API
@api.route('/regist', methods=['POST'])
def regist():
    email = request.form['email']
    password = ['password']

    # SQL 実行
    connection = MySQLdb.connect(
        host = 'localhost',
        user = 'hacku',
        password = 'hacku',
        db = 'hacku')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO hacku.users VALUE")

    connection.commit()
    connection.close()

    # 実行結果処理
    

# QR 登録処理
@api.route('/genqr', methods=['POST'])
def genqr():
    email = request.form['email']
    qrname = request.form['qrname']
    
    # SQL 実行
    connection = MySQLdb.connect(
        host = 'localhost',
        user = 'hacku',
        password = 'hacku',
        db = 'hacku')
    cursor = coonection.cursor()

    cursor.execute("INSERT INTO hacku.user VALUE")

    connection.commit()
    connection.close()

    # 実行結果処理

# QR 一覧表示
@api.route('/listqr', methods=['POST'])
def listqr():
    email = request.form['email']
    
    # SQL 実行
    connection = MySQLdb.connect(
        host = 'localhost',
        user = 'hacku',
        password = 'hacku',
        db = 'hacku')
    cursor = coonection.cursor()

    cursor.execute("INSERT INTO hacku.user VALUE")

    connection.commit()
    connection.close()

    return cursor

# 登録成功時の処理
@api.route('/regist_success', methods=['POST'])
def regist_success():
    pass
    # メール送信等

# 37564番ポートでWebサーバを起動する
if __name__ == '__main__':
    api.run(host='0.0.0.0', port=37564, debug=True)
