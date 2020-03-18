#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2020��3��13��

@author: cmck
'''

from models.common import *

class Event(Common):
    
    eventtypedict = {41: "分享视频", 18: "分享单曲", 0: "分享评论", 17: "分享节目", 13: "分享歌单", 22: "转发动态", 4: "分享歌单", 19: "分享专辑", 6: "分享mv", 7: "发布mv", 35: "动态"}
    resourcetype = {41: "video", 18: "song", 13: "playlist", 22: "event", 19:"album", 17: "program"}
    
    def __init__(self):
        # 动态id
        self.__eventid = ""
        # 动态时间
        self.__eventtime = ""
        # 活动名
        self.__actname = ""
        # 作者id
        self.__userid = ""
        # 动态类型
        self.__type = ""
        # 动态说说
        self.__msg = ""
        # 动态中的图片
        self.__picture = []        
        # 转发资源的id（mv、playlist）
        self.__resouceid = ""        
        # 活动id
        self.__actid = ""        
        # 评论id
        self.__threadid = ""
        # uuid
        self.__uuid = ""
        
    @property
    def uuid(self):
        return self.__uuid
    @uuid.setter
    def uuid(self, uuid):
        self.__uuid = uuid    
        
    @property
    def eventid(self):
        return self.__eventid
    @eventid.setter
    def eventid(self, eid):
        if str(eid).isdigit is False:
            self.__eventid = str(eid)
        else:
            raise ValueError("eventid is error, not digit")
        
    @property
    def eventtime(self):
        return self.__eventtime
    @eventtime.setter
    def eventtime(self, timestamp):
        if str(timestamp).isdigit is False:
            self.__eventtime = str(timestamp)[:10]
            
        else:
            raise ValueError("eventtime is error, not digit")
        
    @property
    def actname(self):
        return self.__actname
    @actname.setter
    def actname(self, actionname):
        self.__actname = actionname
        
    @property
    def userid(self):
        return self.__userid
    @userid.setter
    def userid(self, authorid):
        self.__userid = authorid
    
    def gettypename(self):
        """
        function: 获取动态类型
        """
        typename = self.eventtypedict.get(int(self.__type), None)
        if typename is None:
            typename = ""
            raise ValueError("{0} isn't in [{1}]".format(self.__type, ",".join(x for x in self.eventtypedict.values())))
        
    @property
    def eventtype(self):
        return self.__type
    @eventtype.setter
    def eventtype(self, etype):
        if str(etype).isdigit is not False:
            self.__type = etype
        else:
            ValueError("{0} isn't digit!".format(etype))
            
    @property
    def msg(self):
        return self.__msg
    @msg.setter
    def msg(self, message):
        self.__msg = message
        
    @property
    def picture(self):
        return self.__picture
    @picture.setter
    def picture(self, piclst):
        if isinstance(piclst, list):
            self.__picture.extend(piclst)
            # 去重
            self.__picture = copy.deepcopy(list(set(self.__picture)))
        
    @property
    def resouceid(self):
        return self.__resouceid
    @resouceid.setter
    def resouceid(self, resid):
        self.__resouceid = resid
            
    @property
    def actid(self):
        return self.__actid
    @actid.setter
    def actid(self, actionid):
        self.__actId = actionid        
    
    @property
    def threadid(self):
        return self.__threadid
    @threadid.setter
    def threadid(self, thrid):
        self.__threadid = thrid

