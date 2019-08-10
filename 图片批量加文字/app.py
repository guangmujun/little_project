# -*- coding: utf-8 -*-
"""
Created on 2019/8/10 16:03 

@author: WangYuhang

@function:
"""

import os
import cv2

# 加载背景图片
pic_path = './pics/'
save_path = './pics_add/'
files = os.listdir(pic_path)
i = 0
for item in files:
    a = os.path.join(pic_path, (str(i)+'.jpg'))
    b = os.path.join(save_path, (str(i)+'.jpg'))

    bk_img = cv2.imread(a)

    # 确定图片宽和高
    sp = bk_img.shape
    img_width, img_height = sp[0], sp[1]

    # 在图片上添加文字信息
    cv2.putText(bk_img, "Loving You, ZQ", (int(img_width*0.2), int(img_height*0.9)), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (0, 0, 0), 2, cv2.LINE_AA)

    # 显示图片
    # cv2.imshow("add_text", bk_img)
    # cv2.waitKey()

    # 保存图片
    cv2.imwrite(b, bk_img)

    i += 1


