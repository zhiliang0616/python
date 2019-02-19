import os
def fun():
    result=os.fork()
    print(result)
    print(result," 返回当前的进程id",os.getpid(),"返回父进程的id",os.getppid())
fun()