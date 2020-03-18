#coding:utf-8

'''
Created on 2020年1月25日

@author: cmck
'''

import requests
import json
import copy
from models.artistinfo import *
from basecollect import BaseCollect


artistcat = {
    5001: "入驻歌手",
    1001: "华语男歌手",
    1002: "华语女歌手",
    1003: "华语组合/乐队",
    2001: "欧美男歌手",
    2002: "欧美女歌手",
    2003: "欧美组合/乐队",
    6001: "日本男歌手",
    6002: "日本女歌手",
    6003: "日本组合/乐队",
    7001: "韩国男歌手",
    7002: "韩国女歌手",
    7003: "韩国组合/乐队",
    4001: "其他男歌手",
    4002: "其他女歌手",
    4003: "其他组合/乐队"
}

class CollectArtist(BaseCollect):
    def __init__(self):
        BaseCollect.__init__(self, "artist")
    
    def ExtractArtists(self, cateid = 1001):
        ismore = True
        limit = 30
        offset = 0
        
        while ismore:
            url = "http://localhost:3000/artist/list?cat={0}&limit={1}&offset={2}".format(cateid, limit, offset)
            rettext = self.GetRespText(url)

            if rettext is not None:
                try:
                    ret = json.loads(rettext)
                    ismore = ret["more"]
                    
                    for artist in ret["artists"]:
                        try:
                            artistinfo = Artistinfo()
                            artistinfo.id = artist["id"]
                            artistinfo.artistname = artist["name"]
                            artistinfo.musicsize = artist["musicSize"]
                            artistinfo.albumsize = artist["albumSize"]
                            artistinfo.briefdesc = artist["briefDesc"]
                            artistinfo.alias = artist["alias"]
                            artistinfo.accountid = artist["accountId"]
                            
                            yield artistinfo
                            
                        except Exception:
                            # TODO: 获取赋值错误，并将错误内容记录下来
                            continue
                        # artistinfo.topicdata = artist["accountId"]
                        
                except Exception:
                    #TODO: 错误日志
                    ismore = False
            else:
                ismore = False
    
    def ExtractArtistdetail(self, artistinfo, proxy):

        url = "http://localhost:3000//artist/desc?id={0}".format(artistinfo.artistid)
        rettext = self.GetRespText(url)

        if rettext is not None:
            ret = json.loads(rettext)
            artistinfo.briefdesc = ret["briefDesc"]
            artistinfo.introduction = ret["introduction"]
            artistinfo.topicdata = ret["topicData"]
            
    def SaveArtists(self, artistinfo):
        return self.manager.insert(artistinfo)


if __name__ == "__main__":
    pass