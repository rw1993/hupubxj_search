#!/usr/bin/env python
# encoding: utf-8
import MySQLdb
import pickle
import math
import jieba


con = MySQLdb.connect(host="localhost", user="root", passwd="5626719", db="hupu",
                              charset="utf8", port=3306)
cur = con.cursor()

total = 11867.0

sql = 'select href, content, title from bxj'

word_dict = pickle.load(open('./word_dict'))


inverted_index = {}


inverted_index = {key:[] for key in word_dict}


cur.execute(sql)
for r in cur.fetchall():
    print r[0].encode("utf8")
    for key in inverted_index:
        if key in r[1]:
            inverted_index[key].append(r[0])


pickle.dump(inverted_index, open("inverted_index", "wb"))
