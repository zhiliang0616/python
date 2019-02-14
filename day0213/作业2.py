#编码验证迭代器与可迭代的区别
from collections.abc import Iterator,Iterable

a=(x for x in range(10))
print(next(a),next(a),next(a),next(a))
for i in a:
    print(next(a))
#判断是否可迭代
print(isinstance(a,Iterable))
#判断是否是迭代器
print(isinstance(a,Iterator))
listA=[1,2,3,4,5,6,7,8,9]
#判断是否可以迭代
print(isinstance(listA,Iterable))
for i in listA:
    print(i)
#判断是否是迭代器
print(isinstance(listA,Iterator))
if isinstance(listA,Iterator)==True:
    print(next(listA))
#迭代器可以使用 for循环 并且可以用next回调
#可迭代可以使用for循环但不可以使用next回调