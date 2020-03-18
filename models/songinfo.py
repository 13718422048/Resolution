#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020��3��13��

@author: cmck
'''

from models.common import *


class Songinfo(Common):
    def __init__(self):
        # 歌曲id
        self.__songid = ""
        # 歌曲名
        self.__songname = ""
        # 歌词
        self.__lrc = ""
        # 歌手id
        self.__artistid = []
        # 歌曲url
        self.__songurl = ""
        
        self.__mvid = ""
        #所属专辑id
        self.__albumid = ""
        # 发行时间
        self.__publishtime = ""
        # 歌曲别名
        self.__alias = []
            
    @property
    def id(self):
        return self.__songid
    @id.setter
    def id(self, sid):
        self.__songid = sid
        
    @property
    def songname(self):
        return self.__songname
    @songname.setter
    def songname(self, sname):
        self.__songname = sname
    
    @property
    def lrc(self):
        return self.__lrc
    @lrc.setter
    def lrc(self, lrc):
        val = re.sub(r"\[[0-9]+:[0-9]+.[0-9]+\]","\n", lrc)
        self.__lrc = val.replace("\n\n", "\n")
        
    @property
    def artistid(self):
        return self.__artistid
    @artistid.setter
    def artistid(self, artistids):
        for artist in artistids:
            self.__artistid.append(artist["id"])
    
    @property
    def songurl(self):
        return self.__songurl
    @songurl.setter
    def songurl(self, sourl):
        self.__songurl = sourl
        
    @property
    def mvid(self):
        return self.__mvid
    @mvid.setter
    def mvid(self, mid):
        self.__mvid = mid
        
    @property
    def albumid(self):        return self.__albumid
    @albumid.setter
    def albumid(self, album):
        self.__albumid = album["id"]
    
    @property
    def publishtime(self):
        return self.__publishtime
    @publishtime.setter
    def publishtime(self, timestamp):
        self.__publishtime = timestamp[:10]
        
    @property
    def alias(self):
        return self.__alias
    @alias.setter
    def alias(self, alia):
        self.__alias.extend(alia)