'''
Created on 2020年1月24日

@author: cmck
'''

import requests
import json

from models.playlistinfo import *
from basecollect import BaseCollect

class CollectPlaylist(BaseCollect):
    def __init__(self):
        BaseCollect.__init__(self, "event")
        self.limit = 30
    
    # 抽取歌单信息
    def ExtractPlaylist(self, uid, limit = 30, offset = 0):
        ismore = True
        iter = 0
        
        while ismore:
            url = "http://localhost:3000/user/playlist?uid={0}&limit={1}&offset={2}".format(uid, limit, offset)
            rettext = self.GetRespText(url)
            if rettext is not None:
                try:
                    ret = json.loads(rettext)
                    
                    ismore = ret["more"]
                    iter += 1
                    offset = limit * iter
                except Exception:
                    ismore = False                  
                
                for playlist in ret["playlist"]:
                    try:
                        playlistinfo = PlaylistInfo()
                        playlistinfo.createtime = playlist["createTime"]
                        playlistinfo.userid = playlist["userId"]
                        playlistinfo.trackcount = playlist["trackCount"]
                        playlistinfo.subscribecount = playlist["subscribeCount"]
                        playlistinfo.description = playlist["description"]
                        playlistinfo.name = playlist["name"]
                        playlistinfo.id = playlist["id"]
                        playlistinfo.speialtype = playlist["speialType"]
                        playlistinfo.tags = playlist["tags"]
                        playlistinfo.commentthreadid = playlist["commentThreadId"]
                        playlistinfo.playcount = playlist["playCount"]
                        
                        yield playlistinfo
                    except Exception:
                        #TODO: 
                        pass
                    
            ismore = False        
    
    def SavePlaylist(self, playlist):
        """
        function: 存储歌单信息、歌曲列表、订阅者
        """
        # 歌曲列表和订阅者分别另存在其他表中。罗列歌曲和订阅者存放，考虑下是逐条存放，还是分批次存放
        ret = 0
        try:
            # TODO: 重做关系
            songs =  self.Extractsongs(playlist.playlistid)
            subscribers = self.Extractsubscribers(playlist.playlistid, 30)
            
            # 存放歌单信息
            ret = self.manager.insert(playlist, songls = songs, subscri = subscribers)
            
        except Exception:
            pass
        
        return ret
    
    # 获取歌曲列表
    def Extractsongs(self, playlistid):
        
        url = "http://localhost:3000/playlist/detail?id={0}".format(playlistid)
        rettext = self.GetRespText(url)
        
        if rettext is not None:
            try:
                detail = json.loads(rettext)
                # playlistinfo.tracks启用的情况下
                # playlistinfo.tracks = detail["trackIds"]
                for track in detail["trackIds"]:
                    yield track["id"]
            except Exception:
                # TODO:
                return
            
    # 获取所有订阅者
    def Extractsubscribers(self, playlistid, limit = 30, offset = 0):
        
        ismore = True
        iter = 0
        
        while ismore:
            url = "http://localhost:3000/playlist/subscribers?id={0}&limit={1}&offset={2}".format(playlistid, limit, offset)
            rettext = self.GetRespText(url)
            
            if rettext is not None:
                try:
                    ret = json.loads(rettext)
                    ismore = ret["more"]
                    iter += 1
                    offset = iter * limit
                    
                    # playlistinfo.subscribers启用的情况下
                    # playlistinfo.subscribers = ret["subscribers"]
                    for subscriber in ret["subscribers"]:
                        yield subscriber["userId"]
                        
                    continue
                
                except Exception:
                    #TODO:
                    pass
                
            ismore = False        
                    
    def run(self, uid):
        
        offset = 0
        for playlistinfo in self.ExtractPlaylist(uid, self.limit, offset):
            self.SavePlaylist(playlistinfo)
    
if __name__ == "__main__":
    pass


