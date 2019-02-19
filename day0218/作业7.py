import os
import time
from  multiprocessing import Pool
def fun(**kw):
    time.sleep(1)
    print("当前进程",os.getpid(),"循环次数为",kw)

def main():
    pool = Pool(5)
    for i in range(20):
        pool.apply_async(fun, kwds={"计数": i+1})
    pool.close()
    pool.join()
if __name__ == '__main__':
    main()
