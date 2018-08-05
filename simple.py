#!/usr/bin/env python3


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



############################################



######  SimpleCSVクラス  ###################

class SimpleCSV:
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
   buf.remove("")
   data = csv.reader(buf,delimiter=",")
  self.data = list(data)
 
 ### columnToIndex:カラム名をインデックスに変換する### 
 def columnToIndex(self,name):
  return self.data[self.headerNum].index(name)

 ### select:カラムを選択する ###
 def select(self,_names):
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


#ファイルを読みこむ
def readFile(path):
 f = open(path,"r")
 res = f.read()
 f.close()
 return res


#リストで指定されたpopする
def mPopList(_list,*_num):
 ret = []
 _num =list(_num)
 while not len(_num) == 0:
  thisNum = _num.pop(0)
  ret.append( _list.pop(thisNum ))
  _num = list( map(  lambda x: x if(x<thisNum)else x-1   ,_num ))
  #print(_num)
 return ret
 
#リストで指定された要素が存在するインデックスを返す
def mIndexList(_list,*elem):
 ret = []
 for x in elem:
  ret.append( _list.index(x))
 return ret


##### 引数管理クラス #############
class ArgManager:
 ###__init__ :  初期化############
 def __init__(self):
  arg = sys.argv[1::]
  argc = len(arg)
  #ファイルの取得
  self.filePath = ""
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
###################################


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
 #print(argman.select)
 #print(argman.filePath)
 simCSV = SimpleCSV(argman.filePath)
 #print(simCSV.data)
 #print(argman.select)
 #print(argman.getWhere()[0].debug())
 #print(simCSV.columnToIndex( argman.getWhere()[0].name  ))


 #whereが存在する場合はwhere処理を行う 
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





