'''
开闭原则：面向修改关闭，面向扩展开放
装饰器（满足开闭原则的设计）
有@符号+语法糖构成
比@classmethod
'''
def checkuser(fun):
    def check(n):
        username=input("请输入用户名")
        if username == "zzy":
            print("有权限执行方法")
            fun(n)

        else:
            print("未授权")
            check(n)
    return check
@checkuser
def showlist(n):
    print("你的订单第"+str(n)+"页")
showlist(10)