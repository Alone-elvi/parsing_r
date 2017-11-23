import csv
from grab import Grab

FILENAME = "urls.csv"

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row[0])
#             if url in row:
#                 return False
# g = Grab()
# url = 'https://news.yandex.ru/index.rss'
# g.go(url)
#
# print (g.doc.text_search(u'Яндекс'.encode('utf-8'), byte=True))