'''
爬虫
author:钟毓
creat date:2020-8-8
update date:2020-8-13
'''


from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import urllib
import xlwt
#查找条件
findInfo=re.compile(r'<h2.*?>(.*?)</h2>',re.S)
findName=re.compile(r'<a href=".*?">(.*?)</a></h2>',re.S)
findJian=re.compile(r'<p>(.*?)</p>',re.S)
findImg=re.compile(r'src="(.*?)"',re.S)
findLink=re.compile(r'',re.S)


def main():
    baseurl="https://aten.net.cn/author/guofangkejidaxue/page/"
    datalist=getData(baseurl)
    savepath = "guofang.xls"
    saveData(datalist, savepath)

#从网站的源代码中获取我们想要的数据
def getData(baseurl):
    datalist = []
    for i in range(1, 6):
        url = baseurl + str(i)
        html = askURL(url)

        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div'):
            #print(item)
            data = []
            item = str(item)
            info=re.findall(findInfo,item)
            if(len(info)==1):#对我们想要的item进行数据采集
                name=re.findall(findName,item)
                if(len(name)==1):
                    cname=name[0]
                    jian=re.findall(findJian,item)[0]
                    img=re.findall(findImg,item)[0]
                else:
                    print()
                data.append(cname)
                data.append(jian)
                data.append(img)
            else:
                data.append('')
                data.append('')
                data.append('')

            datalist.append(data)

        # datalist.append(data)
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

    for i in range(0,450):
        print("第%d条" % i)
        data=datalist[i]
        for j in range(0,3):
            sheet.write(i+1,j,data[j])

    book.save(savepath)

# 执行main方法
main()