import pandas as pd

df = pd.read_html('https://shuju.wdzj.com',encoding='utf-8')
# print(df[0].iloc[:,0:6].head())

df = df[0].ix[0:100,0:6]
def f(s):
    return s.split(' ')[0]
df['平台'] = df['平台'].map(f)
df.to_excel(r'E:\\GitHub\\little_project\\little_project\\pandas\\网贷之家\data\\网贷平台.xls',sheet_name='p2p',index=['序号'])
df = pd.read_excel(r'E:\\GitHub\\little_project\\little_project\\pandas\\网贷之家\data\\网贷平台.xls')
print(df.head())

df['成交量(万元)'].hist(bins=200)
