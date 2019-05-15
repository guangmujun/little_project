# -*- coding: utf-8 -*-
"""
Created on 2019/5/6 11:26 

@author: WangYuhang

@function: 最小二乘法拟合
"""

###最小二乘法直线拟合试验###
import numpy as np
from scipy.optimize import leastsq

###采样点(Xi,Yi)###
# Xi=np.array([669184.849,669238.6199,669560.3493,669590.4885,669463.0366,669207.3004,668224.5249,667962.3971,670184.3452,671304.0393])
# Yi=np.array([12099.1,12154.8,12459.4,12496.1,12363.1,12101.8,11131.6,10884,13082.8,14200.1	])

# Xi=np.array([3559607.215,3559610.685,3559631.471,3559842.086,3560386.794,3560457.937,3559551.125,3560389.516,3560164.547,3560709.253])
Xi=np.array([3559607,3559610,3559631,3559842,3560386,3560457,3559551,3560389,3560164,3560709])
Yi=np.array([20222,20206.5,20228.9,20434.8,21006.4,21080.1,20166.2,20968.7,20757.8,21294])


###需要拟合的函数func及误差error###
def func(p,x):
    k,b=p
    return x+b

def error(p,x,y,s):
    print(s)
    return func(p,x)-y #x、y都是列表，故返回值也是个列表

# k、b的初始值
p0=[1,2]

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
Para=leastsq(error,p0,args=(Xi,Yi,s)) #把error函数中除了p以外的参数打包到args中
k,b=Para[0]
print('k = %s\nb = %s' %(k,b))

###绘图，看拟合效果###
import matplotlib.pyplot as plt
plt.figure()
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x = np.arange(3559000, 3562000,500)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
plt.legend()
plt.show()

