#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json,sys
import cgitb,cgi
import random

cgitb.enable()

#---------------------#
#   クラスの定義      #
#---------------------#

class MakeJSONCB:
    def __init__(self):
        self.ids = ["CB1","CB2","CB3","CB4"]
    #現在CBの情報を取得する
    def getCurrentCB(self):
        csv = open("CB.csv").read().split(",")
        csv = map(int,csv)
        return list(csv)
        #return [0,0,1,1]
    #JSON形式のデータを作成する
    def makeJSON(self):
        c_cb = self.getCurrentCB()
        ret = []
        for id,val in zip(self.ids , c_cb):
            dict_cb = {}
            dict_cb["type"] = "CB"
            dict_cb["id"]   = id
            dict_cb["val"]  = val
            ret.append(dict_cb)
        #print(ret)
        return ret


class MakeJSONTM:
    def __init__(self):
        self.ids = ["TM1","TM2","TM3","TM4"]
    #現在CBの情報を取得する
    def getCurrentNowTM(self):
        ret = []
        for x in self.getCurrentContorolTM():
            ret.append(int(x*random.random()))
        return ret
        #return [50,100,150,200]
    def getCurrentContorolTM(self):
        csv = open("TM.csv").read().split(",")
        csv = map(int,csv)
        return list(csv)
        #return [100,200,300,400]
    #JSON形式のデータを作成する
    def makeJSON(self):
        now_tm = self.getCurrentNowTM()
        con_tm = self.getCurrentContorolTM()
        ret = []
        for id,now,control in zip(self.ids , now_tm,con_tm):
            dict_tm = {}
            dict_tm["type"]    = "TM"
            dict_tm["id"]      = id
            dict_tm["now"]     = now
            dict_tm["control"] = control
            ret.append(dict_tm)
        #print(ret)
        return ret


#--------------------#
#  JSONデータの送信  #
#--------------------#

print('Content-Type:application/json\n\n')
#print(json.dumps(result_json))
#print(json.dumps(current_cb))
kind =  cgi.FieldStorage()["kind"].value
if kind == "CB":
    jcb = MakeJSONCB()
    jtm = MakeJSONTM()
    print( json.dumps( jcb.makeJSON()+jtm.makeJSON() ))






