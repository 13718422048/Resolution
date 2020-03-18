#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020��3��16��

@author: cmck
'''

from .commonfunc import OperaComfunc
from models.artistinfo import Artistinfo

class OperateArtist:
    def __init__(self):
        self.tablename = "artist"
        self.operator = OperaComfunc(self.tablename)
        self.idname = "artistid"
        
    # 聚合查询
    def query(self, *args, **kwargs):
        return self.operator.query(*args, **kwargs)    
    
    # 获取
    def getone(self, *args, **kwargs):
        id = args[0]
        return self.operator.getone(self.idname, id, self.tablename)
    
    def getlist(self, *args, **kwargs):
        strwhere = args[0]
        rets = self.operator.getlist(strwhere, self.tablename, **kwargs)
        
        for valedict in rets:
            entity = Artistinfo()
            entity.copy(valedict)
            yield entity
        
    def insert(self, *args, **kwargs):
        entity = kwargs.get("record", None)
        id = args[0]
        record = entity.getitems()
        return self.operator.insert(self.idname, id, self.tablename, record = record)
    
    def exists(self, *args, **kwargs):
        id = args[0]
        return self.operator.exists(self.idname, id, self.tablename)
    
    def update(self, *args, **kwargs):
        entity = kwargs.get("record", None)
        id = args[0]
        record = entity.getitems()
        return self.operator.update(self.idname, id, self.tablename, record = record)
    
    def totalnum(self, *args, **kwargs):
        strwhere = args[0]
        return self.operator.totalnum(self.tablename, strwhere)
    