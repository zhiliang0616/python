def checkuser(fun):
    def check():
        username=input("请输入用户名")
        if username=="wzk":
            print("已授权")
            fun()
        else:
            print("未授权")
    return check



@checkuser
def showlist():
    print("获取商品列表")
@checkuser
def showmoney():
    print("余额为10000￥")



showlist()
showmoney()