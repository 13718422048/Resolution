#coding: utf-8
'''
Created on 2020��1��24��

@author: cmck
'''

import requests 
import json
from models.radioinfo import *
from models.programinfo import *
from basecollect import BaseCollect
from operamodels.managefactory import ManageFactory

class CollectRadio(BaseCollect):
    
    def __init(self):
        BaseCollect.__init__(self, "radio")
        self.managerprogram = ManageFactory("program")

    def ExtractRadio(self, uid):
        url = "http://localhost:3000/user/audio?uid={0}".format(uid)
        rettext = self.GetRespText(url)
        
        if rettext is not None:
            try:
                radios = json.loads(rettext)
                
                for radio in radios:
                    radioinfo = Radioinfo()
                    
                    radioinfo.category = radio["category"]
                    radioinfo.description = radio["desc"]
                    radioinfo.createtime = radio["createTime"]
                    radioinfo.categoryid = radio["categoryId"]
                    radioinfo.subcount = radio["subCount"]
                    radioinfo.programcount = radio["programCount"]
                    radioinfo.radioname = radio["name"]
                    radioinfo.radioid = radio["id"]
                    radioinfo.rcmdtext = radio["rcmdtext"]
                    radioinfo.djid = uid
                    
                    yield radioinfo
            
            except Exception:
                pass
                # TODO: 
                
    def ExtractProgram(self, rid):
        ismore = True
        limit = 30
        offset = 0
        iter = 0
        
        while ismore:
            url = "http://localhost:3000/dj/program?rid={0}&offset={1}&limit={2}".format(rid, offset, limit)
            rettext = self.GetRespText(url)
            if rettext is not None:
                programdict = {}
                try:
                    programdict = json.loads(rettext)
                    ismore = programdict["more"]
                    iter += 1
                    offset = iter * limit
                    
                except Exception:
                    ismore = False
                    continue
                
                for program in programdict["programs"]:
                    try:
                        programinfo = Programinfo()
                        programinfo.mainsongid = program["mainSong"]["id"]
                        programinfo.djid = program["dj"]["userId"]
                        programinfo.duration = program["duration"]
                        programinfo.listenernum = program["listenerCount"]
                        programinfo.commentthreadid = program["commentThreadId"]
                        programinfo.description = program["description"]
                        programinfo.createtime = program["createTime"]
                        programinfo.name = program["name"]
                        programinfo.id = program["id"]
                        programinfo.sharenum = program["shareCount"]
                        programinfo.likenum = program["likeCount"]
                        programinfo.commentnum = program["commentCount"]
                        programinfo.radioid = rid 
                    
                        self.SaveProgram(programinfo)
                    except Exception:
                        # TODO: 
                        pass
            
            ismore = False
            
    def SaveRadio(self, radioinfo):
        return self.manager.insert(radioinfo)
    
    def SaveProgram(self, programinfo):
        return self.managerprogram.insert(programinfo)
    
    def run(self, uid):
        
        for radioinfo in self.ExtractRadio(uid):
            self.SaveRadio(radioinfo)
            self.ExtractProgram(radioinfo.radioid)
    
if __name__ == "__main__":
    pass



