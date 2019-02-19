from multiprocessing import Queue,ProcessError
q=Queue(5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
print(q.qsize())
print(q.empty())
print(q.full())
try:
    q.put(6,block=True,timeout=1)
except Exception as e:
    print(e)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
try:
    print(q.get(block=True, timeout=1))
except Exception as e:
    print(e)
