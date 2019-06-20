import threading

from flask import Flask
from flask import render_template
from flask import jsonify

from retro_snake.snake import Snake


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
    snake.move_up()
    return resp

@app.route('/snake/down')
def snake_down():
    print("DOWN")
    resp = jsonify(success=True)
    snake.move_down()
    return resp
    
@app.route('/snake/left')
def snake_left():
    print("LEFT")
    resp = jsonify(success=True)
    snake.move_left()
    return resp

@app.route('/snake/right')
def snake_right():
    print("RIGHT")
    resp = jsonify(success=True)
    snake.move_right()
    return resp


snake = Snake(16, 16)
f_stop = threading.Event()
snake.update(f_stop) # start calling update now and every 1 sec thereafter

# start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
