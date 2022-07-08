
def triangle_p(x, y, z):
    if x <= 0 or y <= 0 or z <= 0 or (x + y) < z or (x +z ) < y or (z +y) < x:
        return "Нет такой фигуры"
    else:
        return x + y + z

import math
def triangle_s(x, y, z):
    if x <= 0 or y <= 0 or z <= 0 or (x + y) < z or (x +z ) < y or (z +y) < x:
        return "Нет такой фигуры"
    else:
        p = (x + y + z)/2
        s = math.sqrt(p*(p-x)*(p-y)*(p-z))
        return s
