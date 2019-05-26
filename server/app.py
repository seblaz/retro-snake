from flask import Flask
from flask import render_template
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('helloWorld.html', name=name)

@app.route('/snake')
def snake():
    return render_template('snake.html', score = 0)

@app.route('/snake/up')
def snake_up():
    print("UP")
    resp = jsonify(success=True)
    return resp

@app.route('/snake/down')
def snake_down():
    print("DOWN")
    resp = jsonify(success=True)
    return resp
    
@app.route('/snake/left')
def snake_left():
    print("LEFT")
    resp = jsonify(success=True)
    return resp

@app.route('/snake/right')
def snake_right():
    print("RIGHT")
    resp = jsonify(success=True)
    return resp