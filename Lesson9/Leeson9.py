# Task 1
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

# Task 2
# list_1 = input()
# list_2 = input()
# set(list_1).issubset(list_2)

# Task 3
# def all_subsets(data):
#     subsets = [[]]
#     for i in range(len(data)):
#         for j in range(len(subsets)):
#             new_subset = subsets[j] + [data[i]]
#             subsets = subsets + [new_subset]
#     return subsets
#
# print(all_subsets([1, 2 ,3]))
# print(set([1, 2, 3]).issubset(set([1, 3])))

# itertools - для работы с множествами и подмножествами


a = [0, 2, 3, 4]
x = [3, 5, 7, 9]

dict1 = dict(zip(a, x))
print(dict1)
