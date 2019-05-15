# -*- coding: utf-8 -*-
"""
Created on 2019/5/6 17:07 

@author: WangYuhang

@function:读写.dat文件
        修改后缀名当作TXT处理
        txt文件的一行一列处理
"""

import numpy

dic = 'E:\GitHub\Zone\data\南京基础交通网络\\rowOD.txt'
od_dic = 'E:\GitHub\Zone\data\南京基础交通网络\OD.txt'

# 读取一列
def read_acol(i):
    f = open(dic)
    list1 = []
    line = f.readline()
    while line:
        a = line.split()
        b = a[i]  # 这是选取需要读取的位数
        list1.append(b)  # 将其添加在列表之中
        line = f.readline()
    f.close()
    return list1

o_list = []# 各个交通小区的发生量
for line in open(dic):# 不是每一行都有332个元素
    aline = line.split()
    aline_sum = 0.0
    for a in range(0,len(aline)):
        if len(aline[a])>10:
            aline[a] = aline[a][0: 9]
        aline_sum = aline_sum + float(aline[a])
    o_list.append(aline_sum)


d_list = []# 各个交通小区的吸引量
for i in range(0,326):
    acol = read_acol(i)
    acol_sum = 0.0
    for a in range(0,len(acol)):
        if len(acol[a])>10:
            acol[a] = acol[a][0: 9]
        acol_sum = acol_sum + float(acol[a])
    d_list.append(acol_sum)

print(len(o_list),len(d_list))

with open(od_dic, 'w') as f_od:
    f_od.write('小区编号 发生量 吸引量\n')
    for i in range(0,326):
        f_od.write(str(i+1) + ' ' +
                         str(o_list[i]) + ' ' + str(d_list[i]) + '\n')
    print('--OD.txt已生成--')