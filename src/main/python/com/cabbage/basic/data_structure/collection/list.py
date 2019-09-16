
def list_method():

    tl1 = []
    tl2 = tl1
    tl1.append(34)
    print(tl1,tl2)
    tl1.insert(1, 55)
    print(tl1,tl2)


def dir_list():
    print(dir(list))


def for_each_list():
    lt = [1, 2, 3, 4, 5, 6]
    for i in lt:
        print(i)

    for i in range(len(lt)):
        print(lt[i])


if __name__ == "__main__":
    for_each_list()