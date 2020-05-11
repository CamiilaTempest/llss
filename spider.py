import bs4
import requests
import time
import re
def GET_URL(url):#捕获页面信息文本
    try:
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        x= requests.get(url,headers=user_agent,timeout=30)
        x.encoding=x.apparent_encoding
        x.raise_for_status()
        return x.text
    except:
        print('Sorry')
def LINKS(Links,url): #捕获里面的每一部的链接
    Soup = bs4.BeautifulSoup(GET_URL(url),'lxml')
    for X in Soup.find_all('header',class_='entry-header'):
        for XXX in X.find_all('h1'):
            Links.append(XXX.a.get('href'))#存储到Link列表里
def Down(Links,down_Links):#获取磁力链接，并返回
    rules=re.compile('\w{40}',re.S)
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    for url in Links:
        r = requests.get(url, headers=user_agent, timeout=30)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        X = soup.find('div',class_='entry-content')
        X=str(X)
        string_X = re.sub("[\u4e00-\u9fa5]", "",X)
        for a in re.findall(rules,string_X):
            down_Links.append(a)
def Write(content):#写入
    with open('NeiRon.txt','a+',encoding='utf-8') as f :
        f.write('\tmagnet:?xt=ur一n:btih:'+content+'\n')
def main(A):
    url = 'https://llss.li/wp/category/all/anime/page/' + str(A)
    Links = []
    down_Links = []
    new_down_Links = []
    LINKS(Links,url)
    Down(Links,down_Links)
   # print(down_Links)
    for x in down_Links:
        if len(x)>40:
            pass
        else:
            if x not in new_down_Links:
                new_down_Links.append(x)
                Write(x)
                print(str(x)+'    OK      ')
            else:
                continue




if __name__ =='__main__':
    for XXX in range(2):         #range里面的数字是下载页数,需要几页自己修改
        main(A=XXX+1)
        time.sleep(1) #延迟

