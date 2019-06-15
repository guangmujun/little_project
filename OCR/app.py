# -*- coding: utf-8 -*-
"""
Created on 2019/6/15 9:08 

@author: WangYuhang

@function:识别图片中文字
"""

import pytesseract
from PIL import Image

tessdata_dir_config = '--tessdata-dir "D:\Program Files (x86)\Tesseract-OCR\\tessdata"'
PRO_DIC = 'D:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
DATA_DIC = 'E:\GitHub\little_project\OCR\data\\test_data'

# import os
# for filename in os.listdir(DATA_DIC):# 读取文件夹内所有文件
#     print (filename)
#     PIC_DIC = DATA_DIC + '\\' + str(filename)# 构造文件路径
#     RES_DIC ='.\\result' + '\\' + str(filename[0]) + '.txt'# 构造输出的结果路径
#
#     pytesseract.pytesseract.tesseract_cmd = PRO_DIC# 调用tesseract
#     image = Image.open(PIC_DIC )# 打开图片文件
#     text = pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)# 识别图中文字
#     print('识别完成！')
#
#     with open(RES_DIC, "w") as f:# 写入TXT
#         f.write(text)
#

pytesseract.pytesseract.tesseract_cmd = PRO_DIC# 调用tesseract
image = Image.open('E:\GitHub\little_project\OCR\data\\5.jpg' )# 打开图片文件
text = pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)# 识别图中文字

text = ''.join(text.split())# 去除空格
print(text)

with open('E:\GitHub\little_project\OCR\data\\5.txt', "w") as f:# 写入TXT
    f.write(text)
