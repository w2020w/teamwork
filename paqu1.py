import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import urllib
import xlwt



def main():
    baseurl="http://opencourse.pku.edu.cn/course/opencourse2/classification.html"
    datalist=getData(baseurl)
    savepath="hahoho.xls"
    saveData(datalist,savepath)

findLink=re.compile(r'<a href="..(.*?)">',re.S)
findName=re.compile(r'<td><a href=".*?">(.*?)</a></td>',re.S)
findTeacher=re.compile(r'<td>(.*?)</td>')
findYear=re.compile(r'<td>(.*?)</td>')



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

        link = re.findall(findLink, item)

        year = re.findall(findYear, item)
        if (len(year) == 4):
            cyear = year[3]
            clink=year[0]
            cname=year[1]
            cname=re.sub('<a href=".*?">','',cname)
            cname=re.sub('</a>','',cname)
            cteacher=year[2]
            data.append(clink)
            data.append(cname)
            data.append(cteacher)
            data.append(cyear)
            data.append(link)

        else:
            data.append('')
            data.append('')
            data.append('')
            data.append('')
            data.append('')

        datalist.append(data)
    #print(datalist)
    return datalist


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


def saveData(datalist,savepath):
    print("save...")
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet('haha',cell_overwrite_ok=True)
    col=("序号","课程名","教师","录制年份","链接")
    for i in range(0,5):
        sheet.write(0,i,col[i])
    for i in range(0,53):
        print("第%d条"%i)
        data=datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j,data[j])

    book.save(savepath)


main()









