#from luma.led_matrix.device import max7219
#from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.error import DeviceNotFoundError
from luma.emulator.device import pygame


def get_device(width, height):
    """
    Devuelve un dispositivo. En caso de que la matriz esté conectada
    devuelve la misma, en caso contrario devuelve un dispositivo de
    simulación de pygame.
    """
    # try:
    #     serial = spi(port=0, device=0, gpio=noop())
    #     device = max7219(serial, width=width, height=height)
    # except DeviceNotFoundError:
    device = pygame(width=width, height=height,
                    mode="1", transform='led_matrix')
    return device
