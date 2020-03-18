#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020��3��13��

@author: cmck
'''

import requests
import json
from operamodels.managefactory import ManageFactory 

class BaseCollect(object):
    
    def __init__(self, modelname):
        self.retry = 3
        self.timeout = (4, 6)
        self.blackproxies = dict()
        self.manager = ManageFactory(modelname)
    
    def Exists(self, id):
        return self.manager.exists(id)
    
    # 获取代理
    def GetProxy(self):
        # proxy = {"proxyid":"", "ip":"", "port":"", "protocol":""}
        proxy = {}
        terminal = False
        while not terminal:
            try:
                req = requests.get("")
                if req.status_code == 200:
                    if req.text is not None:
                        proxy = json.loads(req.text)
                        # 获取的ip不在黑名单中
                        if self.blackproxies.get(proxy["proxyid"], None):
                            terminal = True
                            return proxy
            
            except Exception:
                continue
    
    def GetRespText(self, url):
        for i in range(self.retry):
            avlidproxy = self.GetProxy()
            req = None
            
            try:
                proxypar = "&proxy={0}://{1}:{2}".format(avlidproxy["protocol"], avlidproxy["ip"], avlidproxy["port"])
                req = requests.get(url + proxypar, timeout = self.timeout)
            
            except requests.exceptions.Timeout:
                # 代理连接超时，需要重换代理
                # 当前代理被标记为黑名单
                # 如果连接 self.retry次都出现错误，不用代理
                if self.blackproxies.get(avlidproxy["proxyid"], None) is None:
                    self.blackproxies[avlidproxy["proxyid"]] = avlidproxy
                    
                if i == self.retry - 1:
                    req = requests.get(url, timeout = self.timeout)
                    
                continue
                
            except requests.exceptions.RequestException:
                # 连接超时
                continue
            
            if req.status_code == 200:
                if req.text is not None:
                    return req.text
                
            return None 
            
            
            
            
            