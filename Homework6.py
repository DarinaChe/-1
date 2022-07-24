import os
from os.path import exists

# Проверяем файл на наличие, на пустоту, на длину слова (если слова будут одинаковой длины, тоже будет ошибка)
# и на наличие символов и цифр в слове (с таким файлом тоже не работаем)

a = input("Введите путь к файлу: ")
file_exists = exists(a)
if file_exists == True:
    result = os.stat(a)
    if result.st_size == 0:
        print("Not found")
    else:
        f = open(a, encoding="utf8")
        All = f.read().split()
        i = 0
        if All[i].isdigit() or All[i].isalpha():
            def sortByLength(All):
                return len(All)


            newList = sorted(All, key=sortByLength)
            i += 1

            if len(newList[-1]) == len(newList[-2]):
                print("Not found")
            else:
                print(newList[-1])
                f.close()
        else:
            print("Not found")

else:
    print("Not found")