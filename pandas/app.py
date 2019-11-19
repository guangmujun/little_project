import pandas as pd
from pandas import Series,DataFrame
import numpy as np

pds1 = Series([1,2,3,4],index=['a','b','c','d'])
dict1 = {'i1':1,'i2':2,'i3':3}
pds2 = Series(dict1, index=['i1','i2','i3'])


data = {
    'name':['张三','李四','王二'],
    'sex':['男','女','男'],
    'age':[20,19,21]
}
df = DataFrame(data, columns=['name','sex','age'])
df1 = DataFrame(np.arange(9).reshape(3,3), index=['L1','L2','L3'], columns=['id1','id2','id3'])
df2 = df.reindex(index=['L1','L2','L3','L4'], columns=['id1','id2','id3'], fill_value=9)  # fill_value对缺失值进行填充
df3 = df2.ix[[0,2],0:2]  # 切片，第0和第2行，前两列
df4 = df[(df['sex']=='男') & (df['age']>20)]  # 查询，性别为男，年龄大于20岁

# 操作行与列
append_data = {
    'name':'朱八',
    'sex':'女',
    'age':35
}
new_df = df.append(append_data,ignore_index = True)
new_df['city'] = ['北京','上海','广州','重庆']
new_df.drop(1)  # 删除行
new_df.drop(['city','age'],axis=1,inplace=False)  # 删除列
# print(new_df.rename(index={0:4,1:5}, columns={'age':'year'}))  # 完成行和列索引标签的修改

# 函数应用与映射
# map()  Series元素操作
data = {
    'name':['张三','李四','王二'],
    'sex':['男','女','男'],
    'high':['150cm','190cm','180cm']
}
df5 = DataFrame(data,index = ['name','sex','high'])
def f(s):
    return s.split('cm')[0]
df5['high'] = df5['high'].map(f)

#apply()  DataFrame行列操作
df6 = DataFrame(np.random.rand(3,3),columns = ['a','b','c'])
f = lambda x:x.mean()
df7 = df6.apply(f,axis=0)  # 0： 求解每列平均值 1:每行

# applymap()  DataFrame元素操作
df8 = df6.applymap(lambda x: x+1)


# 数据清洗

## 处理缺失值
NA = np.nan
A = DataFrame([[1,2,3],[4,5,NA],[6,NA,7]],columns=list('abc'),index=list('123'))
### 填充
# print(A.fillna(value=A.stack().mean()))
# print(A.fillna(method='ffill',axis=1))
### 删除
print(A.dropna())  # 删除NA所在的行
print(A.dropna(axis=1))

## 处理重复值
data = {
    'id':[1,2,3,1,4],
    'name':['apple','pear','banana','apple','peach'],
    'price':[5,4,3,5,3]
}
df = DataFrame(data)
print(df.drop_duplicates())  # 保留第一次出现的值
print(df.drop_duplicates(['name','price'],keep='last'))

## 替换值
# df.replace(np.nan:1066,'':'大连')


# 数据分组
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

tips = sns.load_dataset('tips')
groupdata = tips['tip'].groupby(tips['sex']).mean()

groupdata1 = tips['tip'].groupby(tips['day']).mean()

size_mean2 = tips.groupby('size')['tip'].mean()
size_mean2.plot()

