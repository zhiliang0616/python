import time
def prt():
    time.sleep(1)
    print("单线程")
start=time.time()
for i in range(5):
    prt()
end=time.time()
print("单线程耗时为:",end-start)



















from threading import Thread
start=time.time()
def prt():
    time.sleep(1)
    print("多线程")
list=[]
for i in range(5):
    t=Thread(target=prt)
    t.start()
    list.append(t)
for j in list:
    j.join()
end=time.time()
print("多线程耗时为:",end-start)