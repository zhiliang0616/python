import threading
from threading import Lock
num = 0
lock =Lock()
def fun1():
    for r in range(1000000):
        global num
        lock.acquire()
        num += 1
        lock.release()

t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun1)
t1.start()
t2.start()

t1.join()
t2.join()
print(num)
