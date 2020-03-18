#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020年3月17日

@author: cmck
'''
from models.common import *
import hashlib


class Relationinfo(Common):
    def __init__(self):
        
        # 关系id
        self.__id = ""
        # 关系终点
        self.__arrow = ""
        # 关系起点
        self.__tail = ""
        # 关系类型：follw(关注)、subscibe(歌单订阅)，quote(歌单引用歌曲)，contains（专辑包含）
        self.__rtype = ""
    
    @property
    def id(self):
        self.__id = hashlib.md5((self.__tail + self.__arrow).encode("utf-8")).hexdigest()
        return self.__id
    
    @property
    def arrow(self):
        return self.__arrow
    @arrow.setter
    def arrow(self, id):
        self.__arrow = id
        
    @property
    def tail(self):
        return self.__tail
    @tail.setter
    def tail(self, id):
        self.__tail = id
        
    @property
    def rtype(self):
        return self.__rtype
    @rtype.setter
    def rtype(self, rtype):
        self.__rtype = rtype
        
    
    