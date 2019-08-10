# -*- coding: utf-8 -*-
"""
Created on 2019/8/10 16:55 

@author: WangYuhang

@function:
"""

import time
import datetime


# logfile：监测信息写入文件
def MonitorSystem(logfile = None):
    # 获取当前时间
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} '
    print(line)
    if logfile:
        logfile.write(line)


def loopMonitor():
    while True:
        MonitorSystem()
        # 2s检查一次
        time.sleep(3)

loopMonitor()