import math


def quadratic_equation(a, b, c):
    if a == 0:
        x = -c / b
        return "Уравнение не является квадратным, оно линейное, его корень равен: " + str(x)
    elif b == 0:
        if -c / a >= 0:
            d = - 4 * a * c
            if d < 0:
                return "Нет корней"
            elif d == 0:
                x = -b / (2 * a)
                return(x)
            else:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b + math.sqrt(d)) / (2 * a)
                return(x1, x2)
        else:
            return "Нет корней"
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
                return "Нет корней"
        elif d == 0:
                x = -b / (2 * a)
                return(x)
        else:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                return(x1, x2)
