# -*- coding: utf-8 -*-
"""
Created on 2019/5/10 9:13 

@author: WangYuhang

@function:数据的标准化处理和还原
"""

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from matplotlib import gridspec
import numpy as np
import matplotlib.pyplot as plt

# cps = np.random.random_integers(0, 100, (100, 2))
# ss = StandardScaler()
# std_cps = ss.fit_transform(cps)
# gs = gridspec.GridSpec(5, 5)
# fig = plt.figure()
# ax1 = fig.add_subplot(gs[0:2, 1:4])
# ax2 = fig.add_subplot(gs[3:5, 1:4])
# ax1.scatter(cps[:, 0], cps[:, 1])
# ax2.scatter(std_cps[:, 0], std_cps[:, 1])
# plt.show()

data = np.random.uniform(0, 100, 10)[:, np.newaxis]
ss = StandardScaler()
std_data = ss.fit_transform(data)# 标准化
origin_data = ss.inverse_transform(std_data) # 标准化还原
print('data is ',data)
print('after standard ',std_data)
print('after inverse ',origin_data)
print('after standard mean and std is ',np.mean(std_data), np.std(std_data))


