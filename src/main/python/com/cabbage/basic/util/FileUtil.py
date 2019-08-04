DESKTOP_PATH = "C:\\Users\\Administrator\\Desktop"


# 文本文件所有的数据输入或输出都必须是字符串
def read_from_number_file():
    number_file_path = DESKTOP_PATH+"\\number.txt"
    f = open(number_file_path, "r")     # "r"：只读模式  "w"写模式

    # 一次 读取所有的数据
    print(f.read())

    # 读取一行
    f = open(number_file_path, "r")
    print(f.readline())

    # 循环读取
    f = open(number_file_path, "r")
    for line in f:
        print(line)
    f.close()


# 向文件中写入
def write_to_file():
    file_path = DESKTOP_PATH+"\\my_file.txt"
    f = open(file_path, 'w')
    f.write("First line.\nSecond line.\n")
    f.close()


# 将数字写入到文件
def write_and_read_number_with_file():
    import random
    f = open(DESKTOP_PATH+"\\number_write.txt", 'w')
    for count in range(500):
        number = random.randint(1, 500)
        f.write(str(number)+"\n")
    f.close()

    f = open(DESKTOP_PATH+"\\number_write.txt", 'r')
    sum = 0
    for line in f:
        sum += int(line.strip())
    f.close()
    print(sum)


# 使用pickle 读写对象
def pickle_with_object():
    import pickle
    lyst = [60, "A string object", 1997]
    file_obj = open(DESKTOP_PATH+"\\items.dat", 'wb')
    pickle.dump(lyst, file_obj)
    file_obj.close()

    file_obj = open(DESKTOP_PATH+"\\items.dat", 'rb')
    read_l = pickle.load(file_obj)
    print(read_l)


if __name__ == "__main__":
    pickle_with_object()