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


cur.execute(sql)


word_idf = {key:0.0 for key in word_dict}
#get_idf
cur.execute(sql)
for r in cur.fetchall():
    words = jieba.cut(r[1])
    words = set(word for word in words)
    for word in words:
        word_idf[word] += 1.0

#get_tdidf

href_word_tdidf = {}
cur.execute(sql)
for r in cur.fetchall():
    href = r[0]
    #print href.encode("utf8")
    words = jieba.cut(r[1])
    word_tfidf= {}
    for word in words:
        if word not in word_tfidf:
            word_tfidf[word] = 0.0
        word_tfidf[word] += 1.0
    for key in word_tfidf:
        word_tfidf[key] = word_tfidf[key] / len(r[1]) * math.log(total/word_idf[key], 2)
        print word_idf[key], key.encode("utf8")
    href_word_tdidf[href] = word_tfidf


pickle.dump(href_word_tdidf, open("href_word_tdidf", "wb"))

