list = input("Введите список чисел: ").split()
list1 = set(list)
print(list1)
uniq = []
for i in list1:
    if list.count(i) == 1:
        uniq.append(i)
print(uniq)
print(len(uniq))
