'''
爬虫
author:钟毓
creat date:2020-8-8
update date:2020-8-13
'''


import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import urllib
import xlwt

def main():
    baseurl="http://jwc.nankai.edu.cn/2020/0205/c5106a264802/page.htm"
    datalist=getData(baseurl)
    savepath="nankai.xls"
    saveData(datalist,savepath)

#查找条件
findName=re.compile(r'<span.*?>(.*?)</span>',re.S)
findLink=re.compile(r'<a href="(.*?)"',re.S)


#从网站的源代码中获取我们想要的数据
def getData(baseurl):
    datalist=[]
    # for i in range(0,10):
    url=baseurl
    html=askURL(url)

    soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('tr'):
        #print(item)
        data=[]
        item=str(item)
        name=re.findall(findName,item)
        link = re.findall(findLink, item)
        if(len(name)==5):#对我们想要的item进行数据采集
            cname=name[1]
            teacher=name[2]
            pingtai=name[3]
            pingtai=re.sub('<span.*?>','',pingtai)
            if(len(link)==1):
                clink=link[0]
            else:
                clink=''
            data.append(cname)
            data.append(teacher)
            data.append(pingtai)
            data.append(clink)
        else:
            data.append('')
            data.append('')
            data.append('')
            data.append('')

        datalist.append(data)
    #print(datalist)
    return datalist

#从网站获取源代码
def askURL(url):
    #head
    request=urllib.request.Request(url)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#保存数据到Excel表格
def saveData(datalist,savepath):
    print("save...")
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet('haha',cell_overwrite_ok=True)

    for i in range(0,51):
        print("第%d条"%i)
        data=datalist[i]
        for j in range(0,4):
            sheet.write(i+1,j,data[j])

    book.save(savepath)


# 执行main方法
main()