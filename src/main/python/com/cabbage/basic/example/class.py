class Counter:

    """Models a counter"""

    # class variable
    instances = 0
    # 定义私有属性
    __weight = 100

    # 构造方法 创建实例的时候 默认调用该方法, 构造方法可以指定参数 self 不是python关键字 换成别的变量也可以运行
    def __init__(self, _value=0):
        # Set up the counter to 0
        print("counter  构造方法被调用")
        Counter.instances += 1
        self._value = _value

    # Mutator method
    def reset(self):
        self._value = 0
        print(self.__weight)

    def increment(self, amount=1):
        self._value += amount

    def decrement(self, amount = 1):
        self._value -= amount

    def get_value(self):
        return self._value

    # 重写 toString  方法
    def __str__(self):
        return str(self._value)

    # 重写 eq 方法
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other): return False
        return self._value == other._value


# 继承  除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用 class DerivedClassName(modname.BaseClassName):
class MultiplyCounter(Counter):

    def multiply(self, num=2):
        self._value *= num


def counter_test():
    c1 = Counter()
    print(c1)
    print(c1.get_value())
    print(c1.__str__())
    c1.increment()
    print(c1)
    c1.increment(5)
    print(c1)
    c1.reset()
    print(c1)
    c2 = Counter()
    print(Counter.instances)
    print(c1 == c2)
    c1 = 0
    print(c1 == c2)


    multiply = MultiplyCounter(10)
    print(multiply)
    multiply.multiply()
    print(multiply)


if __name__ == "__main__":
    counter_test()

