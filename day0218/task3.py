from multiprocessing import Pool
import os
import time
def run(**kw):
    time.sleep(1)
    print("进程为",os.getpid(),kw)
if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        pool.apply(func=run,kwds={"计数":i+1})
    pool.close()
    pool.join()