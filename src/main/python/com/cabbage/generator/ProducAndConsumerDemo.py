
def consumer(name):
    print(name+":开始消费数据")

    while True:
        data = yield
        print(name+":开始消费数据:"+str(data))


c = consumer("cabbage")

c.__next__()
c.send("aaa")