import requests

url = 'https://tsouz.belgiss.by/#ui-tabs-1'
# url = 'https://tsouz.belgiss.by/'
payload = {'_search': 'false',
           'nd': '1506610130720',
           'page': '2',
           'rows': '1000',
           'sidx': 'cert_id',
           'sord': 'desc',
           }


r = requests.post(url, data=payload)
print(r.text)


