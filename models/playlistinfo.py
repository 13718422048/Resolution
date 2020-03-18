#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020��3��13��

@author: cmck
'''

from models.common import *


class PlaylistInfo(Common):
    def __init__(self):
        # 歌单创建时间
        self.__createtime = ""
        self.__updatetime = ""
        # 创建者id
        self.__userid = ""
        # 歌曲数量
        self.__trackcount = 0
        # 评论id
        self.__commentthreadid = ""
        # 播放次数
        self.__playcount = 0
        # 订阅数量
        self.__subscribecount = 0
        # 歌单简介
        self.__description = ""
        # 歌单名
        self.__playlistname = ""
        # 歌单id
        self.__playlistid = ""
        # 
        self.__speialtype = ""
        # 歌单标签
        self.__tags = []    
        
        # 数量太多，且不方便做检索，独立成其他内容
        # 歌单订阅者id
        #self.__subscribers = []
        # 歌曲id
        #self.__tracks = []
        
    @property
    def creattime(self):
        return self.__creattime
    @creattime.setter
    def creattime(self, timestamp):
        self.creattime = timestamp[:10]
        
    @property
    def updatetime(self):
        return self.__updatetime
    @updatetime.setter
    def updatetime(self, timestamp):
        self.__updatetime = timestamp[:10]
    
    @property
    def userid(self):
        return self.__userid
    @userid.setter
    def userid(self, uid):
        self.__userid = uid
        
    @property
    def trackcount(self):
        return self.__trackcount
    @trackcount.setter
    def trackcount(self, tracknum):
        self.__trackcount = self.validatenum(tracknum)
        
    @property
    def commentthreadid(self):
        return self.__commentthreadid
    @commentthreadid.setter
    def commentthreadid(self, threadid):
        self.__commentthreadid = threadid
    
    @property
    def playcount(self):
        return self.__playcount
    @playcount.setter
    def playcount(self, num):
        self.__playcount = self.validatenum(num)
        
    @property
    def subscribecount(self):
        return self.__subscribecount
    @subscribecount.setter
    def subscribecount(self, subnum):
        self.__subscribecount = self.validatenum(subnum)
        
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, desc):
        self.__description = desc 
        
    @property
    def name(self):
        return self.__playlistname
    @name.setter
    def name(self, name):
        self.__playlistname = name
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, playid):
        self.__id = playid
        
    @property
    def speialtype(self):
        return self.__speialtype
    @speialtype.setter
    def speialtype(self, specitype):
        self.__speialtype = specitype
        
    @property
    def tags(self):
        return self.__tags
    @tags.setter
    def tags(self, categories):
        if isinstance(categories, list):
            self.__tags.extend(categories)
            self.__tags = copy.deepcopy(list(set(self.__tags)))
        else:
            raise ValueError("tags must be list!")
        
        
        
        
        
        
    '''@property
    def subscribers(self):
        return self.__subscribers
    @subscribers.setter
    def subscribers(self, subscids):
        if isinstance(subscids, list):
            for user in subscids:
                if user["userId"] not in self.__subscribers:
                    self.__subscribers.append(user["userId"])
        else:
            raise ValueError("subscribers' id must be list!")
        
    @property
    def trackid(self):
        return self.__tracks
    @trackid.setter
    def trackid(self, songids):
        if isinstance(songids, list):
            for songid in songids:
                if songid["id"] not in self.__tracks:
                    self.__tracks.append(songid["id"])
        else:
            raise ValueError("songs' id must be list!")
'''