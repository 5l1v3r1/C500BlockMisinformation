# Author : Bui Quy Bao
import requests, re, sys

def Get_ID_Facebook(url):
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    return idre.findall(page.content)[0]

url = str(sys.argv[1])
print Get_ID_Facebook(url)

