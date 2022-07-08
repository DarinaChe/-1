from math import pi

import pytest
from Geometricfigure.Circle import circle_p, circle_s


def test_circle_p():
    assert circle_p(5) == 10 * pi


def test_circle_p1():
    assert circle_p(0) == "Нет такой фигуры"


def test_circle_s():
    assert circle_s(5) == 78.5


def test_circle_s():
    with pytest.raises(Exception):
        circle_s(0)
