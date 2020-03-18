#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020年3月13日

@author: cmck
'''

from models.common import *


        
class Radioinfo(Common):
    def __init__(self):
        # 电台类别名称
        self.__category = ""
        # 电台简介
        self.__description = ""
        # 创建时间
        self.__createtime = ""
        # 电台类别id
        self.__categoryid = ""
        # 订阅总数
        self.__subcount = 0
        # 节目数量
        self.__programcount = 0
        # 电台名
        self.__radioname = ""
        # 电台id
        self.__radioid = ""
        # djid即用户id
        self.__djid = ""
        # 推荐理由
        self.rcmdtext = ""
        
    def __str__(self):
        return json.dumps(self.getitems(), ensure_ascii = False)
    
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, categoryname):
        self.__category = categoryname
        
    @property
    def description(self):
        return self.__desc
    @description.setter
    def description(self, desc):
        self.__description = desc
        
    @property
    def createtime(self):
        return self.__createtime
    @createtime.setter
    def createtime(self, timestamp):
        self.__createtime = str(timestamp)[:10]
        
    @property
    def categoryid(self):
        return self.__categoryid
    @categoryid.setter
    def categoryid(self, cateid):
        self.__categoryid = cateid
    
    @property
    def subcount(self):
        return self.__subcount
    @subcount.setter
    def subcount(self, subscribecount):
        self.__subcount = self.validatenum(subscribecount)
      
    @property
    def programcount(self):
        return self.__programcount
    @programcount.setter
    def programcount(self, prognum):
        self.__programcount = self.validatenum(prognum)
        
    @property
    def radioname(self):
        return self.__radioname
    @radioname.setter
    def radioname(self, name):
        self.__radioname = name
        
    @property
    def radioid(self):
        return self.__radioid
    @radioid.setter
    def radioid(self, rid):
        self.__radioid = rid

    @property
    def djid(self):
        return self.__djid
    @djid.setter
    def djid(self, djid):
        self.__djid = djid
        
    @property
    def rcmdtext(self):
        return self.__rcmdtext
    @rcmdtext.setter
    def rcmdtext(self, recommend):
        self.__rcmdtext = recommend
