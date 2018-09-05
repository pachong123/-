
# 煎蛋网 妹子板块 图片的爬取
# 完成时间：2018-09-03
# 网址：http://jandan.net/ooxx

import requests
from bs4 import BeautifulSoup
import base64
import time
import os

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# 爬取图片并下载
def get_info(url):
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text,'lxml')
    image_hashs = soup.select('.img-hash')

    image_urls = []
    for image_hash in image_hashs:
        image_urls.append('https:' + base64.b64decode(image_hash.get_text()).decode())

    path = 'C:\\Users\\Administrator\\Desktop\\image\\'    # 新建文件夹
    if not os.path.exists(path):
        os.makedirs(path)
    
    global counter    # 设置全局变量
    for url in image_urls:
        name = url.split('/')[-1]    # .gif .jpg图片格式 使用字符串方式获取图片名
        response = requests.get(url,headers = headers)
        # print(url)    # 用于监视程序运行的状况
        with open(path + name,'wb') as file:
            file.write(response.content)
        if counter%20 == 0:    # 每下载20张图片，就显示一下
            print('已下载%d张图片'%counter)
        counter += 1

# 主程序
if __name__ == "__main__":
    counter = 1
    urls = ['http://jandan.net/ooxx/page-{}#comments'.format(i) for i in range(12)]    # 一共有39页
    for url in urls:
        get_info(url)
        time.sleep(1.5)
    print('all done you can enjoy it on desktop....')

