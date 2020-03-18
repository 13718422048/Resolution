#coding:utf-8
'''
Created on 2020年1月25日

@author: cmck
'''
# coding: utf-8
import requests
import json
import copy
from models.commentinfo import *
from basecollect import BaseCollect
from operamodels.managefactory import ManageFactory

# 获取歌曲评论
# 获取专辑评论
# 获取歌单评论
# 获取mv评论
# 获取电台节目评论
# 获取视频评论
# 获取动态评论
# 



class CollectComment(BaseCollect):
    def __init__(self):
        BaseCollect.__init__(self, "comment")

    # 获取动态评论
    def Extractfromevent(self, eventid):
        limit = 30
        offset = 0
        ismore = True
        iter = 0
        hotidls = []
        
        while ismore:
            url = "http://localhost:3000/comment/event?threadId={0}&limit={1}&offset={2}".format(eventid, limit, offset)
            rettext = self.GetRespText(url)
            
            if rettext is not None:
                try:
                    ret = json.loads(rettext)
                    
                    ismore = ret["ismore"]
                    
                    if ret["total"] == 0 or ret["total"] == "0":
                        return
                    
                    # 只有获取第一页评论时才出现热评
                    if len(ret["hotcomments"]) > 0:
                        for hotcomment in ret["hotcomments"]:
                            hotidls.append(hotcomment["commentId"])
                            
                    for comment in ret["comments"]:
                        try:
                            commentinfo = Commentinfo()
                            commentinfo.commentid = comment["commentId"]
                            commentinfo.createtime = comment["time"]
                            commentinfo.content = comment["content"]
                            commentinfo.parentcommentid = comment["parentCommentId"]
                            commentinfo.likecount = comment["likeCount"]
                            commentinfo.userid = comment
                            commentinfo.ishot = commentinfo.commentid in hotidls
                            commentinfo.resourceid = eventid
                            commentinfo.resourcetype = "event"
                            
                            yield commentinfo
                        except Exception:
                            #TODO: 错误日志
                            continue
                    
                    iter += 1
                    offset = limit * iter
                except Exception:
                    #TODO:
                    ismore = False
            # 结束获取内容
            else:
                ismore = False
            
    # 获取电台节目、视频、歌曲等的评论        
    def Extractfromresouce(self, resid, action = "playlist"):
        """
        action = song、album、playlist、program、mv、vidio（视频），mv和视频的评论暂时不获取
        """
        
        limit = 30
        offset = 0
        ismore = True
        iters = 0
        hotidls = []
        
        while ismore:
            
            url = "http://localhost:3000/comment/{0}?id={1}&limit={2}&offset={3}".format(action, resid, limit, offset)
            rettext = self.GetRespText(url)
            
            if rettext is not None:
                try:
                    ret = json.loads(rettext)
                    
                    ismore = ret["more"]
                    
                    if ret["total"] == 0 or ret["total"] == "0":
                        return
                    
                    if len(ret["hotcomments"]) > 0:
                        for hotcomment in ret["hotcomments"]:
                            if hotcomment["commentId"] not in hotidls:
                                hotidls.append(hotcomment["commentId"])
                            
                    for comment in ret["comments"]:
                        try:
                            commentinfo = Commentinfo()
                            commentinfo.commentid = comment["commentId"]
                            commentinfo.createtime = comment["time"]
                            commentinfo.content = comment["content"]
                            commentinfo.parentcommentid = comment["parentCommentId"]
                            commentinfo.likecount = comment["likeCount"]
                            commentinfo.userid = comment["user"]["userId"]
                            commentinfo.ishot = commentinfo.commentid in hotidls
                            commentinfo.resourceid = resid
                            commentinfo.resourcetype = action
                            
                            yield commentinfo
                        except Exception:
                            #TODO: 错误日志
                            continue
                    iters += 1
                    offset = limit * iters
                        
                except Exception:
                    #TODO: 错误日志
                    ismore = False
                
            else:
                ismore = False
            
    def SaveComment(self, commentinfo):
        return self.manager.insert(commentinfo)


if __name__ == "__main__":
    eventmanager = ManageFactory("event")
    collcommen = CollectComment()
    
    pagesize = 100
    eventtotal = eventmanager.totalnum({})
    eventpages = eventtotal / pagesize + (1 if eventtotal % pagesize > 0 else 0)
    offset = 0
    
    #TODO: 打印输出，event总数，当前到第几页，
    for iter in eventpages:
        offset = pagesize * iter
        for event in eventmanager.getlist({}, limit = pagesize, skip = offset):
            for comment in collcommen.Extractfromevent(event.eventid):
                collcommen.SaveComment(comment)

    actionls = ["song", "album", "playlist", "program"]
    
    for action in actionls:
        sourcemanage = ManageFactory(action)
        sourcetotal = sourcemanage.totalnum({})
        sourcepages = sourcetotal / pagesize + (1 if sourcetotal % pagesize > 0 else 0)
        
        for iter in sourcepages:
            offset = pagesize * iter
            
            for source in sourcemanage.getlist({}, limit = pagesize, skip = offset):
                for comment in collcommen.Extractfromresouce(source.id, action):
                    collcommen.SaveComment(comment)

