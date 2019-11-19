# Matplotlib
## 直方图
import numpy as np
from matplotlib import pyplot as plt
# data1 = np.random.randn(100000)  # 正态分布
# data2 = np.random.rand(100000)   # 均匀分布
# plt.hist(data1,100,alpha=0.7,normed=True)  # 第二个参数：柱子的个数
# plt.hist(data2,100,alpha=0.4,normed=True)
# plt.grid(True,ls='--')
# plt.legend(['Normal','Uniform'])
# plt.show()

## 垂直柱状图
# data1 = [107,115,145,212,280]
# data2 = [190,260,310,380,410]
# years = np.arange(2000,2005,1)
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False
# plt.figure(figsize=(10,6))
# plt.bar(years,data2,label='大学录取人数',color='b',width=0.3,alpha=0.3)
# for x,y in zip(years,data2):
#     plt.text(x,y,y,ha='center',va='bottom')  # 写上y数据
# plt.bar(years+0.3,data1,label='大学毕业人数',color='g',width=0.3,alpha=0.3)
# plt.grid(color='r',linestyle='--',linewidth=1,axis='y',alpha=0.3)
# for x,z in zip(years+0.3,data1):
#     plt.text(x,z,z,ha='center',va='bottom')  # 写上y数据
# plt.xlabel('年度')
# plt.ylabel('大学录取/毕业人数(万)')
# plt.title('中国大学录取/毕业人数数据（2000年-2004年）')
# plt.legend()
# plt.show()

## 水平柱状图
# data1 = [107,115,145,212,280]
# data2 = [190,260,310,380,410]
# years = np.arange(2000,2005,1)
# plt.barh(years,data2,label='大学录取人数',color='b',height=0.5,alpha=0.3)
# plt.barh(years,data1,label='大学毕业人数',color='g',alpha=0.6)
# plt.grid(color='r',linestyle='--',linewidth=1,axis='x',alpha=0.4)
# plt.show()

## 散点图
# x = np.random.random(50)
# y = x + np.random.random(50)/8
# plt.scatter(x,y,s=x*300,c='r',marker='.')
# plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\散点图.png',dpi=1000)

## 箱线图
# data1 = [107,115,145,212,280,338,350,358,368]
# data2 = [900,260,310,380,410,500,510,580,600]
# label = ['毕业人数','录取人数']
# plt.figure()
# plt.rcParams['font.sans-serif'] = 'SimHei'  # 字体，中文显示问题
# plt.rcParams['axes.unicode_minus'] = False
# plt.boxplot((data1,data2),notch=True,labels=label,meanline=True)
# plt.grid(color='k',linestyle='--',linewidth=1,axis='y',alpha=0.4)
# plt.xlabel('类型')
# plt.ylabel('人数（万）')
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\箱线图.png',dpi=1000)

# Seaborn
import seaborn as sns
tips =sns.load_dataset('tips')
sns.set(style='ticks')
# sns.set(style='whitegrid',palette='muted',color_codes=True)
# plt.plot(np.arange(10),marker='D')
# plt.show()

## 散点图
# sns.set(style='ticks')
# fig,axes = plt.subplots(1,2,figsize=(8,4))
# sns.stripplot(x='day',y='total_bill',ax=axes[0],data=tips,hue='smoker')
# sns.swarmplot(x='day',y='total_bill',ax=axes[1],data=tips,hue='smoker')
# sns.despine()  # 去掉坐标轴
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\散点图.png',dpi=1000)

## 箱线图
# sns.boxplot(x='day',y='total_bill',hue='smoker',orient='v',palette='Set3',data=tips)
# sns.despine()  # 去掉坐标轴
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\箱线图.png',dpi=1000,bbox_inches='tight',pad_inches=0)

## 琴形图
# fig,axes = plt.subplots(1,2,figsize=(13,6))
# sns.violinplot(x='day',y='total_bill',ax=axes[0],data=tips,hue='sex',split=True)
# sns.violinplot(x='day',y='total_bill',ax=axes[1],data=tips,hue='sex',inner='stick')  # inner参数对每个数据进行可视化
# sns.swarmplot(x='day',y='total_bill',ax=axes[0],data=tips,color='R',alpha=0.6)
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\琴形图.png',dpi=1000,bbox_inches='tight',pad_inches=0)

## 柱状图
# sns.barplot(x='day',y='tip',hue='sex',data=tips)
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\柱状图.png',dpi=1000,bbox_inches='tight',pad_inches=0)

## 计数图
# sns.countplot(x='day',data=tips,palette='Set2')
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\计数图.png',dpi=1000,bbox_inches='tight',pad_inches=0)

## 分组关系图
# sns.factorplot(x='size',col='sex',data=tips,col_wrap=2,kind='count',size=4,aspect=0.9)
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\分组关系图.png',dpi=1000,bbox_inches='tight',pad_inches=0)

## 单变量分布图
# fig,axes = plt.subplots(2,2,figsize=(10,6))
# sns.distplot(tips['tip'],ax=axes[0][0])
# sns.distplot(tips['tip'],ax=axes[0][1],kde=False)
# sns.distplot(tips['tip'],ax=axes[1][0],hist=False)
# sns.distplot(tips['tip'],ax=axes[1][1],rug=True)
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\单变量分布图.png',dpi=1000,bbox_inches='tight',pad_inches=0)

## 多变量分布图
# sns.jointplot(x='tip',y='total_bill',data=tips,kind='reg',color='b')
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\多变量分布图.png',dpi=1000,bbox_inches='tight',pad_inches=0)

# sns.pairplot(tips,diag_kind='hist',hue='sex',markers=['x','o'])
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\多变量分布图2.png',dpi=1000,bbox_inches='tight',pad_inches=0)

## 热力图
# sns.set(font='SimHei')  # 设置中文字体
# sns.heatmap(tips.corr(),xticklabels=True,yticklabels=True,cmap='rainbow',annot=True,square=True)
# plt.title('热力图')
# # plt.show()
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\热力图.png',dpi=1000,bbox_inches='tight',pad_inches=0)

## 回归图
# sns.lmplot('total_bill','tip',hue='smoker',markers=['x','o'],data=tips)
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\回归图1.png',dpi=1000,bbox_inches='tight',pad_inches=0)
# sns.lmplot('total_bill','tip',col='sex',row='time',data=tips,ci=None)
# plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\回归图2.png',dpi=1000,bbox_inches='tight',pad_inches=0)
# plt.show()

## 网格图
g = sns.FacetGrid(tips,col='time',row='smoker')
g.map(plt.scatter,'total_bill','tip',color='b')
# plt.show()
plt.savefig(r'E:\\GitHub\\little_project\\little_project\\图表\\常用图表\\result\\seaborn\\网格图.png',dpi=1000,bbox_inches='tight',pad_inches=0) 


