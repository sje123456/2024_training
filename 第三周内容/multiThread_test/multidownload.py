# -*- coding: utf-8 -*-

#!/usr/bin/env python3
"""
Created on Tue Jun 11 19:52:15 2024

@author: sss
"""

import requests
from threading import Thread

# 百度首页URL
url = 'https://www.baidu.com'

# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 保存网页内容的函数
def download_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open('baidu.html', 'wb') as file:
                file.write(response.content)
            print(f'下载完成：{url}')
    except Exception as e:
        print(f'下载出错：{e}')

# 创建多线程下载
threads = []
for i in range(5):  # 创建5个线程
    thread = Thread(target=download_page, args=(url,))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print('所有线程已完成下载。')
