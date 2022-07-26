#
# a = input().split()
# for i, item in enumerate(a):
#     a[i] = int(item)
# maximum = max(a)
# minimum = min(a)
# for i in range(len(a)):
#     if a[i] == maximum:
#         a[i] = minimum
#     elif a[i] == minimum:
#         a[i] = maximum
# print(a)

list_1 = input()
list_2 = input()
if set(list_1).issubset(list_2):
    print ('True')
else:
    print('False')



