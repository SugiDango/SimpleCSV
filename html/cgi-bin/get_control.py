#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json,sys
import cgitb,cgi
import os.path

cgitb.enable()

#---------------------#
#   クラスの定義      #
#---------------------#

indexer  = {}
for x in ["CB","TM"]:
    for y in range(1,5):
        indexer[x+str(y)] = y - 1

sys.stderr = open("./err_log", "w")

#---------------------#
#   関数の定義        #
#---------------------#
def operater(types,id,val):
    csv_name = types + ".csv" 
    if os.path.exists(csv_name):
        csv = open(csv_name).read().split(",")
        csv = map(int,csv)
    else:
        csv = [0,0,0,0]
    print(csv)
    i = indexer[id]
    csv[i] = int(val)
    csv = map(str,csv)
    csv = ",".join(csv)
    open(csv_name,"w").write(csv)

#--------------------#
#  JSONデータの送信  #
#--------------------#
#sys.stderr.write(get_data)
get_data = dict(cgi.FieldStorage())
#print(str(get_data["type"]))
operater(get_data["type"].value,get_data["id"].value,get_data["val"].value)

print('Content-Type:application/json\n\n')
#print(indexer)
#operater("CB","CB1",1)
#print(json.dumps(result_json))
#print(json.dumps(current_cb))



