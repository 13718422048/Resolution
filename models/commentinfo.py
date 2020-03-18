#coding:utf-8
'''
Created on 2020��3��13��

@author: cmck
'''

from models.common import Common


class Commentinfo(Common):
    
    resoucetype = ["event", "dj", "music", "album", "playlist", "mv", "video", "program"]
    
    def __init__(self):
        # 评论id
        self.__commentid = ""
        # 创建时间
        self.__createtime = ""
        # 评论内容
        self.__content = ""
        # 上级评论
        self.__parentcommentid = ""
        # 点赞数
        self.__likecount = 0
        # 评论者id
        self.__userid = ""
        # 是否为热门评论过
        self.__ishot = False
        # 被评论资源类型
        self.__resourcetype = ""
        # 被评论资源id、歌曲id、mvid、动态id等
        self.__resourceid = ""
    
    @property
    def commentid(self):
        return self.__commentid
    
    @commentid.setter
    def commentid(self, comid):
        self.__commentid = comid
        
    @property
    def createtime(self):
        return self.__createtime
    @createtime.setter
    def createtime(self, timestamp):
        self.__createtime = str(timestamp)[:10]
        
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, text):
        self.__content = text
        
    @property
    def parentcommentid(self):
        return self.__parentcommentid
    @parentcommentid.setter
    def parentcommentid(self, fatherid):
        self.__parentcommentid = fatherid
        
    @property
    def likecount(self):
        return self.__likecount
    @likecount.setter
    def likecount(self, num):
        self.__likecount = self.validatenum(num)
    
    @property
    def userid(self):
        return self.__userid
    @userid.setter
    def userid(self, uid):
        self.__userid = uid
        
    @property
    def ishot(self):
        return self.__ishot
    @ishot.setter
    def ishot(self, flag):
        self.__ishot = flag
    
    @property
    def resourcetype(self):
        return self.__resourcetype
    
    @resourcetype.setter
    def resourcetype(self, restype):
        self.__resourcetype = restype
        if restype not in self.resoucetype:
            self.resoucetype.append(restype)
    
    @property
    def resourceid(self):
        return self.__resourceid

    @resourceid.setter
    def resourceid(self, resid):
        self.__resourceid = resid

