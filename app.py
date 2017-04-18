#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template, request
import query


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search")
def search():
    words = request.args.get("search_words", "12")
    hrefs = query.query_with_string(words)[:20]
    prefix = "http://bbs.hupu.com"
    urls = [prefix+href for s, href in hrefs]
    return render_template("list.html", urls=urls)
if __name__ == "__main__":
    app.run()
