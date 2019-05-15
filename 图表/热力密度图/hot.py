# -*- coding: utf-8 -*-
"""
Created on 2019/5/10 9:33 

@author: WangYuhang

@function:热力密度图
"""
import folium
import numpy as np
from folium.plugins import HeatMap
import webbrowser
import pandas as pd

# 创建基于folium热力图数据结构的数据对象：
# lon = np.array([i["lng"] for i in myaddress],dtype=float)
# lat = np.array([i["lat"] for i in myaddress],dtype=float)
# scale = np.random.randint(100,500,len(address))
# data1 = [[lat[i],lon[i],scale[i]] for i in range(len(address))]
# # 输入热力图数据源，并可视化输出
# map_osm = folium.Map(location=[35,110],zoom_start=5)
# HeatMap(data1).add_to(map_osm)
# file_path = r"D:/Python/Image/People.html"
# map_osm.save(file_path)
# webbrowser.open(file_path)

posi = pd.read_excel("Cities2015.xlsx")
posi = posi.dropna()
lat = np.array(posi["lat"][0:len(posi)])
lon = np.array(posi["lon"][0:len(posi)])
pop = np.array(posi["pop"][0:len(posi)],dtype=float)
gdp = np.array(posi["GDP"][0:len(posi)],dtype=float)
data1 = [[lat[i],lon[i],pop[i]] for i in range(len(posi))]
map_osm = folium.Map(location=[35,110],zoom_start=5)
HeatMap(data1).add_to(map_osm)
file_path = r"PeopleGDP.html"
map_osm.save(file_path)   #保存本地
webbrowser.open(file_path) #在本地浏览器打开

