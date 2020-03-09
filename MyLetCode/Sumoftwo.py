# _*_ coding:utf-8 _*_

#@Time :2020/3/9 

# @Author : litao

# @File : Sumoftwo.py

def sum(num, targt):
    hash = {}
    for i in range(0, len(num)):
        if (targt - num[i]) in hash:
            print(targt - num[i], hash)
            return hash[targt - num[i]], i
        hash[num[i]] = i
    return -1, -1
print(sum([2, 7, 11, 15], 9))