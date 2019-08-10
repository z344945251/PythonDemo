"""
    hanoi 问题递归实现
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def pop(self):
        return self.items.pop()


def hanoi(n,stack_x, stack_y, stack_z):           # 以 y 为辅助 移动 x 中的元素 到 z
    if n == 1:
        move(stack_x, stack_z)
    else:
        hanoi(n-1, stack_x, stack_z, stack_y)      # 移动n之前需要先移动n-1
        move(stack_x, stack_z)                     # 移动最上层的元素 到 z
        hanoi(n-1, stack_y, stack_x, stack_z)      # 以x为辅助  移动 y 中的元素到到 z （将y空出 以便进行下一次hanoi操作）
    print("x:", stack_x, "y:", stack_y, "z", stack_z)


def move(stack_x, stack_z):
    stack_z.append(stack_x.pop())  # 将x中的第一位元素 移动到 z


def hanoiTest():
    x = [3, 2, 1]
    y = []
    z = []
    hanoi(3,x,y,z)


"""
hanoi 问题非递归（栈） 实现
"""


class StackFrame:
    def __init__(self, rd, f_n, f_sx, f_sy, f_sz):
        self.rd = rd
        self.f_n = f_n
        self.f_sx = f_sx
        self.f_sy = f_sy
        self.f_sz = f_sz


def movex2z(stack):
    pop = stack.pop()
    pop.f_sz.append(pop.f_sx.pop())  # 将x中的第一位元素 移动到 z
    stack.push(pop)

def movex2y(stack):
    pop = stack.pop()
    pop.f_sy.append(pop.f_sx.pop())  # 将x中的第一位元素 移动到 z
    stack.push(pop)


def hanoiVectorProcedure(n, stack_x, stack_y, stack_z):
    s = Stack()     # 初始化栈
    s.push(StackFrame(3, n, stack_x, stack_y, stack_z))  # 当前参数入栈
    while not s.isEmpty():
        while s.peek().f_n > 1:
            s.push(StackFrame(1, s.peek().f_n-1, stack_x, stack_y, stack_z))
        movex2y(s)
        rd = s.peek().rd
        print(rd)

        if rd == 1:
            movex2z(s)
            s.push(StackFrame(2, s.peek().f_n, stack_y, stack_x, stack_z))
            s.pop()
        if rd == 2:
            s.pop()
            
        if rd == 3:
            s.pop()

        print("x:", stack_x, "y:", stack_y, "z", stack_z)

x = [3, 2, 1]
y = []
z = []
hanoiVectorProcedure(3,x,y,z)


def hanoiVectorProcedure1(n, stack_x, stack_y, stack_z):
    s = Stack()     # 初始化栈
    s.push(StackFrame(3, n, stack_x, stack_y, stack_z))  # 当前参数入栈
    while not s.isEmpty():
        if s.peek().f_n == 1:
            move(s.peek().stack_x, s.peek().stack_y)
            # GOTO s.peek().rd
            s.pop()
        else:
            s.push(StackFrame(1, s.peek().f_n-1, s.peek().f_sx, s.peek().f_sy, s.peek().f_sz))
            # GOTO 0

            # rd = 1 start
            sf1 = s.pop()   # 没有额外的操作 直接退栈
            move(s.peek().stack_x,s.peek().stack_z)

            # 第二次递归
            s.push(StackFrame(2, s.peek().f_n, s.peek().f_sy, s.peek().f_sx, s.peek().f_sz))
            # GOTO 0

            # rd = 2 start nothing to do

            # rd = 3 done
            s.pop()





































