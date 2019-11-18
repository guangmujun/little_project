
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.cbooo.cn/year?year=2018'


def getInfo(url):
    time.sleep(2)
    rawhtml = requests.get(url).text
    soup = BeautifulSoup(rawhtml,'lxml')
    return soup.find('dl',{'class':'dltext'}).a.string

rawhtml = requests.get(url).text
soup = BeautifulSoup(rawhtml,'lxml')
movies_table = soup.find('table',{'id':'tbContent'})
movies = movies_table.find_all('tr')

names = [tr.find_all('td')[0].a.get('title') for tr in movies[1:]]
urls = [tr.find_all('td')[0].a.get('href') for tr in movies[1:]]
types = [tr.find_all('td')[1].string for tr in movies[1:]]
boxoffices = [int(tr.find_all('td')[2].string) for tr in movies[1:]]
countries = [tr.find_all('td')[5].string for tr in movies[1:]]
print('爬取导演信息...')
directors = [getInfo(url) for url in urls]

df = pd.DataFrame({'电影名':names,
                    '类型':types,
                    '票房':boxoffices,
                    '国家及地区':countries,
                    '观看地址':urls,
                    '导演':directors},columns=['电影名','类型','票房','国家及地区','观看地址','导演'])
df.head()
df.to_csv('movies.csv',index=False,encoding='utf_8_sig')

a = df.groupby('国家及地区').agg({'票房':[('数量','count'),('平均票房','mean')]})
print(a)