# coding:utf-8
'''
Created on 2020��2��5��

@author: cmck
'''

import pymongo


class mongodb:
    instance = None
    def __init__(self, name, host, port, **kwargs):
        self.tablename = name
        self.client = pymongo.MongoClient(host, port, **kwargs)
    
    def chagetable(self, tablename):
        self.tablename = tablename
        
    #def __call__(self):
