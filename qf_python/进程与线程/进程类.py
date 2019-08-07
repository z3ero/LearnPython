from multiprocessing import Process
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        # 进程类功能函数
        print('%s is runing'%self.name)

if __name__=="__main__":
    my_process = MyProcess("sub_process")
    my_process.start()
    my_process.join()