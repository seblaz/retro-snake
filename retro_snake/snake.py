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


class Snake:

    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    NONE = (0, 0)

    def __init__(self, width=8, height=8):
        # canvas: https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html#module-PIL.ImageDraw
        self.width = width
        self.height = height
        self.device = get_device(width, height)
        self.direccion = self.next_direccion = self.RIGHT
        self.died = False

        # Create snake
        center_width = (int)(width/2)
        center_height = (int)(height/2)
        head = (center_width, center_height)
        center = (center_width - 1, center_height)
        tail = (center_width - 2, center_height)
        self.snake = [head, center, tail]  # list of tuples

        # Create food
        self.generate_random_food()

    def render(self):
        """Writes the game to the device."""
        virtual = viewport(self.device, width=200, height=200)
        if self.died:
            with canvas(virtual) as draw:
                draw.rectangle(((0, 0), draw.im.size),
                               fill="black", outline="black")
                font = ImageFont.truetype('retro_snake/fonts/pixelmix.ttf', 8)
                draw.multiline_text(
                    (2, 0), "Game\nover", fill="white", font=font, spacing=-1, align='center')

            while True:
                for offset in range(12):
                    virtual.set_position((offset, 0))
                    sleep(0.5)

        else:
            with canvas(virtual) as draw:
                draw.rectangle(((0, 0), draw.im.size),
                               fill="black", outline="black")
                draw.point(self.food, fill="white")
                draw.point(self.snake, fill="white")

    def update(self, f_stop=None):
        """Updates the game model."""
        if not f_stop.is_set() and not self.died:
            # call update again in x seconds
            threading.Timer(0.7, self.update, [f_stop]).start()

        head = add_tuples(self.snake[0], self.next_direccion)
        self.direccion = self.next_direccion

        if head[0] == self.width:
            head = (0, head[1])  # borde derecho
        elif head[1] == self.height:
            head = (head[0], 0)  # borde inferior
        elif head[0] == -1:
            head = (self.width - 1, head[1])  # borde izquierdo
        elif head[1] == -1:
            head = (head[0], self.height - 1)  # borde superior

        # snake advances
        self.snake.pop()
        self.snake.insert(0, head)

        if head[0] == self.food[0] and head[1] == self.food[1]:  # snake eats food
            self.snake.append(add_tuples(mult_tuple_by_scalar(
                self.snake[-1], 2), mult_tuple_by_scalar(self.snake[-2], -1)))
            self.generate_random_food()

        # Check if snake eats itself
        for point in self.snake[1:]:
            if head[0] == point[0] and head[1] == point[1]:
                self.died = True

        self.render()

    def move_right(self):
        """Sets next direction right."""
        if not self.direccion == self.LEFT:
            self.next_direccion = self.RIGHT

    def move_left(self):
        """Sets next direction left."""
        if not self.direccion == self.RIGHT:
            self.next_direccion = self.LEFT

    def move_up(self):
        """Sets next direction up."""
        if not self.direccion == self.DOWN:
            self.next_direccion = self.UP

    def move_down(self):
        """Sets next direction down."""
        if not self.direccion == self.UP:
            self.next_direccion = self.DOWN

    def generate_random_food(self):
        """Generates random food."""
        self.food = random_tuple(self.width, self.height)
        while(self.food in self.snake):
            self.food = random_tuple(self.width, self.height)


# Helper functions
def add_tuples(t1, t2):
    """Adds t1 and t2."""
    return (t1[0]+t2[0], t1[1]+t2[1])


def mult_tuple_by_scalar(tup, scalar):
    """Multiplies every value of tup by scalar."""
    return (tup[0]*scalar, tup[1]*scalar)


def random_tuple(t1_max, t2_max):
    """Return a random tuple between (0, 0) and (t1_max, t2_max)."""
    return (int(random.random()*t1_max), int(random.random()*t2_max))
