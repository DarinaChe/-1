from Geometricfigure.Triangle import triangle_p, triangle_s


def test_triangle_p():
    assert triangle_p(5, 6, 3) == 14


def test_triangle_p1():
    assert triangle_p(5, 0, 6) == "Нет такой фигуры"

def test_triangle_s1():
    assert triangle_s(5, 6, 3) == 7.483314773547883

def test_triangle_s2():
    assert triangle_s(5, 0, 3) == "Нет такой фигуры"