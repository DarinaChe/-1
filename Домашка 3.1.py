# Написать функцию, принимающую три агрумента - день, месяц и год Вывести "OK" если дата корректна, "FAILED" если дата не корректа
# дополнительно - можно вывести тот компонент, в котором ошибка, например для даты 32.01.1999 вывести "Incorrect day"

def datamounthyear(a, b, c):
    if c > 0 and c % 4 == 0: # считаю, что отрицательных и года с номером 0 не бывает
        if c % 100 == 0 and c % 400 != 0:
            if b == 1 or b== 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
                if 0 < a < 32:
                    print('ОК')
                else:
                    print('FAILED')
                    print('Incorrect day')
            elif b == 4 or b == 6 or b == 9 or b == 11:
                if 0 < a < 31:
                    print('ОК')
                else:
                    print('FAILED')
                    print('Incorrect day')
            elif b == 2:
                if 0 < a < 29:
                    print('ОК')
                else:
                    print('FAILED')
                    print('Incorrect day')
            else:
                print('FAILED')
                print('Incorrect mounth')
        else:
            if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
                if 0 < a < 32:
                    print('ОК')
                else:
                    print('FAILED')
                    print('Incorrect day')
            elif b == 4 or b == 6 or b == 9 or b == 11:
                if 0 < a < 31:
                    print('ОК')
                else:
                    print('FAILED')
                    print('Incorrect day')
            elif b == 2:
                if 0 < a < 30:
                    print('ОК')
                else:
                    print('FAILED')
                    print('Incorrect day')
            else:
                print('FAILED')
                print('Incorrect mounth')

    elif c <= 0:
        print('FAILED')
        print('Incorrect year')
    else:
        if b == 1 or b== 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
            if 0 < a < 32:
                print('ОК')
            else:
                print('FAILED')
                print('Incorrect day')
        elif b == 4 or b == 6 or b == 9 or b == 11:
            if 0 < a < 31:
                print('ОК')
            else:
                print('FAILED')
                print('Incorrect day')
        elif b == 2:
            if 0 < a < 29:
                print('ОК')
            else:
                print('FAILED')
                print('Incorrect day')
        else:
            print('FAILED')
            print('Incorrect mounth')


l = input('Введите дату: ').replace('.', ' ')
l1 = [int(i) for i in l.split()]
a = l1[0]
b = l1[1]
c = l1[2]
print(datamounthyear(a, b, c))

