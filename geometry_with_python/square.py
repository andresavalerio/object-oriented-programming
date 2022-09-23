# Created by Andresa Valério
from invalid_square import InvalidSquareError

class Square():
    def __init__(self, il, ir, sl, sr):
        self.il = il
        self.ir = ir
        self.sl = sl
        self.sr = sr

        self.invalid_square()

    def invalid_square(self):
        left_side = self.il.distance(self.sl)
        right_side = self.ir.distance(self.sr)

        inferior_side = self.sl.distance(self.sr)
        superior_side = self.il.distance(self.ir)

        if not (left_side == right_side and inferior_side == superior_side and left_side == inferior_side):
            raise Exception

    def area(self):
        return self.il.distance(self.sl) ** 2