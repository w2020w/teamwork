'''
爬虫
author:钟毓
creat date:2020-8-7
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
    baseurl="http://jpkc.fudan.edu.cn/13/list.htm"
    datalist=getData(baseurl)
    savepath="fudan.xls"
    saveData(datalist,savepath)

#查找条件
findInfo=re.compile(r'<td.*?>(.*?)</td>',re.S)
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

        info=re.findall(findInfo,item)
        #link=re.findall(findLink,item)

        if(len(info)==4):#对我们想要的item进行数据采集
            link = re.findall(findLink, item)
            #print(link)
            name=info[0]
            name=re.sub('</a>','',name)
            name=re.sub('<a.*?>','',name)
            name=re.sub('<span.*?>','',name)
            name=re.sub('</span>','',name)
            name=re.sub('<p.*?>','',name)
            name=re.sub('</p>','',name)
            teacher=info[1]
            teacher=re.sub('<p.*?>','',teacher)
            teacher=re.sub('</p>','',teacher)
            teacher=re.sub('<span.*?>','',teacher)
            teacher=re.sub('</span>','',teacher)
            xueyuan=info[2]
            xueyuan=re.sub('<p.*?>','',xueyuan)
            xueyuan=re.sub('</p>','',xueyuan)
            xueyuan=re.sub('<span.*?>','',xueyuan)
            xueyuan=re.sub('</span>','',xueyuan)
            time=info[3]
            time=re.sub('<p.*?>','',time)
            time=re.sub('</p>','',time)
            time=re.sub('<span.*?>','',time)
            time=re.sub('</span>','',time)
            time=re.sub('<br/>','',time)
            data.append(name)
            data.append(teacher)
            data.append(xueyuan)
            data.append(time)
            if(len(link)==1):
                clink=link[0]
                data.append(clink)
            else:
                data.append('')
        else:
            data.append('')
            data.append('')
            data.append('')
            data.append('')
            data.append('')


            #print(link)


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

    for i in range(0,164):
        print("第%d条"%i)
        data=datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j,data[j])

    book.save(savepath)


# 执行main方法
main()