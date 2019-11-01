# -*- coding: utf-8 -*-
"""
Created on 2019/10/12 9:32 

@author: WangYuhang

@function:
"""

import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import urllib.request

login_url = 'http://sep.ucas.ac.cn/'
notice_url = 'http://sep.ucas.ac.cn/portal/site/226/821'
lecture_url = 'http://jwxk.ucas.ac.cn/subject/humanityLecture'
imgUrl = "http://sep.ucas.ac.cn/changePic "
usename = 'your-usename'
password = 'your-password'

chrome_options = Options()
chrome_options.add_argument('--headless')  # 无界面
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速。
chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
browser = webdriver.Chrome('chromedriver', chrome_options=chrome_options)


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

    my_url = 'https://oapi.dingtalk.com/robot/send?access_token=d0e375b4215e453ced4d308d66f38d695e3f2ba1f19c4fe88fcdea627cb8e66f'

    send_request(my_url, my_data)


def init_login():
    browser.get(login_url)
    elem_user = browser.find_element_by_name('userName')
    elem_user.send_keys(usename)  # 输入用户名
    elem_pwd = browser.find_element_by_name("pwd")
    elem_pwd.send_keys(password)  # 密码
    browser.save_screenshot(str("登录界面.png"))  # 验证码
    browser.find_element_by_name("certCode").send_keys(input("输入验证码\n>>> "))

    browser.find_element_by_name("sb").click()
    time.sleep(5)  # 等待10s
    current_url = browser.current_url  # 当前页面的url
    print(current_url)


def get_page():
    global max_id
    browser.get(notice_url)  # 跳转到你要爬取的页面
    time.sleep(5)
    current_url = browser.current_url  # 当前页面的url
    print(current_url)

    browser.get(lecture_url)  # 跳转到你要爬取的页面
    time.sleep(5)
    html = browser.page_source  # 获得当前页面的html字符串
    selector = etree.HTML(html)
    content = selector.xpath('//td[1]/text()')

    in_text = ''
    for i in range(0, 3):
        in_text = in_text + content[i][0:9] + '\n\n' + content[i][9:] + '\n\n'

    # 获得讲座序号
    get_id = max([int(each[5:8]) for each in content])
    max_id = int(open('num.txt', 'r').readline())

    if get_id > max_id:
        with open('num.txt', "w") as f:
            f.write(str(get_id))
        send_news('讲座更新', in_text)
    else:
        print('讲座未更新！')
    browser.quit()


if __name__ == "__main__":
    try:
        while 1:
            localtime = time.strftime('%H', time.localtime(time.time()))
            if int(localtime) in range(7, 20):  # 07:00-19:00
                init_login()  # 登陆教务系统
                get_page()  # 获取讲座信息
                time.sleep(1800)
    except Exception as e:
        send_news('错误提示', e)

