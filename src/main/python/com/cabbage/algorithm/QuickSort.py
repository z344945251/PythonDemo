"""
快速排序
"""


def quick_sort(data, left, right):
    print(data, left, right)
    if right - left == 0:
        return
    if right - left == 1:
        compare_and_change(data, left, right)
        return

    # 选取一个基准点（中间值）
    middle = (right + left) // 2
    pivot = data[middle]
    # 变量整个列表 小于基准点的放在左边 大于基准点的在右边
    change(data, middle, right)
    index = left
    for i in range(left, right):
        if data[i] <= pivot:
            change(data, i, index)
            index += 1
    change(data, right, index)

    # 递归对字列表进行快速排序
    r1 = index - 1
    l1 = index + 1
    if r1 > left:
        quick_sort(data, left, r1)
    if right > index:
        quick_sort(data, l1, right)


def change(data, index1, index2):
    # 交换两个下标的数据
    tmp = data[index1]
    data[index1] = data[index2]
    data[index2] = tmp


def compare_and_change(data, index1, index2):
    if data[index1] > data[index2]:
        change(data, index1, index2)


if __name__ == "__main__":
    d = [23, 545, 3523, 312, 45, 6, 5, 44, 3, 23, 44, 75, 22, 123, 44]
    print(d.__len__())
    quick_sort(d, 0, d.__len__()-1)
    print(d)
