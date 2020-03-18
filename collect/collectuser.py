#coding:utf-8
'''
Created on 2020年2月4日

@author: cmck
'''

import requests

from collect import *
import threading
import queue
import time

from collectuserinfo import CollectUser
from collectuserrelation import Collectrelation
from collectplaylist import CollectPlaylist
from collectradio import CollectRadio
from collectevent import CollectEvent
from operamodels.managefactory import ManageFactory
from models.relationinfo import Relationinfo

import random
import os

import gevent
from gevent import monkey
monkey.patch_all(thread = False, queue = False)


class ClusteUser(threading.Thread):
    def __init__(self, userqueue, followsqueue, follwedsqueue):
        
        threading.Thread.__init__(self)
        # 待抽取的用户列表
        self.userqueue = userqueue
        self.followsqueue = followsqueue
        self.follwedsqueue = follwedsqueue
        
        # 协程 
        self.colluser = CollectUser()
        self.collevent = CollectEvent()
        self.collplaylist = CollectPlaylist()
        self.collradio = CollectRadio()
        
        # 控制获取用户信息的频率
        self.rate = 1 + random.randint(0, 2)
        # 控制队列无数据时的迭代上限
        self.uperiter = 20
    
    # 协程，获取用户信息、动态、收藏歌单、电台，评论内容单独获取
    def CordinateUserinfo(self, userid):
        
        try:
            guser = gevent.spawn(self.colluser.ExtractUser, userid)
            gevent = gevent.spawn(self.collevent.ExtractEvent, userid)
            gplaylist = gevent.spawn(self.collplaylist.run, userid)
            gradio = gevent.spawn(self.collradio.run, userid)
            
            glist = []
            glist.extend([guser, gevent, gplaylist, gradio])
            
            gevent.joinall(glist)
        except Exception:
            #TODO:
            pass
        
        try:
            gevent.killall(glist)
        except Exception:
            #TODO: 
            pass
       
    def run(self):
        # 控制结束
        terminal = False
        # 队列无数据时迭代次数
        iter = 0
        
        while not terminal:
            while not self.userqueue.empty():
                iter = 0
                userid = self.userqueue.get()
                # 用户不存在
                if not self.operauser.Exists(userid):
                    # 开启协程. 获取用户数据，并开启协程获取用户动态、收藏的歌单、电台
                    self.CordinateUserinfo(userid)
                        
                    # 将未遍历过的用户id存放在队列中，供遍历关系的两个线程使用
                    self.followsqueue.put(userid)
                    self.followedsqueue.put(userid)
                
                time.sleep(self.rate)
            
            # 队列长时间为空，则默认为没有数据
            time.sleep(10)
            iter += 1
            if iter == self.uperiter:
                terminal = True
    
# 获取粉丝/关注者
class ClustFollow(threading.Thread):
    
    def __init__(self, userqueue, followqueue, action = "follows"):
        threading.Thread.__init__()
        
        self.userqueue = userqueue
        self.queue = followqueue
        self.collrelat = Collectrelation(action)
        # action 的取值为“follows”、 “followed”
        self.action = action
        
        self.rate = 1 + random.randint(0, 3)
        # 控制队列无数据时的迭代上限
        self.uperiter = 20

    def run(self):
        # 控制结束
        terminal = False
        # 队列无数据时迭代次数
        iter = 0
        while not terminal:
            while not self.queue.empty():
                
                userid = self.queue.get()
                # 新增的用户数
                newfollownum = 0
                
                # TODO: 打印正在获取哪个userid的action
                
                for followid in self.collrelat.Collectfollows(userid, action = self.action):
                    
                    originuid = ""
                    endpointuid = ""
                    
                    if self.action == "follows":
                        originuid = followid
                        endpointuid = userid
                    else: # followeds
                        originuid = userid
                        endpointuid = followid
                
                    relatinfp = Relationinfo()
                    relatinfp.arrow = endpointuid
                    relatinfp.tail = originuid
                    relatinfp.rtype = "follow"
                
                    # 1. 判断关系是否存在，关系不存在，则追加至数据库且开始遍历
                    if not self.collrelat.Exists(relatinfp.id):
                        self.collrelat.Savefollow(relatinfp)
                        newfollownum += 1
                        
                        # 控制待搜索用户队列
                        isfull = True
                        while isfull:
                            try:
                                while not self.userqueue.full():
                                    self.userqueue.put(followid)
                                    isfull = False
                            except Exception:
                                # TODO: 预防队列满时的异常
                                pass
                            time.sleep(10)
                
                # TODO: 打印userid的action新数目共有多少个
                            
                # 控制获取粉丝/追随者的速度
                time.sleep(self.rate)
            
            time.sleep(10)
            iter += 1
            if iter == self.uperiter:
                terminal = True


