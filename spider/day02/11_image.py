import requests
import os
from fake_useragent import UserAgent
url = 'http://static.1sapp.com/qupost/image/20170320/fa/fab14f3be88f2d969877efc3743230af5c32e442.jpg'
headers = { 'User-Agent':UserAgent().random }
html = requests.get(url=url,headers=headers).content

directory = '/home/tarena/images/赵丽颖/'
if not os.path.exists(directory):
    os.makedirs(directory)

filename = directory + url[-44:]
with open(filename,'wb') as f:
    f.write(html)

# /home/tarena/images/





