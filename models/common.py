#coding:utf-8
'''
Created on 2020��2��4��

@author: cmck
'''


import json
import copy
import re

class Common:
        
    def __init__(self):
        pass
    
    # TODO: 需要测试下，给类的私有成员赋值情况
    def copy(self, val):
        """
        function: 将字典格式的实例转换为类实例
        """
        
        if isinstance(val, dict):
            classname = self.__class__.__name__
            
            classdict = vars(self)
            for name, val in classdict.items():
                propertyname = name.replace("_" + classname +"__", "")
                if val.get(propertyname, None) is not None:
                    classdict[name] = val[propertyname]
            
    
    def getitems(self):
        """
        function: 将模型实例以字典格式输出
        """
        classname = self.__class__.__name__
        ddit = {}
        
        for name, value in vars(self).items():
            ddit[name.replace("_" + classname +"__", "")] = value
        
        return copy.deepcopy(ddit)
    
    def validatenum(self, num):
        ret = -1
        try:
            if(isinstance(num, str) and num.isdigit()):
                ret = int(num)
                
        except Exception:
            raise ValueError("the value must be digit")
            
        return ret