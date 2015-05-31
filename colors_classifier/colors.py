# encoding: utf-8
from colormath.color_objects import sRGBColor


class Color(sRGBColor):

    def __eq__(self, other):
        return self.values() == other.values()

    @staticmethod
    def from_hex(hex_str):
        return Color(*sRGBColor.new_from_rgb_hex(hex_str).get_value_tuple())

    def values(self):
        return self.get_upscaled_value_tuple()