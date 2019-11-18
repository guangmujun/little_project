import os
import re
import time
import requests
import os.path
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as pl  # 多线程

dstDir = r'E:\\GitHub\\little_project\\little_project\\爬虫\\院士信息'


def download(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    rawhtml = response.text
    time.sleep(2)
    return BeautifulSoup(rawhtml,'lxml')


def spider(item):
    perUrl,name = item
    perUrl = 'http://www.cae.cn' + perUrl
    name = os.path.join(dstDir,name)
    soup = download(perUrl)
    imgUrl = soup.select('div .info_img a img')[0].get("src")
    imgUrl = 'http://www.cae.cn' + imgUrl
    with open (name+'.jpg','wb') as fp:
        fp.write(requests.get(imgUrl).content)
    tag = soup.select('div .intro p')
    intro = []
    for sibling in tag:
        intro.append(sibling.string.strip())
    with open(name+'.doc','wt',encoding='utf-8') as fp:
        fp.write('\n'.join(intro))


def main():
    if not os.path.isdir(dstDir):
        os.makedir(dstDir)

    url = 'http://www.cae.cn/cae/html/main/col48/column_48_1.html'
    soup = download(url)
    ys_tag = soup.select('div .ysxx_namelist ul')[2:4]  # .表示属性 #表示id 之间用空格隔开
    pattern = r'<li class="name_list"><a href="(.+?)" target="_blank">(.+?)</a></li>'  # 正则表达式匹配出网址和名字
    ys_info = re.findall(pattern,str(ys_tag))

    if __name__ == '__main__':
        pool = pl(4)
        pool.map(spider,ys_info)
        pool.close()
        pool.join()

main()