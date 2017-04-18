#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import bs4
import MySQLdb
import multiprocessing
import time


with open("./urls", "r") as f:
    urls = f.readlines()
    urls = map(lambda x: x.strip(), urls)
    urls = list(set(urls))


def get_downloaded():
    con = MySQLdb.connect(host="localhost", user="root", passwd="5626719", db="hupu",
                            charset="utf8", port=3306)
    cur = con.cursor()
    sql = 'select href from bxj'
    cur.execute(sql)
    urls = cur.fetchall()
    cur.close()
    con.close()
    urls = [url for url,  in urls]
    return urls


def insert(href=None, title=None, content=None):
    sql = "insert into bxj values(%s, %s, %s)"
    con = MySQLdb.connect(host="localhost", user="root", passwd="5626719", db="hupu",
                          charset="utf8", port=3306)
    cur = con.cursor()
    cur.execute(sql, (href, title, content))
    con.commit()
    cur.close()
    con.close()
    time.sleep(1)
    print href


def download_a_url(url):
    try:
        url_prefix = "https://bbs.hupu.com/{0}"
        r = requests.get(url_prefix.format(url))
        soup = bs4.BeautifulSoup(r.content)
        title = soup.find("h1", id="j_data")["data-title"].encode("utf-8")
        content = soup.find("div", class_="quote-content").text.encode("utf-8")
        insert(url, title, content)
    except Exception, e:
        print e



if __name__ == "__main__":
    pool = multiprocessing.Pool(8)
    pool.map(download_a_url, urls)
