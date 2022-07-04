list = input("Введите список чисел, разделенных пробелом: ").split()
for i in range(len(list)):
    list[i] = int(list[i])
max_number = max(list)
print("Наибольшее число:", max_number)
min_number = min(list)
print("Наименьшее число:", min_number)
list_new = []
for i in range (len(list)):
    if list[i] % 3 ==0 and list[i] % 5 !=0:
        list_new.append(list[i])
print(list_new)
