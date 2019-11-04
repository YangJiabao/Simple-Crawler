import requests
from bs4 import BeautifulSoup
import os

txt_list=[]
href_list=[]
def list1():
    url = 'https://www.biquyun.com/2_2016/'
    req = requests.get(url,verify=False)
    req.encoding = 'gbk'
    #print(req.text)
    soup = BeautifulSoup(req.text, 'lxml').find('div', id='list').find_all('a')
    #soup = BeautifulSoup(req.text, 'lxml').find('div', id='content')
    #print(soup.text.replace('\xa0'*8,'\n\n'))
    for i in soup[8:]:
        #print(i.text)
        href_list.append(url + i['href'])
        txt_list.append(i.text)
    get1()

def get1():
    for (i,j) in zip(href_list,txt_list):
        rec = requests.get(i,verify=False)
        rec.encoding = 'gbk'
        soup = BeautifulSoup(rec.text, 'lxml').find('div', id='content')
        text1 = soup.text.replace('\xa0'*8,'\n\n')
        os.chdir(os.path.join("E:\zhetian"))  ##切换到目录
        with open('zhetian.txt', 'a+', encoding='utf-8') as f:
            f.write(j + '\n')
            f.writelines(text1)
            f.write('\n\n')

def main():
    list1()

if __name__ == '__main__':
    main()
