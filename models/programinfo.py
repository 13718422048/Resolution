#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020��3��17��

@author: cmck
'''

from models.common import *

class Programinfo(Common):
    def __init__(self):
        # 主题歌id
        self.__mainsongid = ""
        # 作者id
        self.__djid = ""
        # 节目时长
        self.__duration = ""
        # 播放次数
        self.__listenernum = ""
        # 评论id
        self.__commentthreadid = ""
        # 节目描述
        self.__description = ""
        # 节目创建时间
        self.__createtime = ""
        # 节目名称
        self.__programname = ""
        # 节目id
        self.__programid = ""
        # 分享次数
        self.__sharenum = 0
        # 点赞人数
        self.__likenum = 0
        # 评论总数
        self.__commentnum = 0
        
        # 电台id
        self.__radioid = ""
        
    def __str__(self):
        return json.dumps(self.getitems(), ensure_ascii = False)
    
    @property
    def radioid(self):
        return self.__radioid
    @radioid.setter
    def radioid(self, rid):
        self.__radioid = rid
        
    @property
    def mainsongid(self):
        return self.__mainsongid
    @mainsongid.setter
    def mainsongid(self, songid):
        self.__mainsongid = songid
    
    @property
    def djid(self):
        return self.__djid
    @djid.setter
    def djid(self, userid):
        self.__djid = userid
        
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = duration
        
    @property
    def listenernum(self):
        return self.__listenernum
    @listenernum.setter
    def listenernum(self, lisnum):
        self.__listenernum = lisnum
        
    @property
    def commentthreadid(self):
        return self.__commentthreadid
    @commentthreadid.setter
    def commentthreadid(self, comadid):
        self.__commentthreadid = comadid
    
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, desc):
        self.__description = desc
        
    @property
    def createtime(self):
        return self.__createtime
    @createtime.setter
    def createtime(self, timestamp):
        self.__createtime = timestamp[:10]
        
    @property
    def name(self):
        return self.__programname
    @name.setter
    def name(self, name):
        self.__programname = name
        
    @property
    def id(self):
        return self.__programid
    @id.setter
    def id(self, pid):
        self.__programid = pid
        
    @property
    def sharenum(self):
        return self.__sharenum
    @sharenum.setter
    def sharenum(self, snum):
        self.__sharenum = self.validatenum(snum)
        
    @property
    def likenum(self):
        return self.__likenum
    @likenum.setter
    def likenum(self, lnum):
        self.__likenum = self.validatenum(lnum)
        
    @property
    def commentnum(self):
        return self.__commentnum
    @commentnum.setter
    def commentnum(self, commnum):
        self.__commentnum = self.validatenum(commnum)
        