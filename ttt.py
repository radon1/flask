# def fun(b=None):
#     b = []
#     b.append(1)
#     print(b.__repr__)
#     #print(type(args))
#     #print(type(**))
#
# fun()
# fun()
# fun()
#
# a = 1
# b = a
# b += 1
# print(b.__repr__)
# print(a.__repr__)
# a = [1, 2, 3]
# print(a)
# a.pop(1)
# print(a)

d = {"Ivan": 29, "Mike": 27, "Elena": 31, "Bob": 31}
list_d = list(d.items())
list_d.sort(key=lambda i: (i[1], i[0]))
for i in list_d:
    print(i[0], ':', i[1])

# list_keys = list(d.keys())
# list_keys.sort()
# for i in list_keys:
#     print(i, ':', d[i])