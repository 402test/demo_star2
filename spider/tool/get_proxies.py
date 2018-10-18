# encoding: utf-8
__author__ = 'ChengweiHuang'
__date__ = '2018/10/17 16:38'
import random
text = {"code":0,"success":'true',"msg":"0","data":[{"ip":"117.42.234.201","port":"4576"},{"ip":"182.247.182.162","port":"4581"},{"ip":"36.41.108.139","port":"4575"},{"ip":"106.60.24.150","port":"4528"},{"ip":"117.23.35.129","port":"4575"},{"ip":"183.150.70.10","port":"4576"},{"ip":"183.188.78.18","port":"4587"},{"ip":"117.43.215.92","port":"4568"},{"ip":"1.25.147.48","port":"4599"},{"ip":"121.231.32.247","port":"4552"}]}
L = []
for i in text['data']:
    data = {'https':'%s:%s'%('http://'+str(i['ip']),i['port'])}
    L.append(data)

print(L)
def random_get_prox():
    #return random.choice(L)
    return None
#
# proxies = {
#   'http': 'http://172.18.101.221:3182',
#   'https': 'http://172.18.101.221:1080',
# }
#
# requests.get("http://example.org", proxies=proxies)
