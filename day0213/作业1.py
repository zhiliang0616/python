def fun():
    yield 10
    yield 20
    return "hello"
result=fun()
print(next(result))
print(next(result))
try:
    print(next(result))
except StopIteration as e:
    print(e)



# Iterable判断是否可以迭代
from collections.abc import Iterable
#Iterator 判断是否是迭代器
from collections.abc import Iterator
l=[1,2,3,4,5,6,7,8]
t=(1,2,3,4,5,6,8,1,)
d={"name":"zzy","addr":"zhengzhou"}
s="abcdefg"
i=100
#判断是否可迭代
print(isinstance(l,Iterable))
print(isinstance(t,Iterable))
print(isinstance(d,Iterable))
print(isinstance(s,Iterable))
print(isinstance(i,Iterable))
#判断是否是迭代器
print(isinstance(l,Iterator))
print(isinstance(t,Iterator))
print(isinstance(d,Iterator))
print(isinstance(s,Iterator))
print(isinstance(i,Iterator))
