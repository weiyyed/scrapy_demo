#!/usr/bin/env python3
# coding: utf-8

import sys
sys.setrecursionlimit(900000000)

import json # https://docs.python.org/3/library/json.html
import requests # https://github.com/kennethreitz/requests
import records # https://github.com/kennethreitz/records
import sys
# randomuser.me generates random 'user' data (name, email, addr, phone number, etc)
# r = requests.get('http://api.randomuser.me/0.6/?nat=us&results=10')
# j = r.json()['results']

db = records.Database('sqlite:///users.db') #连接数据库
# db_con = db.get_connection()  #获取连接
# rows=db_con.query("SELECT * FROM persons") #执行sql语句
with db.transaction() as tx:
    user = {"key": 16, "fname": "zhangsan"}
    tx.query('INSERT INTO persons(key,fname) values (:key, :fname)', **user)
