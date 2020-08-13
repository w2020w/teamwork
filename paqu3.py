'''
爬虫
author:钟毓
creat date:2020-8-6
update date:2020-8-13
'''


from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import urllib
import xlwt

def main():
    baseurl="http://ncu.fanya.chaoxing.com/portal/schoolCourseInfo/columnCourse?columnId=65390&pageNum="
    datalist=getData(baseurl)
    savepath = "nanchang.xls"
    saveData(datalist, savepath)

#查找条件
findName=re.compile(r'<a href=.*?>(.*?)</a>',re.S)
findTeacher=re.compile(r'<dd title="(.*?)">',re.S)
findDianji=re.compile(r'点击量：(.*?)\r\n        \t\t\t\t\t\t\t\t</div>',re.S)
findImag=re.compile(r'src="(.*?)" width=',re.S)
findLink=re.compile(r'<a href="(.*?)" target="_blank" title=',re.S)

#从网站的源代码中获取我们想要的数据
def getData(baseurl):
    datalist=[]
    for i in range(1,17):
        url=baseurl+str(i)
        html=askURL(url)

        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('dl'):
            #print(item)
            data=[]
            item=str(item)

            name=re.findall(findName,item)[1]
            teacher=re.findall(findTeacher,item)[0]
            dianji=re.findall(findDianji,item)[0]
            img=re.findall(findImag,item)[0]
            link=re.findall(findLink,item)[0]
            data.append(name)
            data.append(teacher)
            data.append(dianji)
            data.append(img)
            data.append(link)



            datalist.append(data)


        #datalist.append(data)
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
    col=("课程名","教师","点击量","图片","链接")
    for i in range(0,5):
        sheet.write(0,i,col[i])
    for i in range(0,130):
        print("第%d条" % i)
        data=datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j,data[j])

    book.save(savepath)

#执行main方法
main()