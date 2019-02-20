from multiprocessing import Manager,Pool
def read(q):
    pass
def write(q):
    pass
if __name__ == '__main__':
    q = Manager().Queue(5)
    q.put(-2)
    q.put(-1)
    pool=Pool(5)
    pool.apply_async(write,(q,))
    pool.apply_async(write,(q,))
    pool.close()
    pool.join()
# from multiprocessing import Pool
# from multiprocessing import Manager
# import time
# def read(q):
#     while True:
#         print("pqueue size %d" % q.qsize())
#         r = q.get()
#         print("get %d" % r)
#         print("pqueue size %d" % q.qsize())
#     time.sleep(0.1)
# def write(q):
#     for r in range(5):
#         q.put(r)
#         print("put %d " % r)
#         print("queue size %d" % q.qsize())
#     time.sleep(2)
# if __name__ == '__main__':
#     q = Manager().Queue(5)
#     q.put(-2)
#     q.put(-1)
#     pool = Pool(5)
#     pool.apply_async(write, (q,))
#     pool.apply_async(read, (q,))
#     pool.close()
#     pool.join()
#     print("finish")
