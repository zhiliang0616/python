'''
用函数来创建
打印裴波拉契算法（从第三项开始均为前两项的和）
'''
def fun(n):
    a,b=0,1
    yield a
    yield b
    count=0
    while count<n:
        a, b = b, a + b
        yield b
        count+=1
result=fun(10)
for i in result:
    print(i)