#coding:utf-8
'''
Created on 2020年1月26日

@author: cmck
'''

import requests
import json
import requests_httpsproxy
from models.songinfo import *
from basecollect import BaseCollect
    
class CollectSong(BaseCollect):
    
    def __init__(self):
        BaseCollect.__init__(self, "song")
    
    def ExtractSonginfo(self, songid):
        url = "http://localhost:3000/song/detail?ids={0}".format(songid)
        rettext = self.GetRespText(url)
        if rettext is not None:
            try:
                song = json.loads(rettext)
                if len(song["songs"]) >= 1:
                    songinfo = Songinfo()
                    songinfo.songid = song["songs"][0]["id"]
                    songinfo.songname = song["songs"][0]["name"]
                    
                    songinfo.artistid = song["songs"][0]["ar"]
                    # 从其他地方获取 /song/url?id=33894312
                    songinfo.songurl = ""
                    # 歌词
                    songinfo.lrc = ""
                    
                    songinfo.mvid = song["songs"][0]["mv"]
                    songinfo.albumid = song["songs"][0]["al"]
                    songinfo.publishtime = song["songs"][0]["publishTime"]
                    songinfo.alias = song["songs"][0]["alia"]
                    
                    return songinfo
        
            except Exception:
                #TODO:
                pass
    
    def ExtractSongurl(self, songinfo):
        url = "http://localhost:3000/song/url?id={0}".format(songinfo.songid)
        rettext = self.GetRespText(url)
        if rettext is not None:
            try:
                song = json.loads(rettext)
                if len(song["data"]) >= 1:
                    songinfo.songurl = song["data"][0]["url"]
            except Exception:
                #TODO:
                pass
    
    def ExtractLyc(self, songinfo):
        url = "http://localhost:3000/lyric?id={0}".format(songinfo.songid)
        rettext = self.GetRespText(url)
        if rettext is not None:
            try:
                lyc = json.loads(rettext)
                songinfo.lrc = lyc["lrc"]["lyric"]
            except Exception:
                #TODO:
                pass
    
    def SaveSong(self, songinfo):
        return self.manager.insert(songinfo)
    
    def run(self, songid):
        songinfo = self.ExtractSonginfo(songid)
        if songinfo is not None:
            self.ExtractSongurl(songinfo)
            self.ExtractLyc(songinfo)
            return self.SaveSong(songinfo)
        
        # 表示无数据的情况
        return 0
    
    
if __name__ == "__main__":
    pass