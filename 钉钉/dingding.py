# -*- coding: utf-8 -*-
"""
Created on 2019/8/7 12:41 

@author: WangYuhang

@function:
"""
import os
import json
import time
import datetime
import urllib.request


def get_Copywriting():
    # 计算天数
    inLoveDate = datetime.datetime(2018, 12, 31)
    todayDate = datetime.datetime.today()
    inLoveDays = (todayDate - inLoveDate).days  # 在一起的天数
    word_pic_id = inLoveDays - 222
    print('索引:%s' % word_pic_id)

    # 情话内容
    file_path = 'love_words.txt'
    with open(file_path, encoding='UTF-8') as file:
        love_word = file.readlines()[word_pic_id].split('、')[1]

    # 获得图片
    love_image_file = 'https://raw.githubusercontent.com/guangmujun/little_project/master/%E9%92%89%E9%92%89/pics_add/' + str(word_pic_id) + '.jpg'
    Copywriting = "你好哇，紫琪！\n\n\n我们在一起的 %s 天\n\n今天老王想对你说：\n\n\" %s \"\n\n最后也是最重要的！\n ![screenshot](%s)"
    Copywriting = Copywriting % (inLoveDays, love_word, love_image_file)

    return Copywriting


def send_request(url, datas):
    # 传入url和内容发送请求
    # 构建一下请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    sendData = json.dumps(datas)  # 将字典类型数据转化为json格式
    sendDatas = sendData.encode("utf-8")  # python3的Request要求data为byte类型
    # 发送请求
    request = urllib.request.Request(url=url, data=sendDatas, headers=header)
    # 将请求发回的数据构建成为文件格式
    opener = urllib.request.urlopen(request)
    # 7、打印返回的结果
    print(opener.read())


def send_news(in_title, in_text):
    # 按照钉钉给的数据格式设计请求内容
    my_data = {
        "msgtype": "markdown",
        "markdown": {"title": " ",
                     "text": " "
                     },
        "at": {

            "isAtAll": True
        }
    }
    # 获取当天文案
    my_data["markdown"]["title"] = in_title
    my_data["markdown"]["text"] = in_text

    my_url = 'https://oapi.dingtalk.com/robot/send?access_token=aaef8b9906bdb3cf78cd13e14b5c2467730ec6ad7d1d4b303ac2e4d25370b36f'

    send_request(my_url, my_data)


def MonitorSystem(logfile = None):
    # 获取当前时间
    now = datetime.datetime.now()
    ts = now.strftime('%H:%M:%S')
    if logfile:
        logfile.write(ts)
    return ts


def loopMonitor():
    while True:
        ts = MonitorSystem()
        # print(ts)
        if ts == '09:00:00':
            print('发送每日情话')
            in_title = "每日情话"
            in_text = get_Copywriting()
            send_news(in_title, in_text)
        elif ts == '17:00:00':
            print('发送每日问候')
            in_title = "每日问候"
            in_text = '每天多爱你一点\n用心、关心'
            send_news(in_title, in_text)
        elif ts == '08:55:00':
         	print('程序测试成功')
         	in_title = "测试"
            in_text = '测试成功，哈哈哈哈'
            send_news(in_title, in_text)
        time.sleep(1)


def main():
    loopMonitor()


if __name__ == "__main__":
    main()
