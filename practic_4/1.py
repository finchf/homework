https://www.codewars.com/kata/53f1015fa9fe02cbda00111a/train/python

import random

class Ghost:
    def __init__(self):
        self.color = self.get_random_color()

    def get_random_color(self):
        colors = ["white", "yellow", "purple", "red"]
        return random.choice(colors)