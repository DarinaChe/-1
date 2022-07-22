a = input('Введите фразу:')
a = a.lower()
b = a.replace(" ","")
res = []
for i in range(len(b) - 1, -1, -1):
    res.append(b[i])
print(res)
n = b[::-1]
if b == n:
    print("полиндром")
else:
    print(" не полиндром")

