from Homework4.func import quadratic_equation


def test_quadratic_equation():
    assert quadratic_equation(1, -2, 1) == 1

def test_quadratic_equation1():
    assert quadratic_equation(1, 3, -4) == (1.0, -4.0)

def test_quadratic_equation2():
    assert quadratic_equation(1, 2, 4) == "Нет корней"


def test_quadratic_equation3():
    assert quadratic_equation(0, 3, 9) == "Уравнение не является квадратным, оно линейное, его корень равен: -3.0"


def test_quadratic_equation4():
    assert quadratic_equation(9, 0, 3) == "Нет корней"

def test_quadratic_equation5():
    assert quadratic_equation(9, 0, 0) == 0
