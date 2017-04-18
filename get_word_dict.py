#!/usr/bin/env python
# encoding: utf-8
import MySQLdb
import jieba
import pickle


con = MySQLdb.connect(host="localhost", user="root", passwd="5626719", db="hupu",
                              charset="utf8", port=3306)
cur = con.cursor()



sql = 'select href, content, title from bxj'
word_dict = {}


cur.execute(sql)
for r in cur.fetchall():
    for word in jieba.cut(r[1]):
        print word.encode("utf8")
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1



pickle.dump(word_dict, open("word_dict", "wb"))
