# -*- coding: utf-8 -*-
"""
Created on 2019/10/25 10:32 

@author: WangYuhang

@function: 百度OCR文字识别
"""
from aip import AipOcr

config = {
    'appId': '17615379',
    'apiKey': 'nmAtlbhpcUBQGp34NPGtEIQ0',
    'secretKey': 'oFbAwA32YhHQiEA94fcaXbTzw4q6TukS'
}

client = AipOcr(**config)


def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()


def img_to_str(image_path):
    image = get_file_content(image_path)

    # 定义参数变量
    options = {
        # 定义图像方向
        'detect_direction': 'false',
        # 识别语言类型，默认为'CHN_ENG'中英文混合
        'language_type': 'ENG',
    }
    result = client.basicGeneral(image, options)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])

from PIL import Image

filepath = 'code.jpg'
image = Image.open(filepath)
# 传入'L'将图片转化为灰度图像
image = image.convert('L')
# 传入'1'将图片进行二值化处理
# image = image.convert('1')
image.save('code2.jpg')

a = img_to_str('code2.jpg')
print(a)

