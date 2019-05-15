# -*- coding: utf-8 -*-
"""
Created on 2019/5/8 15:20 

@author: WangYuhang

@function:Person关联性分析，线性关联性分析，适用于数值型变量
        1）输入：x为特征，y为目标变量.
        2）输出：r： 相关系数 [-1，1]之间，p-value: p值。
         注： p值越小，表示相关系数越显著，p<0.01表示非常显著，p<0.05显著相关
            |r|>0.8：高度相关 0.5<|r|<0.8：中度相关 0.3<|r|<0.5：低度相关 |r|<0.3不相关
"""

import scipy
from scipy.stats import pearsonr


import numpy
my_matrix = numpy.loadtxt(open("E:\GitHub\Zone\data\南京基础交通网络\\trip_production.csv","rb"),delimiter=",",skiprows=0)
print(my_matrix)

# x = scipy.array([1, 2, 3, 4, 5])
# y = scipy.array([2, 4, 6, 8, 9])

# r_row, p_value = pearsonr(x, y)
# print(r_row)
# print(p_value)