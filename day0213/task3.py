'''
生成器第二种写法，常见一种函数写法
通过函数 + yield
函数的内部有yield 函数返回的为生成器
yield 向生成器内部放入对象
如果要获取函数的原始返回值，需要通过next 访问所有对象（出错了，错误异常就是函数的原始返回值）
'''
def fun():
    yield 10
    yield 20
    yield 30
    return "helloWorld"
result=fun()
print(next(result))
print(next(result))
print(next(result))
try:
    print(next(result))
except StopIteration as e:
    print(e)