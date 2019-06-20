from time import sleep
from random import random
import threading
import asyncio
import random
import sys

from luma.core.virtual import viewport
from luma.core.render import canvas
from PIL import ImageFont
import pygame

from retro_snake.matriz import get_device



# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting
# From: https://gist.github.com/sanchitgangwar/2158089

class Snake:

	RIGHT = (1, 0)
	LEFT = (-1, 0)
	UP = (0, -1)
	DOWN = (0, 1)
	NONE = (0,0)

	def __init__(self, width=8, height=8):
		# canvas: https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html#module-PIL.ImageDraw
		self.width = width
		self.height = height
		self.device = get_device(width, height)
		self.direccion = self.RIGHT
		self.died = True
		
		center_width = (int)(width/2)
		center_height = (int)(height/2)
		head = (center_width, center_height)
		center = (center_width - 1, center_height)
		tail = (center_width - 2, center_height)
		self.snake = [head, center, tail] # list of tuples
		self.generate_random_food()
	
	def render(self):
		virtual = viewport(self.device, width=200, height=200)
		if self.died:
			with canvas(virtual) as draw:
				draw.rectangle(((0, 0), draw.im.size), fill="black", outline="black")
				font = ImageFont.truetype('retro_snake/fonts/pixelmix.ttf', 8)
				draw.multiline_text((2, 0), "Game\nover", fill="white", font=font, spacing=-1, align='center')
			
			while True:
				for offset in range(12):
					virtual.set_position((offset, 0))
					sleep(0.5)

		else:
			with canvas(virtual) as draw:
				draw.rectangle(((0, 0), draw.im.size), fill="black", outline="black")
				draw.point(self.food, fill="white")
				for point in self.snake:
					draw.point(point, fill="white")
	
	def update(self, f_stop):
		head = add_tuples(self.snake[0], self.direccion)

		if head[0] == self.width: head = (0, head[1]) # borde derecho
		if head[1] == self.height: head = (head[0], 0) # borde inferior

		if head[0] == -1: head = (self.width - 1, head[1]) # borde izquierdo
		if head[1] == -1: head = (head[0], self.height - 1) # borde superior

		self.snake = [head] + self.snake[:-1]

		if head[0] == self.food[0] and head[1] == self.food[1]: # snake eats food
			tail = add_tuples(self.snake[-1], self.NONE)
			self.snake = self.snake + [tail]
			self.generate_random_food()

		# Check if snake eats itself
		for point in self.snake[1:]:
			if head[0] == point[0] and head[1] == point[1]:
				self.died = True
				print("died!")
				self.render()
				return

		self.render()
		if not f_stop.is_set():
			# call update again in 1 seconds
			threading.Timer(0.7, self.update, [f_stop]).start()


	def move_right(self):
		if not self.direccion == self.LEFT:
			self.direccion = self.RIGHT

	def move_left(self):
		if not self.direccion == self.RIGHT:
			self.direccion = self.LEFT

	def move_up(self):
		if not self.direccion == self.DOWN:
			self.direccion = self.UP

	def move_down(self):
		if not self.direccion == self.UP:
			self.direccion = self.DOWN

	def generate_random_food(self):
		self.food = random_tuple(self.width, self.height)
		while(self.food in self.snake):
			self.food = random_tuple(self.width, self.height)



def to_tuple(t):
    return tuple(map(to_tuple, t)) if isinstance(t, (list, tuple)) else t

def add_tuples(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def random_tuple(t1_max, t2_max):
	return (int(random.random()*t1_max),int(random.random()*t2_max))



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
