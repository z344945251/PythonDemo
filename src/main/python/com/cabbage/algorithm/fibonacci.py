"""
fibonacci  递归以及非递归写法
"""


def fibonacci_recursive(n):
    # 递归写法
    if n < 3:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)


def fibonacci_linear(n):
    # 线性循环写法
    first = 1
    second = 1
    for i in range(2, n):
        s = second
        second = first + second
        first = s
    return second


if __name__ == "__main__":
    import array
    list
    print(fibonacci_linear(10))