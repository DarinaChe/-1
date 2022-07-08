from Geometricfigure.Circle import circle_p, circle_s
from Geometricfigure.Square import square_p, square_s
from Geometricfigure.Triangle import triangle_s, triangle_p

r = int(input("Введите радиус круга:"))
a = int(input("Введите сторону квадрата:"))
x = int(input("Введите сторону треугольника:"))
y = int(input("Введите сторону треугольника:"))
z = int(input("Введите сторону треугольника:"))


print(circle_p(r))
print(circle_s(r))

print(square_p(a))
print(square_s(a))

print(triangle_s(x, y, z))
print(triangle_p(x, y, z))
