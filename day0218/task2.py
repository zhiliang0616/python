from multiprocessing import Process
class ProcessPro(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        super().__init__(group, target, name, args, kwargs)

    def run(self):
        print("进程启动了")
def main():
    p1=ProcessPro(name="p1")
    p1.start()
if __name__ == '__main__':

