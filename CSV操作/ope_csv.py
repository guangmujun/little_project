# -*- coding: utf-8 -*-
"""
Created on 2019/5/6 21:10 

@author: WangYuhang

@function:CSV文件的读写
"""

import pandas as pd
from itertools import islice

OD_DIC = 'E:\GitHub\Zone\data\南京主城区\OD.txt'
POPU_DIC = 'E:\GitHub\Zone\data\南京主城区\\tripPopulation.txt'
LIGHT_DIC = 'E:\GitHub\Zone\data\南京主城区\\tripLight.txt'
LANDUSE_DIC = 'E:\GitHub\Zone\data\南京主城区\Landuse.txt'
PRO_DIC = 'E:\GitHub\Zone\data\南京主城区\\trip_production.csv'
ATT_DIC = 'E:\GitHub\Zone\data\南京主城区\\trip_attraction.csv'

# 构造回归模型的输入CSV文件
trip_pro = {}
trip_att = {}
for line in islice(open(OD_DIC),1,None):
    temp=line.split()
    trip_pro[temp[0]] = temp[1]
    trip_att[temp[0]] = temp[2]

popu = {}
for line in islice(open(POPU_DIC),1,None):
    temp=line.split()
    popu[temp[0]] = temp[1]

light = {}
for line in islice(open(LIGHT_DIC),1,None):
    temp=line.split()
    light[temp[0]] = temp[1]

live,edu,gov,bus = {},{},{},{}
tra,pub,hos = {},{},{}
for line in islice(open(LANDUSE_DIC),1,None):
    temp=line.split()
    live[temp[0]] = temp[1]
    edu[temp[0]] = temp[2]
    gov[temp[0]] = temp[3]
    bus[temp[0]] = temp[4]
    tra[temp[0]] = temp[5]
    pub[temp[0]] = temp[6]
    hos[temp[0]] = temp[7]

tp = pd.Series(trip_pro)
ta = pd.Series(trip_att)

t1 = pd.Series(popu)
t2 = pd.Series(light)
t31 = pd.Series(live)
t32 = pd.Series(edu)
t33 = pd.Series(gov)
t34 = pd.Series(bus)
t35 = pd.Series(tra)
t36 = pd.Series(pub)
t37 = pd.Series(hos)

df = pd.DataFrame([tp,t1,t2,t31,t32,t33,t34,t35,t36,t37])
df = df.T
df.to_csv(PRO_DIC, index=True)

df = pd.DataFrame([ta,t1,t2,t31,t32,t33,t34,t35,t36,t37])
df = df.T
df.to_csv(ATT_DIC, index=True)