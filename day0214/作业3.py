def checkuser(fun):
    def check(*args):
        username=input("请输入用户名")
        if username == "zzy":
            print("已授权")
            fun(*args)

        else:
            print("未授权")
            check(*args)
    return check
@checkuser
def showlist(n):
    print("你的订单为第"+str(n)+"页")
showlist(10)