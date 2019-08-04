

import time


def timmer(func):
    def warpper(*args,**kwargs):
        start=time.time()
        func()
        end = time.time()
        print("the func run time is %s"%(end-start))
    return warpper;



@timmer
def test1():
    time.sleep(3)
    print("in the test1")


test1()

a = [i*2 for i in range(9)]
print(a)

