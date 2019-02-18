# 一般意义的复制
# a=[1,2,[4,5]]
# b=a
# a.append(6)
# print(id(a[2]))
# b.append(7)
# print(id(b[2]))
# print(a)
# print(b)
# 浅拷贝
import copy
# a=[1,2,[4,5]]
# b=copy.copy(a)
# print(id(a))
# print(id(b))
# print(id(a[2]))
# print(id(b[2]))
# 深拷贝
a=[1,2,[4,5]]
b=copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(a[2]))
print(id(b[2]))