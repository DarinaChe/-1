a = int(input('Введите номер месяца от 1 до 12:'))
while a == 0 or a > 12:
    a = int(input('Введите номер месяца от 1 до 12:'))
if a == 1 or a == 3 or a ==5 or a == 7 or a == 8 or a == 10 or a == 12:
    print( 31 )
elif a == 4 or a == 6 or a == 9 or a == 11:
    print( 30 )
else:
    print('ФЕВРАЛЬ')
