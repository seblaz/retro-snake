from retro_snake.matriz import get_canvas
import time

canvas = get_canvas()

with canvas as draw:
    draw.point((0,0), fill="white")
time.sleep(10)
