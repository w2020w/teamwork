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
    baseurl="http://netclass.csu.edu.cn/Video/video/Csu.aspx"
    datalist=getData(baseurl)
    savepath="zhongnan.xls"
    saveData(datalist,savepath)

#查找条件
findInfo=re.compile(r'<td.*?>(.*?)</td>',re.S)

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
        if(len(info)==5):#对我们想要的item进行数据采集
            name=info[1]
            name=re.sub('<font.*?><a href.*?>','',name)
            name=re.sub('</a></font>','',name)
            teacher=info[2]
            teacher=re.sub('<font.*?>','',teacher)
            teacher=re.sub('</font>','',teacher)
            xueyuan=info[3]
            xueyuan = re.sub('<font.*?>', '', xueyuan)
            xueyuan = re.sub('</font>', '', xueyuan)
            link=info[1]
            link=re.sub('<font.*?>','',link)
            link=re.sub('<a href="','',link)
            link=re.sub('">.*?</a></font>','',link)
            data.append(name)
            data.append(teacher)
            data.append(xueyuan)
            data.append(link)

        else:
            data.append('')
            data.append('')
            data.append('')
            data.append('')

        datalist.append(data)
    print(datalist)
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
    col=("课程名","教师","学院","链接")
    for i in range(0,4):
        sheet.write(0,i,col[i])
    for i in range(0,52):
        print("第%d条"%i)
        data=datalist[i]
        for j in range(0,4):
            sheet.write(i+1,j,data[j])

    book.save(savepath)
    
#执行main方法
main()

