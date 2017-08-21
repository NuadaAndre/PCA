#!/usr/bin/env python2.7
#coding=utf-8

#保存怕取得结果到cvs文件中

import csv,codecs,time
from lib.spider import *


def Result(key,path):
    filename = 'PCA_'+time.strftime("%Y-%m-%d_%H.%M",time.localtime())+'.csv'
    csvfile = file(filename, 'a+')
    writer = csv.writer(csvfile)
    data = [
      (key, path)
    ]
    writer.writerows(data)
    csvfile.close()

