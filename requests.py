import requests

# url = 'https://tsouz.belgiss.by/libs/site/AjaxServer/CertListFree.ajax.php'
# url = 'https://tsouz.belgiss.by/'
# payload = {'_search': 'false',
#            'nd': '1506610130720',
#            'page': '2',
#            'rows': '1000',
#            'sidx': 'cert_id',
#            'sord': 'desc',
#            }
#
# r = requests.post(url, data=payload)
# print(r.text)

r = requests.get("http://ya.ru")
print(r.text)
