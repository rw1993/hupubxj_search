#!/usr/bin/env python
# encoding: utf-8
import pickle
import jieba



word_dict = pickle.load(open('./word_dict', "rb"))


inverted_index = pickle.load(open('./inverted_index', "rb"))


href_word_tfidf = pickle.load(open("./href_word_tdidf", "rb"))

def cache(func):
    c = []
    length = 20
    def _(string):
        i = -1
        for index, (s, r) in enumerate(c):
            if s == string:
                i = index
                break
        if i != -1:
            s, r = c.pop(i)
            c.append((s, r))
            return r
        else:
            if len(c) == length:
                c.pop(0)
            r = func(string)
            c.append((string, r))
            return r
    return _




def query(words):
    words = [word for word in words]
    document_href = []
    for word in words:
        document_href += inverted_index.get(word, [])

    def get_score(href):
        word_tfidf = href_word_tfidf[href]
        score = .0
        for word in words:
            score += word_tfidf.get(word, 0.0)
            #print score
        return score, href

    scores = map(get_score, document_href)
    return sorted(scores, reverse=True)



#@cache
def query_with_string(string):
    words = jieba.cut(string)
    #print words
    return query(words)


if __name__ == "__main__":
    #keys = [key for key in inverted_index]
    #print query([keys[0]])
    print query_with_string(u"王者荣耀")

