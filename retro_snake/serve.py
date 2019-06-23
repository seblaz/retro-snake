import threading

from flask import Flask
from flask import render_template
from flask import jsonify

from retro_snake.snake import Snake


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello_world.html')


@app.route('/snake')
def snake():
    return render_template('snake.html', score=0)


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


if __name__ == '__main__':
    snake = Snake(16, 16)  # start the game
    f_stop = threading.Event()
    snake.update(f_stop)  # start calling update now and every 1 sec thereafter
    app.run(host='0.0.0.0')  # start the server
