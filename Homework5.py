a = input('Введите команду: ').split()
l = []
num = 1
while a[0] != 'exit':
    if a[0] == 'add':
        l.append({"Number": num, "Name" : (a[1] + " " + a[2]), "Mark": []})
        num += 1
        print("Ок")
    elif a[0] == 'all':
        for i in l:
            print(f"{i['Number']}{'.'} {i['Name']} {' '.join(i['Mark'])}")
    elif a[0] == 'mark':
        for i in l:
            if i['Number'] == int(a[2]):
                i['Mark'].append(a[1])
                print("Ок")
    elif a[0] == 'delete':
        for i in range(len(l) - 1, -1, -1):
            if l[i]['Number'] == int(a[1]):
                l.pop(i)
                num = 1
                for i in l:
                    i['Number'] = num
                    num += 1
    elif a[0] == 'edit':
        for i in l:
            if i['Number'] == int(a[1]):
                i['Name'] = (a[2] + ' ' + a[3])
    elif a[0] == 'average':
        for i in l:
            Len = len(i['Mark'])
            inter = [int(x) for x in i['Mark']]
            Sum = sum(inter)
            Avg = Sum / Len
            print(f"{i['Number']}{'.'} {i['Name']} {' '.join(i['Mark'])} {'Average'} {Avg} ")


    a = input('Введите команду: ').split()


