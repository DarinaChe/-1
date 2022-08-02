from ProjectLU.Copy_surname import dispatch_surname


def test_dispatch_surname():
    assert dispatch_surname(5, 6, 3) == 14

def test_dispatch_surname2():
    assert triangle_p(5, 0, 6) == "Нет такой фигуры"

def test_triangle_s1():
    assert triangle_s(5, 6, 3) == 7.483314773547883

def test_triangle_s2():
    assert triangle_s(5, 0, 3) == "Нет такой фигуры"