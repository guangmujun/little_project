# -*- coding: utf-8 -*-
"""
Created on 2019/5/7 15:33 

@author: WangYuhang

@function:卡方检验、关联性分析
"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# 卡方检验
def chi_square(X,Y,num):
    model1 = SelectKBest(chi2, k=num)#选择k个最佳特征
    m = model1.fit_transform(X, Y)#iris.data是特征数据，iris.target是标签数据，该函数可以选择出k个特征
    score = model1.scores_  # 得分
    p = model1.pvalues_  # p值
    print('得分： %s' %(score))
    print('P值： %s' % (p))