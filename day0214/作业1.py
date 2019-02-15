def fun():
    def fun1():
        return "hello"
    return fun1
f=fun()
print(f())