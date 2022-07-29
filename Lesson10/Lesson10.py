# a = int(input())
# b = int(input())
#
# if b != 0:
#     print(a / b)
# else:
#     raise Exception ('На ноль делить нельзя')

# height = float(input('Enter your height(metres): '))
# weight = float(input('Enter your weight(metres): '))
#
# try:
#     d = [1, 2]
#     print(d[3])
#     print(height / weight)
# except ZeroDivisionError:
#     print('Нельзя делить на 0')
# # except IndexError:
# #     print('Нет такого элемента')
# except Exception as e:
#     print("Ошибка")
#     print(e)
#     print("Ничего не получилось")
#     raise e

# try:
#     with open('test.txt') as f:
#         print(f.readline())
# except FileNotFoundError:
#     print('Не могу найти файл')
# else:
#     print('Все ok')

# try:
#     f = open('test.txt')
# except FileNotFoundError:
#     print('Не могу найти файл')
# else:
#      print(f.readline())
# finally:
#     f.close()
#     print('Все закончилось')

try:
    a = input("Введите имя файла: ")
    f1 = open(a)
except FileNotFoundError:
    print('Не могу найти файл')
else:
    lines = f1.readlines()
    for line in lines:
        c = '#'
        if c in line:
            line.find(c)
            print(line.find(c))
            b = line[0:line.find(c)]
            print(b)
        else:
            print(line)
finally:
     f1.close()
     print('Все закончилось')


# Lesson10test.py






