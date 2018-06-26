import requests
import math
import sys
from sys import path
import io
import urllib3
import urllib.parse
import urllib.robotparser
import urllib.request
import urllib.response
import urllib.error
from lxml import html
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#暂时去除了退出的功能
def logout():
    url2 = 'http://172.18.18.60:8080/eportal/InterFace.do?method=logout'
    data2 = {
        'userIndex': '33376237303965346331643763393936363663666132363331316164383361385f31302e31342e3232302e3232375f55323031373137303830'
    }
    data2 = urllib.parse.urlencode(data2).encode(encoding='utf-8')
    req = urllib.request.Request(url=url2, data=data2)
    response = urllib.request.urlopen(req)
    print("-------------------您已下线")

def login(id,pwd):
    print('开始尝试登陆')
    url = 'http://172.18.18.60:8080/eportal/InterFace.do?method=login'
    data = {
        'userId': id,
        'password': pwd,
        'service':'',
        'queryString': 'wlanuserip%3Dda72b714af7b09e3fde855cd726de90e%26wlanacname%3Dfd8946c594b28b0be7399aa5ba210cc2%26ssid%3D%26nasip%3D37b709e4c1d7c99666cfa26311ad83a8%26snmpagentip%3D%26mac%3D51cb345605afb9886d97572d58488ef5%26t%3Dwireless-v2%26url%3D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30%26apmac%3D%26nasid%3Dfd8946c594b28b0be7399aa5ba210cc2%26vid%3D5539c754309b9fbd%26port%3D25ca6b42ad223b70%26nasportid%3D5b9da5b08a53a54081823d758e3b7d11993bb5755019f49eabd1477044ad9fe3',
        'operatorPwd':'',
        'validcode':''
    }

    print('用户ID：' + id)
    data = urllib.parse.urlencode(data).encode(encoding='utf-8')
    req = urllib.request.Request(url=url,data=data)
    response = urllib.request.urlopen(req).read()
    #将response字符串转为字典
    reDic = eval(response)
    print('连接状况：' + reDic['result'])

#主程序
userId = input("请输入你的账号")
passWord = input("请输入你的密码")
login(pwd=passWord,id=userId)
while 1:
    print('程序正在运行，检测网络状况')
    return1 = os.system('ping baidu.com')
    if return1:
        print('断线，尝试重连')
        login(id=userId, pwd=passWord)
    else:
        #logout()
        print('----连接正常')




