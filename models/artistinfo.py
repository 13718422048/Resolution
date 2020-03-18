#coding:utf-8
'''
Created on 2020年3月13日

@author: cmck
'''

from models.common import *

class Artistinfo(Common):
    def __init__(self):
        # 歌手id
        self.__artistid = ""
        # 歌手名
        self.__artistname = ""
        # 歌曲数量
        self.__musicsize = 0
        # 专辑数
        self.__albumsize = 0
        # 简介
        self.__briefdesc = ""
        # 别名
        self.__alias = []
        # TODO: 歌手账户主页？
        self.__accountid = ""
        # 话题
        self.__topicdata = []
        # 介绍
        self.__introduction = []
    
    def __str__(self):
        return json.dumps(self.getitems(), ensure_ascii = False)
    
    @property
    def id(self):
        return self.__artistid
    @id.setter
    def id(self, arid):
        self.__artistid = arid
        
    @property
    def artistname(self):
        return self.__artistname
    @artistname.setter
    def artistname(self, artname):
        self.__artistname = artname
        
    @property
    def musicsize(self):
        return self.__musicsize
    @musicsize.setter
    def musicsize(self, musize):
        self.__musicsize = self.validatenum(musize)
        
    @property
    def albumsize(self):
        return self.__albumsize
    @albumsize.setter
    def albumsize(self, albsize):
        self.__albumsize = self.validatenum(albsize)
    
    @property
    def briefdesc(self):
        return self.__briefdesc
    @briefdesc.setter
    def briefdesc(self, bidesc):
        self.__briefdesc = bidesc
        
    @property
    def alias(self):
        return self.__alias
    @alias.setter
    def alias(self, alis):
        self.__alias.extend(alis)
        
    @property
    def accountid(self):
        return self.__accountid
    @accountid.setter
    def accountid(self, accid):
        self.__accountid = accid
    
    @property
    def topicdata(self):
        return self.__topicdata
    @topicdata.setter
    def topicdata(self, topcdat):
        if isinstance(topcdat, list):
            for tpcd in topcdat:
                topicinfo = Topicinfo()
                
                topicinfo.topictid = tpcd["id"]
                topicinfo.topicname = tpcd["mainTitle"]
                topicinfo.sharecount = tpcd["shareCount"]
                topicinfo.commcount = tpcd["commentCount"]
                topicinfo.likecount = tpcd["likeCount"]
                topicinfo.category = tpcd["categoryName"]
                topicinfo.tags = tpcd["tags"]
                topicinfo.addtime = tpcd["addTime"]
                topicinfo.title = tpcd["title"]
                topicinfo.recmdcontent = tpcd["recndContent"]
                topicinfo.seriesid = tpcd["seriesid"]
                topicinfo.commentthreadid = tpcd["commentThreadId"]
                topicinfo.content = tpcd["topic"]["content"]
                topicinfo.authorid = tpcd["creator"]["userId"]
                
                self.__topicdata.append(topicinfo.getitems().copy())
    
    @property
    def introduction(self):
        return self.__introduction
    @introduction.setter
    def introduction(self, intrduce):
        self.__introduction.extend(intrduce)


class Topicinfo(Common):
    def __init__(self):
        # 话题id
        self.__topictid = ""
        # 话题名
        self.__topicname = ""
        # 分享数
        self.__sharecount = 0
        # 评论数
        self.__commcount = 0
        # 点赞数
        self.__likecount = 0
        # 话题类别
        self.__category = ""
        # 标签
        self.__tags = ""
        # 发表时间
        self.__addtime = ""
        # 话题副标题
        self.__title = ""
        # 推荐意见
        self.__recmdcontent = ""
        # ？
        self.__seriesid = ""
        # 评论id
        self.__commentthreadid = ""
        # 话题内容
        self.__content = ""
        # 作者id
        self.__authorid = ""
        
    @property
    def topictid(self):
        return self.__topictid
    @topictid.setter
    def topictid(self, topcid):
        self.__topictid = topcid
    
    @property
    def topicname(self):
        return self.__topicname
    @topicname.setter
    def topicname(self, topcname):
        self.__topicname = topcname
    
    @property
    def sharecount(self):
        return self.__sharecount
    @sharecount.setter
    def sharecount(self, num):
        self.__sharecount = self.validatenum(num)
        
    @property
    def commcount(self):
        return self.__commcount
    @commcount.setter
    def commcount(self, num):
        self.__commcount = self.validatenum(num)
    
    @property
    def likecount(self):
        return self.__likecount
    @likecount.setter
    def likecount(self, num):
        self.__likecount = self.validatenum(num)
    
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, cate):
        self.__category = cate
        
    @property
    def tags(self):
        self.__tags    
    @tags.setter
    def tags(self, tages):
        if isinstance(tages, list):
            self.__tags = ";".join(x for x in tages)
    
    @property
    def addtime(self):
        return self.__addtime
    @addtime.setter
    def addtime(self, timestamp):
        self.__addtime = timestamp[:10]
    
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, tit):
        self.__title = tit
    
    @property
    def recmdcontent(self):
        return self.__recmdcontent
    @recmdcontent.setter
    def recmdcontent(self, reccont):
        self.__recmdcontent = reccont
    
    @property
    def seriesid(self):
        return self.__seriesid
    @seriesid.setter
    def seriesid(self, srsid):
        self.__seriesid = srsid
    
    @property
    def commentthreadid(self):
        return self.__commentthreadid
    @commentthreadid.setter
    def commentthreadid(self, threadid):
        self.__commentthreadid = threadid
        
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, contents):
        for cc in contents:
            #TODO: 去掉html标签 
            self.__content += cc["content"]
            
    @property
    def authorid(self):
        return self.__authorid
    @authorid.setter
    def authorid(self, atuid):
        self.__authorid = atuid["creator"]["userId"]
        
        
    
        
    