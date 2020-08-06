import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import urllib
import xlwt

def main():
    baseurl="http://cc.scu.edu.cn/G2S/Showsystem/CourseExcellence.aspx?size=4"
    datalist=getData(baseurl)
    savepath = "sichuan.xls"
    saveData(datalist, savepath)

findInfo=re.compile(r'<td.*?>(.*?)</td>')

def getData(baseurl):
    datalist=[]
    # for i in range(0,10):
    url=baseurl
    html=askURL(url)

    soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('tr'):
        data=[]
        item=str(item)
        info=re.findall(findInfo,item)
        if(len(info)==11):
            xuhao=info[0]
            name=info[1]
            name=re.sub('<span.*?></span><a.*?>','',name)
            name=re.sub('</a><div class="clear"></div>','',name)
            web=info[1]
            web=re.sub('<span.*?></span><a.*?href="..','',web)
            web=re.sub('".*?</a>','',web)
            web=re.sub('<div class="clear"></div>','',web)
            jibie=info[2]
            teacher=info[4]
            xueyuan=info[6]
            update=info[7]
            dianji=info[8]
            data.append(xuhao)
            data.append(name)
            data.append(jibie)
            data.append(teacher)
            data.append(xueyuan)
            data.append(update)
            data.append(dianji)
            data.append(web)
        else:
            data.append('')
            data.append('')
            data.append('')
            data.append('')
            data.append('')
            data.append('')
            data.append('')
            data.append('')


        datalist.append(data)
    #print(datalist)
    return datalist

def askURL(url):
    head={"User-Agent":""}
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
    col=("序号","课程名","级别","教师","学院","更新日期","点击量","链接")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,171):
        print("第%d条"%i)
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)

main()