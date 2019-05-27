from time import sleep
import random
import sys

from retro_snake.matriz import get_canvas


# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting
# From: https://gist.github.com/sanchitgangwar/2158089

class Snake:

	def __init__(self, width=8, height=8):
		# canvas: https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html#module-PIL.ImageDraw
		self.width = width
		self.height = height
		self.canvas = get_canvas(width, height)
		self.direccion = (1, 0)  # right
		self.finalizar = False
		
		center_width = (int)(width/2)
		center_height = (int)(height/2)
		head = (center_width, center_height)
		center = (center_width - 1, center_height)
		tail = (center_width - 2, center_height)
		self.snake = (tail, center, head)
		self.food = (2, 2)
	
	def render(self):
		with self.canvas as draw:
			# draw.line(to_tuple(self.snake), fill="white")
			# draw.point(to_tuple(self.food), fill="white")
			# draw.line(self.snake, fill="white")
			# draw.point(self.food, fill="white")
			for point in self.snake:
				draw.point(point, fill="white")

	
	def update(self):
		new_snake = ()
		for point in self.snake:
			point = add_tuples(point, self.direccion)
			if point[0] == self.width: point = (0, point[1])
			new_snake += (point,)
		self.snake = new_snake
		print(self.snake)
	
	def run(self):
		# while not self.finalizar:
		# self.render()
		# self.update()
		# sleep(1)
		# self.render()
		# sleep(1)
		with self.canvas as draw:
			draw.point((0, 0), fill="white")
		sleep(1)
		with self.canvas as draw:
			draw.point((1, 1), fill="white")
		sleep(1)


def to_tuple(t):
    return tuple(map(to_tuple, t)) if isinstance(t, (list, tuple)) else t

def add_tuples(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])


# snake = [[4,10], [4,9], [4,8]]                                     # Initial snake co-ordinates
# food = [10,20]                                                     # First food co-ordinates

# win.addch(food[0], food[1], '*')                                   # Prints the food

# while key != 27:                                                   # While Esc key is not pressed
#     win.border(0)
#     win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
#     win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
#     win.timeout(150 - (len(snake)/5 + len(snake)/10)%120)          # Increases the speed of Snake as its length increases
    
#     prevKey = key                                                  # Previous key pressed
#     event = win.getch()
#     key = key if event == -1 else event 


#     if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
#         key = -1                                                   # one (Pause/Resume)
#         while key != ord(' '):
#             key = win.getch()
#         key = prevKey
#         continue

#     if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
#         key = prevKey

#     # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
#     # This is taken care of later at [1].
#     snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

#     # If snake crosses the boundaries, make it enter from the other side
#     if snake[0][0] == 0: snake[0][0] = 18
#     if snake[0][1] == 0: snake[0][1] = 58
#     if snake[0][0] == 19: snake[0][0] = 1
#     if snake[0][1] == 59: snake[0][1] = 1

#     # Exit if snake crosses the boundaries (Uncomment to enable)
#     #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

#     # If snake runs over itself
#     if snake[0] in snake[1:]: break

    
#     if snake[0] == food:                                            # When snake eats the food
#         food = []
#         score += 1
#         while food == []:
#             food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
#             if food in snake: food = []
#         win.addch(food[0], food[1], '*')
#     else:    
#         last = snake.pop()                                          # [1] If it does not eat the food, length decreases
#         win.addch(last[0], last[1], ' ')
#     win.addch(snake[0][0], snake[0][1], '#')
    
# curses.endwin()
# print("\nScore - " + str(score))
# print("http://bitemelater.in\n")
