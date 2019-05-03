# -*- coding: utf-8 -*-
"""
Created on 2019/5/2 20:29 

@author: WangYuhang

@function:画带误差的多序列条状图
"""

from pylab import *
import numpy as np
from matplotlib import pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.figure()# 绘图初始化，可指定大小

n = 3# X轴柱的个数
X = np.arange(n)+1

# Y：值，S:误差，D：标签
Y1,Y11,Y111,Y1111 = [476.16,495.61,504.74],[61.09,66.70,73.85],[783.16,495.61,455.44],[68.22,66.70,60.43]
S1,S11,S111,S1111 = [15.69,30.19,301.32],[27.74,2.93,4.00],[16.02,30.19,152.00],[3.71,2.93,6.86]
D1,D11,D111,D1111 = ['aA','aA','aA'],['aA','aA','aA'],['aA','aB','aB'],['aA','aA','aA']

Y2,Y22,Y222,Y2222 = [329.65,384.03,440.70],[57.26,61.50,67.96],[566.67,384.03,408.42],[56.43,61.50,56.64]
S2,S22,S222,S2222 = [20.67,13.38,319.19],[10.45,1.18,6.01],[20.04,13.38,51.42],[5.73,1.18,0.77]
D2,D22,D222,D2222 = ['bA','bA','aA'],['aA','bA','aA'],['bA','bB','aB'],['bA','bA','aA']

Y3,Y33,Y333,Y3333 = [308.42,350.35,320.35],[55.46,56.92,56.73],[365.26,350.35,371.93],[55.02,56.92,55.63]
S3,S33,S333,S3333 = [5.02,19.56,154.88],[5.85,2.69,2.19],[33.25,19.56,78.42],[5.03,2.69,14.52]
D3,D33,D333,D3333 = ['bA','bA','aA'],['bA','bA','aA'],['cA','bA','aA'],['bA','bA','aA']

# 设置坐标轴的取值范围
plt.ylim((0, 1000))

# 画柱形图，label：种类，hatch：填充
plt.bar(X, Y1,yerr = S1,error_kw = {'ecolor' : '0.2', 'capsize' :6,},alpha=0.9, width = 0.2, facecolor = 'white', edgecolor = 'black', label='0-20', lw=1,hatch='///')
plt.bar(X+0.2, Y2,yerr = S2,error_kw = {'ecolor' : '0.2', 'capsize' :6}, alpha=0.9, width = 0.2, facecolor = 'white', edgecolor = 'black', label='20-40', lw=1,hatch='---')
plt.bar(X+0.4, Y3,yerr = S3,error_kw = {'ecolor' : '0.2', 'capsize' :6}, alpha=0.9, width = 0.2, facecolor = 'white', edgecolor = 'black', label='40-60', lw=1,hatch='\\\\\\')

#使用text显示数值
for a,b,c,d in zip(X,Y1,S1,D1):
 plt.text(a, b+c+2, '%s' % d, ha='center', va= 'bottom',fontsize=11)
for a,b,c,d in zip(X+0.2,Y2,S2,D2):
 plt.text(a, b+c+2, '%s' % d, ha='center', va= 'bottom',fontsize=11)
for a,b,c,d in zip(X+0.4,Y3,S3,D3):
 plt.text(a, b+c+2, '%s' % d, ha='center', va= 'bottom',fontsize=11)

plt.ylabel("土壤微生物量碳 MBC(mg/kg)")
plt.legend(loc='upper right',frameon=False) # 图例的位置在右上，去边框
plt.xticks((1.2,2.2,3.2),("幼龄林","中龄林","成熟林"))# 更换X轴坐标的值为汉字
plt.title("不同林龄杉木人工林非根际土壤微生物量碳")

# 去掉边框线
ax = plt.gca()
ax.spines['top'].set_visible(False) #去掉上边框
ax.spines['right'].set_visible(False) #去掉右边框

# 刻度线的朝向
tick_params(direction='in')

plt.savefig("1.png")
plt.show()





