#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
import list_join as LJ



def test_mGetList():
 print("###mGetListのテストを実行###")
 print("テスト関数:GetList(_list,*_num)")
 a = [1,2,3,4,5]
 print(str(a)+" -> _list ")
 print("2,4 -> *_num ")
 ret = LJ.mGetList(a,2,4)
 print("res:"+str(ret))


def test_mIndexCompareList():
 print("###test_mIndexCompareList###")
 print("テスト関数:mIndexCompareList(Alist,Anums,Blist,Bnums)")
 a = [1,2,3,4,5]
 b = [3,4,5,6,7]
 print(str(a)+" -> Alist")
 print(str(b)+" -> Blist")
 aNums = [2,3]
 bNums = [0,1]
 print(str(aNums) + " -> Anums ")
 print(str(bNums) + " -> Bnums ")
 ret = LJ.mIndexCompareList(a,aNums,b,bNums) 
 print("ret:"+str(ret))
 print("Case2")
 bNums = [0,3]
 print(str(bNums) + " -> Bnums ")
 ret = LJ.mIndexCompareList(a,aNums,b,bNums) 
 print("ret:"+str(ret))


def test_compareJoinList():
 print("###test_compareJoinList###")
 print("テスト関数:compareJoinList(Alist,Anums,Blist,Bnums)")
 a = [1,2,3,4,5]
 b = [3,4,5,6,7]
 print(str(a)+" -> Alist")
 print(str(b)+" -> Blist")
 aNums = [2,3]
 bNums = [0,1]
 print(str(aNums) + " -> Anums ")
 print(str(bNums) + " -> Bnums ")
 ret = LJ.compareJoinList(a,aNums,b,bNums) 
 print("ret:"+str(ret))
 print("Case2")
 bNums = [0,3]
 print(str(bNums) + " -> Bnums ")
 ret = LJ.compareJoinList(a,aNums,b,bNums) 
 print("ret:"+str(ret))

def test_innerJoinMatrix():
 print("###test_#innerJoinMatrix###")
 print("テスト関数: innerJoinMatrix(Alist,Anum,Blist,Bnums)")
 a  = [1,2,3,4,5]
 a2 = [3,4,5,6,7]
 b2  = [1,2,3,4,5] 
 b = [3,4,5,6,7]
 b3 =  [3,4,4,4,4]
 A = [a,a2]
 B = [b,b2,b3]
 
 print(str(A)+" -> Alist")
 print(str(B)+" -> Blist")
 aNums = [2,3]
 bNums = [0,1]
 print(str(aNums) + " -> Anums ")
 print(str(bNums) + " -> Bnums ")
 ret = LJ.innerJoinMatrix(A,aNums,B,bNums) 
 print("ret:"+str(ret))
 print("Case2")
 bNums = [0,3]
 print(str(bNums) + " -> Bnums ")
 ret = LJ.innerJoinMatrix(A,aNums,B,bNums) 
 print("ret:"+str(ret))





#main
#処理を実行する関数
def main():
 test_mGetList()
 test_mIndexCompareList()
 test_compareJoinList()
 test_innerJoinMatrix()

if __name__ == "__main__":
 main()


