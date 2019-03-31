#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Send a sentence to the API, and send back the response.'

__author__ = 'Zheng Rachel'

import GetAccessToken
import requests
import json

#此函数用于向API发送请求，判断单句语句str0的情感倾向
def analyze_sentence(str0):
    url='https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token='
    headers={'Content-Type':'application/json'}
    url+=GetAccessToken.get_access_token()['access_token']
    d={}
    d['text']=str0
    d_js=json.dumps(d).encode('utf-8')
    r=requests.post(url,data=d_js,headers=headers)
    #返回内容为json格式的字符串，为方便后续处理，将返回结果转化为dict格式并返回
    r_dict=json.loads(r.text)
    return r_dict

if __name__=='__main__':
    print("请输入您想要分析的文字")
    str0=input()
    result=analyze_sentence(str0)
    print(result)
