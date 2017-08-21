#!/usr/bin/env python2.7
#coding=utf-8

#提供源码路径，以及需要查询的关键词，不输入keyword，则默认为所有关键词，使用者可以通过对key2进行增删，自定义需要查询的关键词。

from lib.spider import *

def Search():
    path = raw_input("Please input PHP Code Path:")
    key1 = raw_input("Please enter the keyword you need to query:")
    key2 = ['_GET','_POST','_COOKIE','_REQUEST','_SERVER','_FILES','_ENV','_HTTP_COOKIE_VARS','_HTTP_ENV_VARS','_HTTP_GET_VARS','_HTTP_POST_FILES','_HTTP_POST_VARS','_HTTP_SERVER_VARS','system','exec','passthru','shell_exec','`','popen,proc_open','pcntl_exec','echo','print','printf','vprintf','<%=$','include','include_once','require','require_once','file_get_contents','show_source','highlight_file','readfile','fopen','file','fgetss','fgets','parse_ini_file','move_upload_file','preg_replace','getimagesize','getimageinfo','unlink','session_destroy','eval','assert','preg_replace','call_user_func','call_user_func_array','array_map','create_function','php://','xpath','copy','rmdir','fwrite','chmod','fread,readfile','ftruncate','file_put_contents','fputcsv','fputs','extract','parse_str','import_request_variables','$$','$command']
    if key1 not in key2 and key1 !="":
        try:
            Spider(path,key1)
        except Exception,e:
            print "error",e
    else:
        try:
            for i in key2:
                Spider(path,i)
        except Exception,e:
            print "error",e

