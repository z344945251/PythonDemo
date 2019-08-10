

class SortDemo:
    arr = [23, 545, 3523, 312, 45,6, 5, 1, 3, 23, 44, 75, 22, 123, 44]
    #arr = [1, 3, 5, 6, 22, 23, 23, 44, 44, 45, 75, 123, 312, 545, 3523]
    #arr = [3523, 545, 312, 123, 75, 45, 44, 44, 23, 23, 22, 6, 5, 3, 1]


    """希尔排序"""
    def shell1(self,sortArr):
        print("shell")
        count=0
        #先选取一个增量  当前数组长度的 1/2 缩小增量=增量/2 重复上面的步骤 直到增量=1
        # for i in range(1,sortArr.__len__,2):
        #     print(i)
        gap=sortArr.__len__()//2
        while(gap>=1):
            for i in range(gap,sortArr.__len__()):
                for j in range(i,gap-1,-gap):
                    count+=1
                    rdata = sortArr[j]
                    lData = sortArr[j-gap]
                    if(rdata<lData):
                        sortArr[j]=lData
                        sortArr[j-gap]=rdata
                    else:
                        break

            gap=gap//2
        print(sortArr)
        print(sortArr.__len__(),count)

    """希尔排序"""
    def shell(self,sortArr):
        print("shell")
        count=0
        #先选取一个增量  当前数组长度的 1/2 缩小增量=增量/2 重复上面的步骤 直到增量=1
        # for i in range(1,sortArr.__len__,2):
        #     print(i)

        gap=sortArr.__len__()//2
        while(gap>=1):
            for i in range(0,gap):
                #遍历数组对各自的增量数组进行 插入排序
                for j in range(i+gap,sortArr.__len__(),gap):
                    for k in range(j,i,-gap):
                        count+=1
                        rdata = sortArr[k]
                        lData = sortArr[k-gap]
                        if(rdata<lData):
                            sortArr[k]=lData
                            sortArr[k-gap]=rdata
                        else:
                            break
            gap=gap//2
        print(sortArr)
        print(sortArr.__len__(),count)

    """插入排序"""
    def insert(self,sortArr):
        print(sortArr[1])
        """从第2个元素开始依次取出数组中的元素"""
        count = 0
        for i in range(1,sortArr.__len__()):

            for j in range(i,0,-1):
                count+=1
                rdata = sortArr[j]
                lData = sortArr[j-1]
                """ 如果值小于当前数据 将两个数据的位置交换
                    如果值大于或者等于当前数据 结束循环"""
                if(rdata<lData):
                    sortArr[j]=lData
                    sortArr[j-1]=rdata
                else:
                    break
        print(sortArr)
        print(sortArr.__len__(),count)



        

    """冒泡排序"""
    def bubble(self,sortArr):
        count = 0
        '''循环n次'''
        for i in range(sortArr.__len__()):
            rc = 0;
            '''从第一个元素开始 遍历 
                判断当前元素与下一个元素的值
                如果大于下一个元素 则将两个元素 对换位置'''
            for j in range(sortArr.__len__()-i-1):
                count+=1
                ld = sortArr[j]
                rd = sortArr[j+1]
                if(ld>rd):
                    sortArr[j]=rd
                    sortArr[j+1]=ld
                    rc+=1
            if(rc==0):
                break;
        print(sortArr)
        print(sortArr.__len__(),count)

    def select(self):
        '''依次遍历数组'''
        count = 0
        for i in  range(self.arr.__len__()):
            '''从第i个元素开始依次向后对比 
            选择出最小元素的下标  
            然后将最小元素 与当前元素替换位置'''
            mi = i
            mv = self.arr[i]
            for j in range(i+1,self.arr.__len__()):
                count += 1
                if(self.arr[j]<mv):
                    mv = self.arr[j]
                    mi = j
            if(mi!=i):
                self.arr[mi]=self.arr[i]
                self.arr[i]=mv

        print(self.arr)
        print(self.arr.__len__(),count)

sd = SortDemo()
#sd.insert(sd.arr)
#sd.shell(sd.arr)
sd.shell1(sd.arr)
#sd.bubble(sd.arr)
#sd.select()
#sd.shell(sd.arr)




