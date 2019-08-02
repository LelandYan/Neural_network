# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/2 15:53'
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))  # 表头信息
    for i in range(num):  # 便利列表中的每一项
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))  # 格式化输出

def main():
    uinfo = []  # 大学信息列表
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)  # 调用函数获取页面信息
    fillUnivList(uinfo, html)  # 信息放入uninfo的列表中
    printUnivList(uinfo, 20)  # 打印大学信息，只打印20个

if __name__ == '__main__':
    main()