# -*- coding: UTF-8 -*-
__author__ = 'ChengweiHuang'
__date__ = '2018/10/17 14:15'
from multiprocessing import Pool
import requests
import time
import json
import re
from tool.gethtml import is_get
from tool.get_cookies import active,cookkk


class Spidersss(object):
    cookies = {'Cookie':'_T_WM=364d128fbe3b73150252be595c16b750; WEIBOCN_FROM=1110005030; MLOGIN=0; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803; SUB=_2A252w2-pDeRhGeBI7FIS9y_EyDyIHXVSTHHhrDV6PUJbkdAKLXPbkW1NRmzvO2qv_Sg93XKk1UX4SbZI8Kjplar5; SUHB=0U1ZY-VBZZOjsN; SCF=AqG77RSxkdgad39uWIEk1TJTXYfO_0vGjGsJB624dWjof6KSIPZ2WsIs3F4jWcryE0F5a20pAI5fw_eLS6mRgvY.; SSOLoginState=1539776506'}
    cookies2 = {'Cookie':'_T_WM=364d128fbe3b73150252be595c16b750; WEIBOCN_FROM=1110005030; SUB=_2A252w2-pDeRhGeBI7FIS9y_EyDyIHXVSTHHhrDV6PUJbkdAKLXPbkW1NRmzvO2qv_Sg93XKk1UX4SbZI8Kjplar5; SUHB=0U1ZY-VBZZOjsN; SCF=AqG77RSxkdgad39uWIEk1TJTXYfO_0vGjGsJB624dWjof6KSIPZ2WsIs3F4jWcryE0F5a20pAI5fw_eLS6mRgvY.; SSOLoginState=1539776506; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E6%259D%25A8%25E5%25B9%2582%26oid%3D4295324657126890%26fid%3D1076031195242865%26uicode%3D10000011'}
    headers = {
        'Host': 'm.weibo.cn',
       # 'Referer': 'https://m.weibo.cn/u/1195242865?uid=1195242865&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%9D%A8%E5%B9%82',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    }
    def __init__(self,url,name,nums=None):
        self.url = url
        self.name = name
        self.nums = nums
        self.isrun()
    def isrun(self):
        for n in self.nums:
            if n != 1:
                self.url+='&page=%d'%(n)
            html = is_get(self.url, self.headers)
            html_data = json.loads(html.content)
            for i in html_data['data']['cards']:
                if 'mblog' in i:
                    # print(i['mblog']['text'])
                    self.id = i['mblog']['id']
                    my_time = i['mblog']['created_at']
                    islike = i['mblog']['attitudes_count']
                    comments = i['mblog']['comments_count']
                    datas = re.sub('<(.*?)>', '', i['mblog']['text'], 0)
                    print('时间',my_time,'点赞数',islike,'评论数',comments)
                    print(datas)
                    self.status = 'https://m.weibo.cn/comments/hotflow?id=%s&mid=%s&max_id_type=0'%(self.id,self.id)
                    print('####################################################')

                    self.get_fans()



    def get_fans(self):
        print('开始获取粉丝信息  1000条 ')
        #html1 = is_get(,
        #              , self.cookies2)   #   cookies  激活

        html1 = active(self.status,self.headers)   #  激活
        data = json.loads(html1.content)
        self.max_id = data['data']['max_id']
        print('原',self.max_id)
        for i in range(1000):
            time.sleep(1)
            url = 'https://m.weibo.cn/comments/hotflow?id=%s&mid=%s&max_id=%s&max_id_type=0'%(self.id,self.id,self.max_id)
            html2 = is_get(url,self.headers,  cookkk())
            if html2.content!= b'{"ok":0}':
                datas = json.loads(html2.content)
            else:
                url = 'https://m.weibo.cn/comments/hotflow?id=4295324657126890&mid=4295324657126890&max_id=%s&max_id_type=1' % (
                self.max_id)
                html2 = is_get(url, self.headers, cookkk())
                datas = json.loads(html2.content)
            try:
                self.max_id = datas['data']['max_id']
                print(self.max_id)
                for i in datas['data']['data']:
                    mytest = re.sub('<(.*?)>', '', i['text'], 0)
                    print(str(mytest).replace(' ','').replace('\n',''))
            except:
                print(html2.content)
                raise

if __name__ == '__main__':
    url = 'https://m.weibo.cn/api/container/getIndex?uid=1195242865&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%9D%A8%E5%B9%82&type=uid&value=1195242865&containerid=1076031195242865'
    name = '杨幂'
    Spidersss(url,name,[x for x in range(1,21)])


    # p = Pool()
    # for i in range(4):  # CPU有几核，每次就取出几个进程
    #     p.apply_async(func=func, args=(50,))
    # p.close()
    # p.join()
    #
    # print('程序结束')