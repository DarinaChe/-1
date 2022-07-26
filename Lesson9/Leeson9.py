
a = input().split()
for i, item in enumerate(a):
    a[i] = int(item)
maximum = max(a)
minimum = min(a)
for i in range(len(a)):
    if a[i] == maximum:
        a[i] = minimum
    elif a[i] == minimum:
        a[i] = maximum
print(a)


