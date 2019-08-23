from flask import Flask, jsonify, abort, make_response, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import MySQLdb

api = Flask(__name__)
CORS(api)  # CORS有効化

@api.route('/get', methods=['GET'])  # Getだけ受け付ける
def get():  # 関数名は重複していなければなんでもよい
    result = ""
    # ローカルのファイルを全部読み込んで返すだけ
    with open("./datafile", mode='r') as f:
        result += f.read()
    return result

@api.route('/post', methods=['POST'])  # Postだけ受け付ける
def post():
    result = request.form["param"]  # Postで送ったときのパラメータの名前を指定する
    # パラメータをローカルのファイルに書き込むだけ
    with open("./datafile", mode='a') as f:
        f.write(result + "\n")
    return make_response(result)


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
    
    for row in cursor:
        print(row)


    # ログイン可否判定
    if cursor == ():
        return "あはは"
    else:
        return "ふぇぇ"


# 4000番ポートでWebサーバを起動する
if __name__ == '__main__':
    api.run(host='0.0.0.0', port=37564, debug=True)
