from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "<h1> Home page </h1>"

@app.route('/user/login', methods = ['GET'])
def login():
    return "<h1> Login thành công </h1>"


if __name__ == "__main__":
    app.run(host = '127.0.0.1',port = '5000',debug = True, threaded = True)
