from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont, ImageDraw


class OLED_helpers:
    """Helper object for OLED functions"""
    # TODO
    # draw title
    # notification bar virtual area
    # notification icons

    def __init__(self):
        self.serial = i2c(port=1, address=0x3C)
        self.device = ssd1306(self.serial, rotate=0)

    def get_device(self):
        """Return OLED device object"""
        return self.device

    def draw_text(self, x, y, text):
        """Draw one line of standard text"""
        with canvas(self.device) as draw:
            draw.text((x, y), text, fill="white")

    def draw_lines(self, lines):
        """Draw several lines of standard text"""
        with canvas(self.device) as draw:
            y = 0
            for line in lines:
                draw.text((0, y), line, fill="white")
                y += 13