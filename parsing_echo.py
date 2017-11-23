# -*- coding: utf-8 -*-

import logging
from grab import *
import time
import json
import urllib.request
from pyquery import PyQuery as pq
import re

# NEWS_COUNT = 10
#
#
# def loadPage(url):
#     g = Grab()
#     g.setup(timeout=15, connect_timeout=10)
#     g.go(url)
#     response = str(g.response.body)
#     return response
#
#
# def readEchoNews():
#     siteUrl = "http://echo.msk.ru"
#     url = siteUrl + "/news/"
#     page = loadPage(url)
#     if page:
#         result = []
#         d = pq(page)
#         newsBlock = d("dl.frame.newsList.newsInside ul.list").children()
#         newsElements = []
#         for i in range(NEWS_COUNT): newsElements.append(newsBlock.eq(i))
#         for one in newsElements:
#             print(one.text())
#             a = one.find("a.name")
#             title = a.text().strip()
#             href = a.attr("href")
#             num = href.replace("/news/", "").replace("-echo.html", "")
#             descr = one.find("div.descr").text().strip().replace("...", ".")
#             text = u"%s. %s" % (title, descr)
#             text = ' '.join(re.findall(u"[a-zA-Zа-яА-Я\,\.]+", text))
#             result.append({'num': num, 'href': siteUrl + href, 'text': text})
#         return result
#     else:
#         return False
#
#
# print(readEchoNews())

# Grab(log_file='out.html').go('https://tsouz.belgiss.by/libs/site/AjaxServer/CertListFree.ajax.php')

url = 'https://tsouz.belgiss.by/#ui-tabs-1'
some_xpath = '//*'
logging.basicConfig(level=logging.DEBUG)
g = Grab()
g.setup(follow_location=True)
g.setup(debug=True)
g.setup(timeout=500, connect_timeout=22500)
g.setup(debug_post=True)
g.setup(verbose_logging=True)
# g.setup(post={'_search': 'false',
#               'nd': '1506610130720',
#               'page': '2',
#               'rows': '1000',
#               'sidx': 'cert_id',
#               'sord': 'desc',
#               })
g.setup(log_dir='tmp/r')
resp = g.go(url)
print(dir(resp))
#
# result = resp
# print(g.doc.json())
# print(g.doc.json())
#
# request = g.go(url, debug_post=True)
# print(request.body, result)
