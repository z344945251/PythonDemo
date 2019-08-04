

def quotes():
    print(True or False)
    print('Using single quotes')
    print("useing double quotes")
    print("Mentioning the word 'Python' by quoting it")
    print("Embedding a \n line break with \\n")
    print("""Embbing a 
                line break with triple quotes""")


def strEqualTest():
    # string equal test
    print(not False)
    a = "123"
    b = "123"
    ar1 = [1,2,3]
    ar2 = [1,2,3]
    print("123" is "123")
    print("123" == "123")
    print(a == b)
    print(a is b)
    print(ar1 == ar2)
    print(ar1 is ar2)
    print(id(a))
    print(id(b))
    print(id(ar1))
    print(id(ar2))


def string_index():
    print("greater"[-1])


def str_cut():
    # 字符串 切片运算符测试
    print("greater"[:])
    print("greater"[1:])
    print("greater"[-1:])
    print("greater"[:1])
    print("greater"[:-1])
    print("greater"[1:3])


def str_formate():
    # 字符串格式化输出 测试
    # 字段宽度： 字符+空格的长度
    for exponent in range(7,11):
        print(exponent, 10 ** exponent)

    # 正右对齐  负 左对齐
    for exponent in range(7, 11):
        print("%-3d" % exponent, "%11d" % 10 ** exponent)

    # 对元组 进行格式化
    for exponent in range(7, 11):
        print("%-3d% 11d" % (exponent, 10 ** exponent))

    # 对浮点数进行格式化 %<filed.width>.<precision>f
    salary = 100.00
    print("your salary is $"+str(salary))
    print("your salary is $%0.2f" % salary)

    # 6的字段宽度 包含了小数点所占的位置
    print("%6.3f" % 3.14)


def str_method():
    # 获取字符串长度
    print("123".__len__())
    print(len("123"))

    # 在后面拼接
    print("123".__add__("456"))

    # 判断是否包含
    print("greater".__contains__("g"))
    print("g" in "greater")


def str_dir():
    # 获取 字符串方法列表
    print(dir(str))
    help(str.upper)
    help(str.__len__)


if __name__ == "__main__":
    str_dir()