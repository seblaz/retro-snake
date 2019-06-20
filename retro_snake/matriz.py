#from luma.led_matrix.device import max7219
#from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.error import DeviceNotFoundError
from luma.emulator.device import pygame


def get_canvas(width, height):
    """
    Devuelve un canvas para dibujar. En caso de que la matriz esté
    conectada devuelve un canvas de la misma, en caso contrario
    devuelve un canvas de simulación de pygame.
    """
    #try:
        #serial = spi(port=0, device=0, gpio=noop())
        #device = max7219(serial, width=width, height=height)
    #except DeviceNotFoundError:
    device = pygame(width=width, height=height, mode="1", transform='led_matrix')
    return canvas(device)
