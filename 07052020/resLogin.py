from flask import Flask, request,jsonify
from checkLogin import CheckLogin
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "<h1> Home page </h1>"

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        us = request.form['username']
        ps = request.form['password']
        if CheckLogin(us,ps):
            return jsonify({"Login":"Đăng Nhập Thành Công!"})
        else:
            return jsonify({"Login":"Đăng Nhập Không Thành Công!"})
@app.route('/loginjson', methods = ['POST'])
def loginWithJson():
    if request.method == 'POST':
        data = request.get_json()
        us = data['username']
        ps = data['password']
        if CheckLogin(us,ps):
            return jsonify({"Login":"Đăng Nhập Thành Công!"})
        else:
            return jsonify({"Login":"Đăng Nhập Không Thành Công!"})
if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = '5000')