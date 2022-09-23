from math import hypot

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return hypot(self.x - other.x, self.y - other.y)