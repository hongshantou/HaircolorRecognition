import os
from bs4 import BeautifulSoup
import time
import urllib
import random

def randname():
    source_str = '1234567890abcdefghijklmnopqrstuvwxyz'
    random.choice(source_str)
    name=''.join([random.choice(source_str) for x in range(20)])
    return name + '.jpg'

def geturl(link):
    body = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(body,'html.parser')
    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        try:
            src = a_tag['id'].lstrip('p')
            url = 'https://safebooru.org/index.php?page=post&s=view&id='+str(src)
            body2 = urllib.request.urlopen(url).read()
            soup2 = BeautifulSoup(body2,'html.parser')
            a_tags2 = soup2.find_all('a')
            for a_tag2 in a_tags2:
                src2 = a_tag2['href']
                if(src2.endswith('.jpg')) or (src2.endswith('.png')) or (src2.endswith('.jpeg')):
                    src2 = 'http:' + str(src2)
                    name = randname()
                    urllib.request.urlretrieve(src2,name)
                    print('[success]: {}'.format(name))
                    time.sleep(1.0)
        except:
            pass

def main():
    page = 200
    for i in range(page+1):
        link = 'hoge' #タグ検索した時のURLをここに入力
        geturl(link)

if __name__ == '__main__':
    main()
