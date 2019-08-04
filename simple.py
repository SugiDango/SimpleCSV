#!/usr/bin/env python3
# encoding: utf-8
from __future__ import print_function


#### 履歴 ####
# 2018-07-31 : 引数方式の方式を変更
##############

#### 変更方針 ####
# @where関数の引数をWhereクラスに変更する
##################



#select
#-fパス

import sys,re,csv
import parser
from functools import partial


######  便利系関数 #########################

### delBlankList:リスト内にある空白文字を削除する###
def delBlankList(_list):
 return list(filter(lambda x:not x=="", _list ))

#debugPrint
#関数名と引数
def getFuncName():
 return sys._getframe().f_code.co_name



############################################



######  SimpleCSVクラス  ###################

class SimpleCSV:
 #whereFlag
 #wherePos
 #headerNum:CSVのヘッダーとなる行番号
 #data:データの中身
 ### __init__:初期化 ###
 def __init__(self,data = ""):
  self.whereFlag=[]
  self.wherePos =-1   #whereFlag用のインデックス
  self.headerNum = 0  #ヘッダーの行番号
  if data == "":
   #標準入力からCSVを取得
   buf  = sys.stdin.read().split("\n")
   buf = delBlankList(buf)
   data = csv.reader(buf,delimiter=",")
  else:
   #ファイルからCSVを取得
   buf = readFile(data).split("\n")
   print(buf)
   buf.remove("")
   data = csv.reader(buf,delimiter=",")
  self.data = list(data)#f
 
 ### columnToIndex:カラム名をインデックスに変換する### 
 #name:インデックスを取得したいヘッダの名称。
 #戻り値:インデックス。
 def columnToIndex(self,name):
  return self.data[self.headerNum].index(name)

 ### getHeader ###
 #ヘッダーのリストを取得する
 #戻り値:hederNumが正の値であれば、
 #それをインデックスとして返す
 #負の値であれば、列番をヘッダーとして返す
 def getHeader(self):
  if 0<=self.headerNum :
   return self.data[self.headerNum]
  data_len = len(self.data[0])
  return list( range( data_len ) )

 ### select:カラムを選択する ###
 def select(self,_names):
  #print("select:"+_names)#Debug
  if not type(_names) == list:
   _names = toList(_names)
   print("select:"+str(_names))#Debug
  selectIndex =  mIndexList( self.data[self.headerNum],*_names)
  buf = []
  #print(selectIndex)
  for x in self.data:
   buf.append( mPopList(x,*selectIndex))
  self.data = buf
  #print(buf)

 ### whereNum:数値に対してwhere処理を行う ###
 def setWhereNum(self,proc,col,valType="num"):
  self.wherePos = self.wherePos + 1
  self.whereFlag.append([])
  cnt = -1
  for x in self.data:
   cnt = cnt + 1
   if cnt == self.headerNum:
    self.whereFlag[self.wherePos].append(1)
    continue
   
   #型によって演算を変更
   if valType == "num":     #数値比較の場合
    checkVal = str(x[col])
   else:                    #文字列比較の場合
    checkVal = "\"{0}\"".format(x[col])
   #演算の実行
   if eval(checkVal + proc  ):
    self.whereFlag[self.wherePos].append(1)
   else:
    self.whereFlag[self.wherePos].append(0)

 ### whereをORで行う ###
 def doWhereOR(self):
  buf = []
  for x in range(len(self.data)):
   for flag in self.whereFlag:
    if flag[x] == 1:
     buf.append(self.data[x])
     break
  self.data = buf

 ### whereをANDで行う ###
 def doWhereAND(self):
  buf = [] 
  for x in range(len(self.data)):
   andFlag = True
   for flag in self.whereFlag:
    if flag[x] == 0:
     andFlag   =  False
     break
   if andFlag == True: 
    buf.append(self.data[x])
  self.data = buf

 ### print:CSV形式で出力する ### 
 def print(self,sep=","):
  for x in self.data:
   print(sep.join(x))
############################################


#readFile
#path:ファイルパス
#テキストファイルを読み込んで文字列を返す
def readFile(path):
 f = open(path,"r")
 res = f.read()
 f.close()
 return res

#mPopList
#リストから指定されたインデックスの値をpopする
#_list:ポップする元になるリスト
#_num:popするインデックス（複数指定可能）
def mPopList(_list,*_num):
 ret = []
 _num =list(_num)
 while not len(_num) == 0:
  thisNum = _num.pop(0)
  ret.append( _list.pop(thisNum ))
  _num = list( map(  lambda x: x if(x<thisNum)else x-1   ,_num ))
  #print(_num)
 return ret

#mIndexList
#リストで指定された要素が存在するインデックスを返す
#_list:要素を探すもとになるリスト
#*elem:インデックスを探した要素（複数指定可能）
def mIndexList(_list,*elem):
 #if not type(elem) == list:
 # elem = toList(elem)
 print(elem)
 ret = []
 for x in elem:
  ret.append( _list.index(x))
 return ret

#toList
#strを一つ持つlistを作成可能なlistのコンストラクタ
#data:リストにするデータ
def toList(data):
 #print("toList:"+data)#debug
 _list = []
 if type(data) in [str,int]:
  _list.append(data)
  print(_list)#debug
  return _list
 else:
  return list(data)



##### 引数管理クラス #############
class ArgManager:
 ###__init__ :  初期化############
 def __init__(self):
  arg = sys.argv[1::]
  argc = len(arg)
  self.arg  = arg
  self.argc = argc
  #ファイルの取得i
  self.filePath = ""

  #helpの確認を行う
  if "--help" in arg:
   print(help_msg)
   exit()

  for x in arg:
   if not None ==  re.match("-f",x):
    self.filePath = x.split("-f")[1]
    arg.remove(x)
  print(arg)
  #パース用の文字列取得
  for x in arg:
   if  None ==  re.match("-",x):
    print(x)
    self.parse = parser.Parser(x,"< > == ")
    break

 def getSelect(self):
  ret = self.parse.getBetween("select","where")
  return ret

 def getWhere(self):
  whereBuf = self.parse.getBetween("where","")
  ret = []
  while 2 <  len(whereBuf):
   a = mPopList(whereBuf,0,1,2)
   b = Where(a)
   ret.append(b)
  return ret

 def checkHelp():
  if "--help" in self.arg:
   return True
  return False

###################################

#ヘルプメッセージ
help_msg="""ファイルの指定 -fファイル名
"""

#Whereのクラス
class Where:
 def __init__(self,_list):
  self.name  = _list[0]
  self.enzan = _list[1]
  self.val   = _list[2]

 def debug(self):
  return "Where: name={0} , enzan={1} , val={2}".format(self.name,self.enzan,self.val)



#main処理
if __name__ == "__main__":
 argman = ArgManager() 
 print(argman.filePath)
 simCSV = SimpleCSV(argman.filePath)
 simCSV.select("dango")
 print(simCSV.data)
 
 
 
 #whereが存在する場合はwhere処理を行う 
"""
 if 0< len(argman.getWhere()):
  for x in argman.getWhere():
   if x.val[0] in "1234567890-+":
    valType = "num"
   else:
    valType = "str"
   simCSV.setWhereNum(  x.enzan + x.val  ,simCSV.columnToIndex( x.name) ,valType  )
   simCSV.doWhereOR()
 simCSV.print()
 if not len(argman.getSelect()) == len(set(argman.getSelect())):
  print("エラー:selectしたカラムが重複しています")
  exit()
 print(argman.getSelect())

 if not argman.getSelect() == []:
  simCSV.select(argman.getSelect())
 simCSV.print()

"""