def ExportUser(followsqueue, follwedsqueue):
    """
    function: 导出已经采集过的用户id
    """
    usermanager = ManageFactory("user")
    total = usermanager.totalnum({})
    pagesize = 200
    pagenum = total / 100 + (1 if total % pagesize != 0 else 0)
    
    # 将已采集过的userid存放在文件中
    mainpath = os.path.dirname(os.path.abspath(__file__))
    rootpath = os.path.dirname(mainpath)
    tmppath = rootpath + "/tmp/"
    tmpfile = tmppath + "tmp.txt"
    
    for iter in range(pagenum):
        offset = pagesize * iter
        
        userls = usermanager.getlist({}, limit = pagesize, skip = offset)
        writestr = "\n".join(user.userid for user in userls) + "\n"
        
        with open(tmpfile) as fp:
            fp.write(writestr)
            
    with open(tmpfile) as fp:
        for line in fp:
            userid = line.repalce("\n", "")
            followsqueue.put(userid)
            follwedsqueue.put(userid)
            
    try:
        os.remove(tmpfile)
    except Exception:
        pass


def collectrun(startuid, isforest = False):
    """
    function: 以单颗树或森林的根节点遍历所有关系
    isforest 为 True的情况是：
    # 顺着关系链的搜索被打断了，关系链由一棵树被打散为森林，需要以已收集的用户为起点，遍历所有关系
    # 此时，startuid = None
    """
    # 用户队列
    userqueue = queue.Queue(2000)
    # 关注者队列
    followsqueue = queue.Queue()
    # 粉丝队列
    follwedsqueue = queue.Queue()
    
    clufollow = ClustFollow(userqueue, followsqueue, action = "follows")
    clufollowed = ClustFollow(userqueue, follwedsqueue, action = "followeds")
    
    clufollow.start()
    clufollowed.start()
    
    if not isforest:
        userqueue.put(startuid)
    else:
        # 0. 启用遍历树节点的线程
        # 1. 获取已采集过的用户列表
        # 2. 将用户列表塞入用户队列中
        exportthread = threading.Thread(target = ExportUser, args = (followsqueue, follwedsqueue))
        exportthread.start()
        
    # 等待完成存放已获取的id到文件的工作
    while not follwedsqueue.empty():
        time.sleep(2)
    
    threads = []
    # 构造爬去单个用户信息的线程
    cluuser = ClusteUser(userqueue, followsqueue, follwedsqueue)
    cluuser.start()
    
    threads.extend([cluuser, clufollow, clufollowed])
    
    # 让各个线程飞一会
    time.sleep(10)
    
    flag = 0
    # 保证三个线程都停止，且用户队列中无数据
    while flag != len(threads) or not userqueue.empty():
        if flag != len(threads):
            flag = 0
            
            for thread in threads:
                if not thread.is_alive():
                    flag += 1
                    
        time.sleep(8)
    
    # TODO: 数据获取结束


if __name__ == "__main__":
    startuserid = ""
    collectrun(startuserid, False)




