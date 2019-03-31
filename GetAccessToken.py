#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Get the access_token of the API. The API key has already been destroyed.'

__author__ = 'Zheng Rachel'

import requests
import json

#此函数用于获取access_token，返回值为含access_token的字典
def get_access_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=5UySi1081b8XYAtpg1XoNZVx&client_secret=KaQprO5ZMfyxTxtIjAagmHijsculFefS'
    r = requests.get(host)
    hjson = json.loads(r.text)
    return hjson

if __name__=='__main__':
    print(get_access_token())



