import pytest
from invalid_square import InvalidSquareError

from point import Point
from square import Square

def test_distance():
    point1 = Point(0, 0)
    point2 = Point(2, 0) 

    assert point1.distance(point2) == 2

def test_area():
    il = Point(0, 0)
    ir = Point(2, 0)
    sl = Point(0, 2)
    sr = Point(2, 2)

    square = Square(il, ir, sl, sr)

    assert square.area() == 4

def test_invalid_square():
    il = Point(0, 0)
    sl = Point(0, 2)
    ir = Point(4, 0)
    sr = Point(4, 4)

    with pytest.raises(InvalidSquareError):
       Square(il, ir, sl, sr)
 