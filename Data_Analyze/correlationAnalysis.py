import csv
import numpy as np
#只读打开
csvFile = open("BlackFriday.csv", "r")
reader = csv.reader(csvFile)
Uid_PidDic = {}
productSet = set()

for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    if item[0] in Uid_PidDic:
        Uid_PidDic[item[0]].append(item[1])
        productSet.add(item[1])
    else:
        Uid_PidDic[item[0]] = [item[1]]
        productSet.add(item[1])
#print(Uid_PidDic['1000001'])
#print(len(Uid_PidDic))
csvFile.close()


#给商品重新编号
product_num = {}
num = 0
for item in productSet:
    product_num[item] = num
    num+=1


#商品对出现次数数组，以及商品单独出现次数
prodCor = np.zeros((3623,3623),dtype=np.int)
prodNum = np.zeros(3623,dtype=np.int)


values=Uid_PidDic.values()
location = 0

#取出某一个顾客的商品购买列表
for value in values:
    #print('location: ' + str(location), file=f)
    i = 1
    index = 0
#取出该顾客商品购买列表中的一个商品
    for product in value:
        prodNum[product_num[product]]+=1
        i = index + 1
        #print('index: '+ str(index), file=f)
        while i<len(value):
            prodCor[product_num[product]][product_num[value[i]]]+=1
            #print(prodCor[product_num[product]][product_num[value[i]]])
            i+=1
        index+=1
    location += 1

#f = open("output.rtf", 'w+')
#f.close()

for i in range(len(prodCor)):
    for j in range(len(prodCor[i])):
        if i < j:
            temp = prodCor[i][j]
            prodCor[i][j] = prodCor[j][i] = temp + prodCor[j][i]




max = prodCor[0][0]
x=y=0
a=b=0
for i in range(len(prodCor)):
    for j in range(len(prodCor[i])):
        if i < j and (prodCor[i][j] > max):
            max = prodCor[i][j]
            x = i
            y = j

#print('max is ' + str(max) + ', x is ' + str(x) + ', y is ' + str(y))
#print('x own is '+ str(prodNum[x])+', y own is ' + str(prodNum[y]))





#打印相关数据
#f = open("output.rtf", 'w+')

#f.close()
