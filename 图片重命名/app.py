# -*- coding: utf-8 -*-
"""
Created on 2019/8/10 15:59 

@author: WangYuhang

@function:
"""

import os

pic_path = 'E:\\GitHub\\little_project\\钉钉\\pics_add\\'
files = os.listdir(pic_path)
i = 0
for item in files:  # 进入到文件夹内，对每个文件进行循环遍历
    os.rename(os.path.join(pic_path, item), os.path.join(pic_path, (str(i)+'.jpg')))  # 表示找到每个文件的绝对路径并进行拼接操作
    i += 1