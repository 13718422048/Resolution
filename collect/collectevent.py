#coding:utf-8
'''
Created on 2020年1月18日

@author: cmck
'''

import requests
import json
import copy

from models.eventinfo import *
from basecollect import BaseCollect

class CollectEvent(BaseCollect):

    

    def __init__(self):
        BaseCollect.__init__(self, "event")
    
    def ExtractEvent(self, uid, limit = 30):
        # 下一页的时间
        lasttime = -1 
        nextpage = True
        
        eventtypedict = Event.eventtypedict
        resourcetype = Event.resourcetype
        
        while nextpage:
            # 修改了接口的参数名，将lasttime替换为timestamp
            #url = "http://localhost:3000/user/event?uid={0}&limit={1}&lasttime={2}".format(uid, limit, lasttime)
            url = "http://localhost:3000/user/event?uid={0}&limit={1}&timestamp={2}".format(uid, limit, lasttime)
            rettext = self.GetRespText(url)
            
            if rettext is not None:
                try:
                    ret = json.loads(rettext)
                    lasttime = ret["lasttime"]
                    events = ret["events"]
                    nextpage = ret["more"]
                
                except Exception:
                    nextpage = False
                    continue
                    
                for event in events:
                    try:
                        evententity = Event()
                        evententity.eventid = event["id"]
                        evententity.eventtime = event["eventTime"][:10]       
                        evententity.actname = event["actName"]
                        evententity.userid = event["user"]["userId"]          
                        evententity.picture = event["pics"]
                        evententity.actid = event["actId"]
                        message = json.dumps(event["json"])
                        evententity.msg = message["msg"]
                        evententity.threadid = event["info"]["threadId"]
                        evententity.uuid = event["uuid"]
                        
                        typeid = event["type"]
                        evententity.eventtype = typeid
                        
                        # 扩充动态列表
                        try:
                            resoucetitle = event["info"]["commentThread"].get("resourceTitle", None)
                            if resoucetitle is not None:
                                typename = resoucetitle[:resoucetitle.find(":") + 1]
                                
                                if typeid not in eventtypedict.keys() and typename not in eventtypedict.values():
                                    eventtypedict[typeid] = typename
                                    # TODO: 输出eventtypedict所有值
                            
                        except Exception:
                            # TODO: 出现异常，日志记录
                            pass
                        
                        # 扩充资源类型列表
                        try:
                            for key in message.keys():
                                if key != "msg" and resourcetype.get(typeid, None) is None and isinstance(message[key], dict):
                                    self.resourcetype[typeid] = key
                                    # TODO: 输入当前resourcetype的所有值
                                
                        except Exception:
                            # TODO: 出现异常，日志记录
                            pass
                    
                        # 获取资源id
                        resourceid = -1
                        if len(message.keys()) >= 2:
                            residname = "id"
                            
                            """
                            excptype = ["comment", "video"]
                            对于"comment", "video"两种类型，id字段名为commentId或videoId
                            """
                            
                            try:
                                resourceid = message[resourcetype[typeid]].get(residname, None)
                                if resourceid is None:
                                    residname = resourcetype[typeid] + "Id"
                                    resourceid = message[resourcetype[typeid]].get(residname, None)
                                    if resourceid is None:
                                        resourceid = -1
                                        # TODO: 出现异常，日志记录
                                        pass
                            except Exception:
                                # TODO: 出现异常，日志记录
                                resourceid = -1
                                pass
                        
                        evententity.resouceid = resourceid
                        
                        yield evententity
                    except Exception:
                        # TODO: 出现异常，日志记录，记录出现错误的数据
                        continue 
            else:
                nextpage = False
    
    # 存储动态
    def SaveEvent(self, event):
        return self.manager.insert(event)
    
    
    def ColloctEvent(self, uid):
        """
        function: 获取一个用户所有动态
        """
        limit = 30
        
        for event in self.ExtractEvent(uid, limit):
            self.SaveEvent(event)
            
if __name__ == "__main__":
    pass
