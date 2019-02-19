from multiprocessing import Process,Queue
import time
def read(q):
    while True:
        print(q.get())
        time.sleep(1)
def write(q):
    i = -1
    while True:
        i+=1
        q.put(i)
    time.sleep(1)
if __name__ == '__main__':
    q = Queue(2)
    q.put(-2)
    q.put(-1)
    pr=Process(target=read,args=(q,))
    pw=Process(target=write,args=(q,))
    pr.start()
    pw.start()
    pr.join()
    pw.join()
