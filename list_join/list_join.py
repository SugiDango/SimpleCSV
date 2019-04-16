#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function

#mGetpList
#リストから指定された複数のインデックスの値を取得し、
#複数の値をリスト型で返す
#_list:取得すする元になるリスト
#_num:popするインデックス（複数指定可能）
def mGetList(_list,*_num):
 ret = []
 _num =list(_num)
 for x in _num:
  ret.append(_list[x])
 return ret


#mIndexCompareList
#複数指定したインデックスから取得した値で
#比較を行う。戻り値はBool型
#Alist:比較するリスト１つめ
#Bnums:比較対象とするインデックスの値。リスト型で指定する
#Blist:比較するリスト２つめ
#Bnumes:比較対象とするインデックス。ふたつ目
def mIndexCompareList(Alist,Anums,Blist,Bnums):
 for (a,b) in zip(Anums,Bnums):
  if not Alist[a] == Blist[b]:
   return False
 return True

#compareJoinList
#複数指定したインデックスから取得した値で
#比較を行う。結果がTrueであれば
#比較した２つのリストを結合したリストを返す
#満たされなければ、[]を戻す（空のリストを戻す）
#Alist:比較するリスト１つめ
#Bnums:比較対象とするインデックスの値。リスト型で指定する
#Blist:比較するリスト２つめ
#Bnumes:比較対象とするインデックス。ふたつ目
def compareJoinList(Alist,Anums,Blist,Bnums):
 if mIndexCompareList(Alist,Anums,Blist,Bnums):
  return Alist + Blist
 return []


#innerJoinMatrix
#二次元配列で指定した列番号が一致する行を結合する
#Alist:比較するリスト１つめ
#Bnums:比較対象とするインデックスの値。リスト型で指定する
#Blist:比較するリスト２つめ
#Bnumes:比較対象とするインデックス。ふたつ目
def innerJoinMatrix(Alist,Anum,Blist,Bnums):
 retList = []#戻り地となるリスト
 for a in Alist:
  for b in Blist:#リストＢのなから条件に一致する行を搜す。
   #print(a)#debug
   #print(b)#debug
   #print(Anum)#debug
   #print(Bnums)#debug
   ret = compareJoinList(a,Anum,b,Bnums)
   #print(ret)#debug
   if ret == []:
    continue
   else:
    retList.append(ret)
 #print(retList[0])#debug
 return retList



