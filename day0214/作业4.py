import time
def checkuser(fun):
    def check():
        time_start=time.time()
        fun()
        time_stop=time.time()
        print(time_stop - time_start)
    return check
@checkuser
def showlist():
    for i in range(1000000):
        print("获取商品列表")
showlist()