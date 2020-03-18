#coding:utf-8

'''
Created on 2020年1月12日

@author: cmck
'''


import requests
import json 
from basecollect import BaseCollect
import hashlib
from models.relatetioninfo import Relatetioninfo

class Collectrelation(BaseCollect):
    def __init__(self, action = "follows"):
        BaseCollect.__init__(self, "relation")
        self.action = action
    
    def Collectfollows(self, uid, limit = 30, action = "follows"):
        
        """
        function 获取用户关注/粉丝列表
        limit 为每次请求的用户个数
        offset = 页数 * limit
        action为表示获取的关注（follows）还是粉丝(followeds)
        """
        offset = 0
        iter = 0
        ismore = True
        
        while ismore:
            try:
                url = "http://localhost:3000/user/{0}?uid={1}&offset={2}&limit={3}".format(action, uid, offset, limit)
                rettext = self.GetRespText(url)
                
                if rettext is not None:
                    try:
                        followsdict = json.loads(rettext)
                        
                        # 翻页
                        ismore = followsdict["more"]
                        iter += 1
                        offset = iter * limit
                        
                        action = "follow" if action == "follows" else action
                        followls = followsdict[action]
                        
                        if len(followls) > 0:
                            for follow in followls:
                                yield follow["userId"]
                                
                    except Exception:
                        #TODO: 
                        pass
                    
            except Exception:
                #TODO: 
                pass
    
    def Savefollow(self, auid, buid):
        """
        function: 存储用户关系
        1. 确认关系是否已经存在
        2. 如果存在，则不做任何操作
        3. 如果不存在，则添加
        """
        # relatid = hashlib.md5((auid + buid).encodin("utf-8")).hexdigest()
        # relation = {"relatid": relatid, "startpoint": auid, "endpoint": buid}
        relatinfo = Relatetioninfo()
        relatinfo.arrow = buid
        relatinfo.tail = auid
        relatinfo.rtype = "follw"
        return self.manager.insert(relatinfo)
    
    '''def Exist(self, relatid):
        """
        function: 辨识用户关系是否存在
        paras:
        return:
        """
        return self.manager.exists(relatid)'''
        
        
    '''def Proceraletion(self, uid, neibhunum = 0, action = "follows", limit = 20):
        """
        function: 获取用户的粉丝和关注者
        """
        
        if neibhunum != 0:
            page = neibhunum / limit + (1 if neibhunum % limit != 0 else 0)
            for i in range(page):
                offset = i * limit
                for buid in self.Collectfollows(uid, limit, offset, action):                
                    if action == "follows":
                        self.Savefollow(buid, uid)
                    else:# action = "followeds"
                        self.Savefollow(uid, buid)
                    
                    yield buid
        
        else:
            return '''
        


if __name__ == "__main__":
    pass