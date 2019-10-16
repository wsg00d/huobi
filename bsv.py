#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
import json
step=1
i=0
for i in range(1,21):
    time.sleep(1)
    print i
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f2=open('/home/wangsong/huobi/bsvrun.txt','w+')
    f2.write(nowtime)
    f2.close()
    btcurl = "https://api.huobi.pro/market/history/kline?period=1min&size=1&symbol=bsvusdt"
    btcurl = requests.get(url=btcurl,timeout=5)
    btc=json.loads(btcurl.content)
    btcnew = btc['data'][0]['close']
    btcold=str(btc['data'][0]['open'])
    print btcnew
    print btcold
    if time.localtime().tm_hour !=0:
        f1=open('/home/wangsong/huobi/bsv_flag.txt','w')
        f1.write('1')
        f1.close()

    f1 = open('/home/wangsong/huobi/bsv_flag.txt', 'r')
    flag = int(f1.read())
    #print type(f1)

    if time.localtime().tm_hour == 0 and  flag ==1:
        f = open('/home/wangsong/huobi/bsv.txt', 'w')
        f.write(btcold)
        f.close()
        f1 = open('/home/wangsong/huobi/bsv_flag.txt', 'w')
        f1.write('0')
        f1.close()

    f = open('/home/wangsong/huobi/bsv.txt', 'r')
    btcold=float(f.read())
    f.close()

    rate=(btcnew-btcold)/btcold
    percent='percent: {:.2%}'.format(rate)
    print percent

    # if True:
    if rate>0.05 or rate <-0.05:
        content = 'bsv ' + ' ' + str(btcnew) + ' ' + str(percent)

        data = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            "at": {
                "isAtAll": True
            }
        }

        header = {
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        sendData = json.dumps(data)
        print sendData

        request = requests.post(
            url='https://oapi.dingtalk.com/robot/send?access_token=',
            data=sendData, headers=header)
        print request.content

        # if True:
    if rate>0.1 or rate <-0.1:
        content = 'bsv ' + ' ' + str(btcnew) + ' ' + str(percent)

        data = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            "at": {
                "isAtAll": True
            }
        }

        header = {
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        sendData = json.dumps(data)
        print sendData

        request = requests.post(
            url='https://oapi.dingtalk.com/robot/send?access_token=',
            data=sendData, headers=header)
        print request.content

