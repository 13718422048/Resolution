#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020��3��16��

@author: cmck
'''

import importlib
#from operamodels import *

class ManageFactory(object):
    # 专辑、歌手、评论、动态、歌单、电台、节目、歌曲、用户、关系
    models = ["album", "artist", "comment", "event", "playlist", "radio", "program", "song", "user", "relation"]
    
    def __init__(self, modelname):
        self.modelname = modelname
        # 动态加载类
        self._class = getattr(importlib.import_module("operamodels.operate" + self.modelname), "Operate" + self.modelname[0].upper() + self.modelname[1:])
        self.manager = self._class()
        
        print(self.manager.__class__.__name__ + " is created")
    
    # 如果模块名不对，则创建失败
    def __new__(cls, *args, **kwargs):
        if args[0] in cls.models:
            return super(ManageFactory, cls).__new__(cls)
        return None
    
    # 聚合查询
    def query(self, *args, **kwargs):
        return self.managerquery(*args, **kwargs)
    
    # 获取单个实体
    def getone(self, *args, **kwargs):
        return self.manager.getone(*args, **kwargs)
    
    # 获取实体列表
    def getlist(self, *args, **kwargs):
        return self.manager.getlist(*args, **kwargs)
    
    # 插入单个实体
    def insert(self, *args, **kwargs):
        return self.manager.insert(*args, **kwargs)
    
    # 判断实体是否存在
    def exists(self, *args, **kwargs):
        return self.manager.exists(*args, **kwargs)
    
    # 更新实体
    def update(self, *args, **kwargs):
        return self.manager.update(*args, **kwargs)
    
    # 获取某种实体的总数
    def totalnum(self, *args, **kwargs):
        return self.manager.totalnum(*args, **kwargs)
    
    # 删除某个实体
    def delete(self, *args, **kwargs):
        return self.manager.delete(*args, **kwargs)
    
    # 按条件删除满足的实体
    def deleteall(self, *args, **kwargs):
        return self.manager.deleteall(*args, **kwargs)
    
    
if __name__ == "__main__":
    
    modelname = "user"
    interface = ManageFactory(modelname)
    print(interface)
    