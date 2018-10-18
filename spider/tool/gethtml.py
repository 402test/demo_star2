# encoding: utf-8
__author__ = 'ChengweiHuang'
__date__ = '2018/10/17 16:24'
import requests
import time
from tool.get_proxies import random_get_prox as pox
headers={
'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
}
def is_get(url,head=headers,cook=None,nums = 3):
    for i in range(nums):
        try:
            if cook ==None:
                html = requests.get(url=url,headers = head, proxies=pox(),timeout= 5)
            else:
                html = requests.get(url=url, headers=head, proxies=pox(),timeout= 5,cookies = cook)

            if html.status_code == 200:
                return html
            else:
                print('返回值不是200')
                print(html.status_code)
                time.sleep(1)
                continue
        except Exception as e:
            print('is error ::', e)
            time.sleep(1)