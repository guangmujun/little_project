# -*- coding: utf-8 -*-
"""
Created on 2019/5/7 10:35 

@author: WangYuhang

@function: 字典相关的 操作
"""

# 最大值标准化
def dict_min_max(dic):
    dic_max = dic[max(dic, key=dic.get)]
    for i in dic:
        dic[i] = dic[i]/dic_max
    return dic


if __name__ == "__main__":
    dogdistance = {'dog-dog': 33, 'dog-cat': 36, 'dog-car': 41, 'dog-bird': 42}
    d = dict_min_max(dogdistance)
    print(d)