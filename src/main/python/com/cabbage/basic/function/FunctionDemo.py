

# 必填参数
def function1(str1):
    print("you input str is : ",str1)


# 可选参数
def function2(str2="str2"):
    print("you input str is : ",str2)


# 可选参数 必须在必填参数后面
def function3(str1, str2="str2"):
    print("you input str is : ",str1, str2)


# 嵌套函数定义：可以在一个函数中嵌套定义另一个函数
# first definition
def factorial(n):
    """Returns the factorial of n."""
    def recurse(n,product):
        if n == 1:return product
        else: return recurse(n-1, n*product)


# Second definition
def factorial2(n,product=1):
    """Returns the factorial of n."""
    if n == 1: return product
    else: return factorial2(n-1, n*product)


"""高阶函数"""


def is_positive(n):
    return n>0


def in_build_high_factorial():
    old_list = [0, 1, 2, 3, 4, 5]
    str_list = list(map(str, old_list))
    print(str_list)

    positive = filter(is_positive, old_list)
    print(list(positive))

    # reduce
    import functools
    print(functools.reduce(lambda a,b: a*b, range(1, 10)))


# 使用lambda 定义匿名函数
def lambda_anonymous():
    old_list = [0, 1, 2, 3, 4, 5]
    positive = filter(lambda n: n > 0, old_list)
    print(list(positive))


if __name__ == "__main__":
    in_build_high_factorial()