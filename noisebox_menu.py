# Based on https://gist.github.com/codelectron/d493d4aaa6fc858ce69f2b335afd0b00#file-oled_rot_menu_rpi-py

from luma.core.render import canvas
from PIL import ImageFont
import oled_layout


class Menu:
    """Object for drawing OLED menu and managing input with rotary"""

    def __init__(self, names, oled_helpers, noisebox):
        # persist values
        self.counter = 1
        self.menuindex = 0
        self.names = names
        self.noisebox = noisebox
        self.oled_helpers = oled_helpers
        self.device = oled_helpers.get_device()

    def invert(self, draw, x, y, text):
        """invert selected menue item"""
        font = ImageFont.load_default()
        draw.rectangle((x, y, x+120, y+12), outline=255, fill=255)
        draw.text((x, y), text, font=font, outline=0, fill="black")

    def menu(self, device, draw, menustr, index):
        """return prepared menu"""
        font = ImageFont.load_default()
        draw.rectangle(self.device.bounding_box, outline="white", fill="black")
        for i in range(len(menustr)):
            if(i == index):
                self.menuindex = i
                self.invert(draw, 2, i*10, menustr[i])
            else:
                draw.text((2, i*10), menustr[i], font=font, fill=255)

    def draw_menu(self):
        """draw menu on convas"""
        with canvas(self.device) as draw:
            self.menu(self.device, draw, self.names, self.counter % 5)

    def menu_operation(self, strval):
        """check menu value when button clicked and run corresponding function"""
        if (strval == "ROOM 1"):
            self.noisebox.start_session()

        if (strval == "LEVEL METER"):

            self.noisebox.start_meters()

        if (strval == "TEST AUDIO"):
            layout = oled_layout.Layout()
            layout.render(self.oled_helpers.get_device())

        if (strval == "P2P"):
            self.noisebox.check_peers()

        if (strval == "IPAddress"):
            self.oled_helpers.draw_text(0, 26, self.noisebox.get_ip())
