list = input("Введите список чисел: ").split()
for i in range(len(list)):
    list[i] = int(list[i])
for i in range(len(list)):
    if list.count(list[i]) == 1:
        print(list[i])







