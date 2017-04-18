#!/usr/bin/env python
# encoding: utf-8

import requests
import bs4
import re
import time


bxj_url = "https://bbs.hupu.com/bxj-{0}"


def download(page_num):
    url = bxj_url.format(page_num)
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content)
    table = soup.find("table", class_="bbstopic ptable topiclisttr")
    hrefs = table.findAll("a")
    urls = []
    for a in hrefs:
        try:
            urls.append(a["href"])
        except:
            pass
    urls = filter(lambda x: re.match(r'/\d*\.html$', x), urls)
    urls = [url+"\n" for url in urls]
    with open('urls', "a") as f:
        f.writelines(urls)
    time.sleep(5)


for i in range(1, 101):
    print i
    download(i)
