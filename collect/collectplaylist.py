'''
Created on 2020��1��24��

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
    
    # ��ȡ�赥��Ϣ
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
        function: �洢�赥��Ϣ�������б�������
        """
        # �����б�Ͷ����߷ֱ�������������С����и����Ͷ����ߴ�ţ���������������ţ����Ƿ����δ��
        ret = 0
        try:
            # TODO: ������ϵ
            songs =  self.Extractsongs(playlist.playlistid)
            subscribers = self.Extractsubscribers(playlist.playlistid, 30)
            
            # ��Ÿ赥��Ϣ
            ret = self.manager.insert(playlist, songls = songs, subscri = subscribers)
            
        except Exception:
            pass
        
        return ret
    
    # ��ȡ�����б�
    def Extractsongs(self, playlistid):
        
        url = "http://localhost:3000/playlist/detail?id={0}".format(playlistid)
        rettext = self.GetRespText(url)
        
        if rettext is not None:
            try:
                detail = json.loads(rettext)
                # playlistinfo.tracks���õ������
                # playlistinfo.tracks = detail["trackIds"]
                for track in detail["trackIds"]:
                    yield track["id"]
            except Exception:
                # TODO:
                return
            
    # ��ȡ���ж�����
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
                    
                    # playlistinfo.subscribers���õ������
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


