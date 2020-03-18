#coding:utf-8

'''
Created on 2020年1月9日
function: 收集用户信息，并将用户信息保存至数据库中
@author: cmck
'''

from models.userinfo import *
from basecollect import BaseCollect

class CollectUser(BaseCollect):
    
    def __init__(self):
        BaseCollect.__init__(self, "user")
    
    # 提取用户信息
    def ExtractUser(self, uid):
        
        url = "http://localhost:3000/user/detail?uid={0}".format(uid)
        rettext = self.GetRespText(url)
        
        if rettext is not None:
            try:
                clouduser = json.loads(rettext)
                info = Userinfo()
                
                info.userid = clouduser["userPoint"]["userId"]
                info.level = clouduser["level"]
                info.viptype = clouduser["profile"]["vipType"]
                info.province = clouduser["profile"]["province"]
                info.city = clouduser["profile"]["city"]
                info.birthday = clouduser["profile"]["birthday"]
                info.gender = clouduser["profile"]["gender"]
                info.signature = clouduser["profile"]["signature"]
                info.nickname = clouduser["profile"]["nickname"]
                info.createtime = clouduser["profile"]["createTime"]
                info.detailDescription = clouduser["profile"]["detailDescription"]
                info.expertTags = clouduser["profile"]["expertTags"]
                info.bindsocity = clouduser["bindings"]
                info.followednum = clouduser["profile"]["followeds"]
                info.followsnum = clouduser["profile"]["follows"]
                
                self.SaveUser(info)
                return info
            except Exception:
                #TODO: 日志
                pass
    
    def SaveUser(self, userinfo):
        return self.manager.insert(userinfo)

        
if __name__ == "__main__":
    pass