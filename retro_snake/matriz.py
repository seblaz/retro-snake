from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
# from luma.core.virtual import viewport
# from luma.core.legacy import text, show_message


def get_canvas():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    return canvas(device)