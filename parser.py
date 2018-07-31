#!/usr/bin/env python3

import re



#パーサークラス
class Parser: 
 #関数 __init__ :初期化.
 #引数 opiton   :区切りとして使用する文字列を追加する
 def __init__(self,_str,option=""):
  sepRex = "\s+"
  if not option == "":
   optionAr = list(filter(lambda x:not x=="", re.split("\s+",option) ))
   for x in optionAr:
    _str = _str.replace(x," {0} ".format(x))
  #print(sepRex)
  #要素に分割し、空白要素も削除する
  self.data = list(filter(lambda x:not x=="", re.split(sepRex,_str)))

 #関数 getBetween:startとendで指定された文字列の間の要素を取得する
 #引数 endStr    :Trueの場合文字列の終端に来た場合にも値を返す
 def getBetween(self,start,end,endStr=True):
  startAr   = re.split("\s+",start)
  endAr     = re.split("\s+",end)
  ret       = []
  flagStart = False
  flagEnd   = False
  for x in self.data:
   if (flagStart == False) and (x in startAr):
    flagStart =True
    continue
   if flagStart == True:
    if x in endAr:
     return ret
    else:
     ret.append(x)
  if endStr == True:
   return ret
  else:
   return []



if __name__ == "__main__":
 p = Parser("select ngo dago  where a<100","< > =")
 print(p.data)
 a = p.getBetween("select","where")
 a = p.getBetween("where","")
 print(a)
 p = Parser("select ngo dago ")
 a = p.getBetween("select","where")
 print(a)



