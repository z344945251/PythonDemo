"""
归并排序
"""


# 递归分解
def merge_sort(data, left, right):
    middle = (left+right)//2
    l1 = left
    r1 = middle
    if r1>l1:
        merge_sort(data, l1, r1)
    l2 = middle+1
    r2 = right
    if r2>l2:
        merge_sort(data, l2, r2)

    print(l1, r1, l2, r2)
    merge_sorted_list(data, l1, r1, l2, r2)


# 递归排序
def merge_sorted_list(data, l1, r1, l2, r2):
    print(data)
    d1 = data[l1:r1+1]
    d2 = data[l2:r2+1]
    i1 = 0
    i2 = 0
    for i in range(l1, r2+1):
        if i1 == d1.__len__():
            data[i] = d2[i2]
            i2 += 1
            continue

        if i2 == d2.__len__():
            data[i] = d1[i1]
            i1 += 1
            continue

        if d1[i1] <= d2[i2]:
            data[i] = d1[i1]
            i1 += 1
        else:
            data[i] = d2[i2]
            i2 += 1


if __name__ == "__main__":
    data = [9, 2, 4, 3, 8, 5]
    merge_sort(data, 0, data.__len__()-1)
    print(data)