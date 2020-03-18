#coding:utf-8

'''
Created on 2020年3月13日

@author: cmck
'''

from models.common import *


class Albuminfo(Common):
    def __init__(self):
        
        # 专辑id
        self.__albumid = ""
        # 专辑别名
        self.__alias = []
        # 歌手id
        self.__artistids = []
        # 专辑简介
        self.__briefdesc = ""
        # 专辑出版时间
        self.__publishtime = ""
        # 专辑发行公司
        self.__company = ""
        # 评论id
        self.__commentthreadid = ""
        # 专辑类型
        self.__subtype = ""
        # 专辑介绍
        self.__description = ""
        # 专辑名
        self.__albumname = ""
        # 类型
        self.__type = ""
        # 评论数量
        self.__commentnum = 0
        # 分享数量
        self.__sharenum = 0
        # 点赞数量
        self.__likenum = 0
        # 歌曲id, 将专辑与歌曲的关系单独存放表
        #self.__songids = []
    
    def copy(self, valdict):
        pass
    
    def __str__(self):
        #return json.dumps(super(Albuminfo, self).getitems())
        return json.dumps(self.getitems(), ensure_ascii = False)
        
    @property
    def alias(self):
        return self.__alias
    @alias.setter
    def alias(self, als):
        if isinstance(als, list):
            self.__alias.extend(als)
            self.__alias = copy.deepcopy(list(set(self.__alias)))
            
        else:
            raise ValueError("")
        
    @property
    def artistids(self):
        return self.__artistids
    @artistids.setter
    def artistids(self, arts):
        if isinstance(arts, list):
            for artor in arts:
                self.__artistids.append(artor["id"])
                
        else:
            raise ValueError("")
        
    @property
    def briefdesc(self):
        return self.__briefdesc
    @briefdesc.setter
    def briefdesc(self, bdesc):
        self.__briefdesc = bdesc
        
    @property
    def publishtime(self):
        return self.__publishtime
    @publishtime.setter
    def publishtime(self, timestamp):
        self.__publishtime = str(timestamp)[:10]
        
    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self, cmpy):
        self.__company = cmpy
        
    @property
    def commentthreadid(self):
        return self.__commentthreadid
    @commentthreadid.setter
    def commentthreadid(self, commid):
        self.__commentthreadid = commid
        
    @property
    def subtype(self):
        return self.__subtype
    @subtype.setter
    def subtype(self, sbtype):
        self.__subtype = sbtype
        
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, desc):
        self.__description = desc
        
    @property
    def albumname(self):
        return self.__albumname
    @albumname.setter
    def albumname(self, albname):
        self.__albumname = albname
        
    @property
    def id(self):
        return self.__albumid
    @id.setter
    def id(self, albid):
        self.__albumid = albid
    
    @property
    def albumtype(self):
        return self.__type
    @albumtype.setter
    def albumtype(self, albtype):
        self.__type = albtype
    
    @property
    def commentnum(self):
        return self.__commentnum
    @commentnum.setter
    def commentnum(self, commnum):
        self.__commentnum = commnum
    
    @property
    def sharenum(self):
        return self.__sharenum
    @sharenum.setter
    def sharenum(self, shanum):
        self.__sharenum = shanum
        
    @property
    def likenum(self):
        return self.__likenum
    @likenum.setter
    def likenum(self, lknum):
        
        self.__likenum = lknum
        
    
    '''@property
    def songids(self):
        return self.__songids
    @songids.setter
    def songids(self, songls):
        if isinstance(songls, list):
            for song in songls:
                self.__songids.append(song["id"])
    
        else:
            raise ValueError("song's id is error")'''
    