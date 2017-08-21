#!/usr/bin/env python
#coding=utf-8

#根据提供的关键词，爬取源码中包含关键词的所有文件。


import os
from lib.result import *


def Spider(path, key):
    for root,dirs,files in os.walk(path):
        for file in files:
            content = "%s\%s" %(root,file)
            try:
                with open(content) as file:
                    keys = file.read()
                    if keys.find(key) != -1:
                        Result(key,content)
                        print key
                        print content
            except Exception,e:
                print "error",content,e
