#coding:utf-8
'''
Created on 2020年1月26日

@author: cmck
'''

import requests
import copy
from models.albuminfo import *
from models.relationinfo import Relationinfo
from operamodels.managefactory import ManageFactory

from basecollect import BaseCollect

class CollectAlbum(BaseCollect):
    def __init__(self):
        BaseCollect.__init__(self, "album")
    
    def Extractalbum(self, albumid):
        
        try:
            url = "http://localhost:3000/album?id={0}".format(id)
            rettext = self.GetRespText(url)
            
            if rettext is not None:
                relationmanager = ManageFactory("relation")
                 
                ret = json.loads(rettext)
                albuminfo = Albuminfo()
                
                for song in ret["songs"]:
                    relatetioninfo = Relationinfo()
                    relatetioninfo.tail = albumid
                    relatetioninfo.songids = song["id"]
                    relatetioninfo.rtype = "contains"
                    relationmanager.insert(relatetioninfo)
                
                albuminfo.id = ["album"]["id"]
                albuminfo.alias = ret["album"]["alias"]
                albuminfo.artistids = ret["album"]["artistids"]
                albuminfo.briefdesc = ret["album"]["briefDesc"]
                albuminfo.publishtime = ret["album"]["publishTime"]
                albuminfo.company = ret["album"]["company"]
                albuminfo.commentthreadid = ret["album"]["commentThreadId"]
                albuminfo.subtype = ret["album"]["subType"]
                albuminfo.description = ret["album"]["description"]
                albuminfo.albumname = ret["album"]["name"]
                albuminfo.type = ret["album"]["type"]
                albuminfo.commentnum = ret["album"]["info"]["commentCount"]
                albuminfo.sharenum = ret["album"]["info"]["shareCount"]
                albuminfo.likenum = ret["album"]["info"]["likedCount"]
                
                self.SaveAlbum(albuminfo)
            
        except Exception:
            #TODO: 错误日志
            pass
                
    def SaveAlbum(self, albuminfo):
        return self.manager.insert(albuminfo)
    

if __name__ == "__main__":
    operaalbu = CollectAlbum()
    id = "32311"
    operaalbu.Extractalbum(id)