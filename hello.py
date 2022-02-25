from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World from Flask!</h1>'
@app.route('/tes')
def hello_tes():
    return '<h1>Hello World from Tes!</h1>'

@app.route('/flask')
def hello_flask():
    return '<h1>Hello World from Flask!</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)