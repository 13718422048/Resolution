#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020��3��16��

@author: cmck
'''

from util.mongodbclient import CMongodbclient
import copy

class OperaComfunc():
    def __init__(self, tablename):
        self.client = CMongodbclient(tabname = tablename)
        pass
    
    def getone(self, *args, **kwargs):
        idname = args[0]
        idval = args[1]
        tabname = args[2]
        
        strwhere = {idname: idval}
        self.client.changetable(tabname)
        ret = self.client.get(strwhere, action = "one")
        
        if len(ret) == 1:
            return ret[0]
        
        return None
    
    def query(self, *args, **kwargs):
        pass
    
    def getlist(self, *args, **kwargs):
        
        strwhere = args[0]
        tabname = args[1]
        
        limit = kwargs.get("limit", None)
        skip = kwargs.get("skip", None)
        action = "all"
        
        if limit is None or skip is None:
            limit = 100
            skip = 0
            
        self.client.changetable(tabname)
        return self.client.get(strwhere, action, limit, skip)
    
    def exists(self, *args, **kwargs):
        flag = 0
        idname = args[0]
        idval = args[1]
        tabname = args[2]
        ret = self.getone(idname, idval, tabname)
        
        if ret is None:
            flag = 0
        else:
            flag = 1
            
        return flag                
    
    def insert(self, *args, **kwargs):
        idname = args[0]
        idval = args[1]
        tabname = args[2]
        record = kwargs.get("record", None)
        if record is None:
            return None
        ret = ""
        
        if not self.exists(idname, idval, tabname):
            self.client.changetable(tabname)
            ret = self.client.put(record)
        
        return ret
    
    def update(self, *args, **kwargs):
        idname = args[0]
        idval = args[1]
        tabname = args[2]
        cc = kwargs.get("record", None)
        if cc is None:
            return None
        
        ret = ""
        if not self.exists(idname, idval, tabname):
            record = copy.deepcopy(cc)
            del record[idname]
            
            strwhere = {idname, idval}
            newval = {"$set": record}
            self.client.changetable(tabname)
            ret = self.client.put(strwhere, newval)
        
        return ret
    
    def totalnum(self, *args, **kwargs):        
        tabname = args[0]
        strwhere = args[1]
        self.client.changetable(tabname)
        self.client.getTotal(strwhere)
        
        
    def delete(self, *args, **kwargs):
        idname = args[0]
        idval = args[1]
        tabname = args[2]
        
        strwhere = {idname: idval}
        self.deleteall(tabname, strwhere)
        
    def deleteall(self, *args, **kwargs):
        tabname = args[1]
        strwhere = args[0]
        
        self.client.changetable(tabname)
        ret = self.client.delete(strwhere)
        
        return ret
        
        
        
        