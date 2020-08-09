from flask import Flask, render_template, request, flash,session

import pymysql
import mydb
app = Flask(__name__)
app.config["SECRET_KEY"] = "123FIISUODFNOSAIFNHASIJDdasd"

# 用户安全问题，设置key值，值随意给出，给的难道越大，破解与麻烦
app.secret_key = "123344"

@app.route('/docourse1',methods=["POST"])
def course1():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=1")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse2',methods=["POST"])
def course2():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=2")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse3',methods=["POST"])
def course3():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=3")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse4',methods=["POST"])
def course4():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=4")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse5',methods=["POST"])
def course5():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=5")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse6',methods=["POST"])
def course6():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=6")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse7',methods=["POST"])
def course7():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=7")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse8',methods=["POST"])
def course8():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=8")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse9',methods=["POST"])
def course9():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=9")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/docourse10',methods=["POST"])
def course10():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=10")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)

@app.route('/ucourse1',methods=["POST"])
def ucourse1():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=265")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse2',methods=["POST"])
def ucourse2():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=266")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse4',methods=["POST"])
def ucourse3():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=267")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse4',methods=["POST"])
def ucourse4():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=268")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse5',methods=["POST"])
def ucours5():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=269")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse6',methods=["POST"])
def ucourse6():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=270")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse7',methods=["POST"])
def ucourse7():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=271")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse8',methods=["POST"])
def ucourse8():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=272")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse9',methods=["POST"])
def ucourse9():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=273")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/ucourse10',methods=["POST"])
def ucourse10():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=274")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)

@app.route('/icourse1',methods=["POST"])
def icourse1():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=436")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse2',methods=["POST"])
def icourse2():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=437")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse3',methods=["POST"])
def icourse3():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=438")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse4',methods=["POST"])
def icourse4():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=439")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse5',methods=["POST"])
def icourse5():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=440")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse6',methods=["POST"])
def icourse6():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=441")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse7',methods=["POST"])
def icourse7():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=442")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse8',methods=["POST"])
def icourse8():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=443")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse9',methods=["POST"])
def icourse9():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=444")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)
@app.route('/icourse10',methods=["POST"])
def icourse10():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=445")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information2.html' , u=result)

@app.route('/zcourse1',methods=["POST"])
def zcourse1():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=596")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse2',methods=["POST"])
def zcourse2():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=597")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse3',methods=["POST"])
def zcourse3():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=598")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse4',methods=["POST"])
def zcourse4():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=599")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse5',methods=["POST"])
def zcourse5():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=600")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse6',methods=["POST"])
def zcourse6():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=601")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse7',methods=["POST"])
def zcourse7():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=602")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse8',methods=["POST"])
def zcourse8():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=603")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse9',methods=["POST"])
def zcourse9():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=604")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/zcourse10',methods=["POST"])
def zcourse10():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=605")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)

@app.route('/fcourse1',methods=["POST"])
def fcourse1():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=628")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse2',methods=["POST"])
def fcourse2():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=629")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse3',methods=["POST"])
def fcourse3():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=630")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse4',methods=["POST"])
def fcourse4():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=631")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse5',methods=["POST"])
def fcourse5():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=632")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse6',methods=["POST"])
def fcourse6():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=633")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse7',methods=["POST"])
def fcourse7():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=634")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse8',methods=["POST"])
def fcourse8():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=635")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse9',methods=["POST"])
def fcourse9():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=636")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)
@app.route('/fcourse10',methods=["POST"])
def fcourse10():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=637")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information4.html' , u=result)

@app.route('/gcourse1',methods=["POST"])
def gcourse1():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=789")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse2',methods=["POST"])
def gcourse2():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=790")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse3',methods=["POST"])
def gcourse3():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=791")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse4',methods=["POST"])
def gcourse4():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=792")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse5',methods=["POST"])
def gcourse5():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=793")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse6',methods=["POST"])
def gcourse6():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=794")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse7',methods=["POST"])
def gcourse7():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=795")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse8',methods=["POST"])
def gcourse8():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=796")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse9',methods=["POST"])
def gcourse9():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=797")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)
@app.route('/gcourse10',methods=["POST"])
def gcourse10():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=798")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information6.html' , u=result)

@app.route('/ncourse1',methods=["POST"])
def ncourse1():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=832")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse2',methods=["POST"])
def ncourse2():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=833")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse3',methods=["POST"])
def ncourse3():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=834")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse4',methods=["POST"])
def ncourse4():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=835")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse5',methods=["POST"])
def ncourse5():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=836")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse6',methods=["POST"])
def ncourse6():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=837")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse7',methods=["POST"])
def ncourse7():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=838")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse8',methods=["POST"])
def ncourse8():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=839")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse9',methods=["POST"])
def ncourse9():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=840")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)
@app.route('/ncourse10',methods=["POST"])
def ncourse10():

    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from course where id=841")
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('course_information.html' , u=result)




# 接收前端注册界面提交的数据


@app.route("/doUser", methods=["POST"])
def doUser():
    # 获取前端的用户名
    name = request.values.get("uname")

    pwd1 = request.values.get("upwd1")

    pwd2 = request.values.get("upwd2")

    bdy = request.values.get("ubdy")

    print("name", name, "pwd1:", pwd1)

    if pwd1 == pwd2:

        # 到数据库中进行查询

        conn = pymysql.connect(

            host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",

            port=3307,

            user="root",

            password="123456",

            db="mython",

            charset="utf8"

        )

        print(conn)

        cls = conn.cursor()

        # # 前端传递的数据，进行到数据库中进行验证

        cls.execute("select * from myuser where uname=%s ", [name])

        result = cls.fetchone()

        if result is None:

            #

            rows = cls.execute("insert into myuser (uid,uname,upwd,ubdy) values(null,%s,%s,%s)", [name, pwd1, bdy])

            conn.commit()

            flash("注册成功")

            return render_template("login.html")



        else:

            flash("用户已存在")

            return render_template("register.html")







    else:

        flash("输入密码不一致")

        return render_template("register.html")


# 显示登录界面


@app.route("/showLogin")
def showloign():
    return render_template("login.html")

@app.route("/showindex")
def showindex():
    return render_template("index.html")

@app.route("/showcourselist1")
def showcourselist1():
    return render_template("courselist1.html")

@app.route("/showcourselist2")
def showcourselist2():
    return render_template("courselist2.html")

@app.route("/showcourselist3")
def showcourselist3():
    return render_template("courselist3.html")

@app.route("/showcourselist4")
def showcourselist4():
    return render_template("courselist4.html")

@app.route("/showcourselist5")
def showcourselist5():
    return render_template("courselist5.html")

@app.route("/showcourselist6")
def showcourselist6():
    return render_template("courselist6.html")

@app.route("/showcourselist7")
def showcourselist7():
    return render_template("courselist7.html")

@app.route("/doregist")
def doregist():
    return render_template("register.html")


@app.route("/dofindpwd")
def dofindpwd():
    return render_template("findpwd.html")


# 检测登录是否成功


@app.route("/doLogin", methods=["POST"])
def doLogin():
    # 获取前端提交的用户名和密码

    name = request.form.get("uname")

    pwd = request.form.get("upwd")

    print(name, pwd)

    # 到数据库中进行校验

    conn = pymysql.connect(

        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",

        port=3307,

        user="root",

        password="123456",

        db="mython",

        charset="utf8"

    )

    print(conn)

    cls = conn.cursor()

    # 前端传递的数据，进行到数据库中进行验证

    cls.execute("select * from myuser where uname=%s ", [name])

    result = cls.fetchone()

    if result is None:

        flash("用户未注册")

        return render_template("register.html")



    else:

        cls.execute("select * from myuser where uname=%s and upwd=%s", [name, pwd])

        result = cls.fetchone()

        if result is None:

            # 用户名和密码不对

            flash("user or password  not  true")

            return render_template("login.html")



        else:

            flash("登录成功")

            cls.execute("select * from myuser ")

            result = cls.fetchall()

            conn.close()
            session["name1"] = name

            return render_template("index.html", users=result)


@app.route("/findpwd")
def findpwd():
    name = request.values.get("uname")

    bdy = request.values.get("ubdy")

    print("name", name, "bdy:", bdy)

    # 到数据库中进行查询

    conn = pymysql.connect(

        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",

        port=3307,

        user="root",

        password="123456",

        db="mython",

        charset="utf8"

    )

    print(conn)

    cls = conn.cursor()

    # 前端传递的数据，进行到数据库中进行验证

    cls.execute("select * from myuser where uname=%s and ubdy=%s", [name, bdy])

    result = cls.fetchone()

    if result is None:

        flash("验证错误，请重新注册")

        return render_template("register.html")



    else:

        return render_template("resetpwd.html")


@app.route("/resetpwd", methods=["POST"])
def resetpwd():
    name = request.form.get("uname")

    pwd1 = request.form.get("upwd1")

    pwd2 = request.form.get("upwd2")

    conn = pymysql.connect(

        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",

        port=3307,

        user="root",

        password="123456",

        db="mython",

        charset="utf8"

    )

    print(conn)

    cls = conn.cursor()

    cls.execute("select * from myuser where uname=%s ", [name])

    result = cls.fetchone()

    if result is None:

        flash("用户名不存在，请重新注册")

        return render_template("register.html")



    else:

        if pwd1 == pwd2:

            flash("重置成功")

            rows = cls.execute("update myuser set upwd =%s where uname=%s", [pwd1, name])

            conn.commit()

            print("name", name, "pwd1:", pwd1)

            return render_template("login.html")



        else:

            flash("输入密码不一致")

            return render_template("resetpwd.html")


# 查询用户名是否存在

@app.route("/checkUName")
def checkUName():
    name = request.args.get("name")

    print(name)

    return mydb.selectName(name)


@app.route("/showmycourse")
def showmycourse():
    name = session.get("name1")
    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )

    cls = conn.cursor()
    cls.execute("select * from myuser where uname=%s", [name])
    result = cls.fetchone()
    conn.close()
    print(result)
    return render_template('mycourse.html', m=result)


@app.route("/ajax",methods=["POST"])
def get_ajax():

    coursename = request.values.get("coursename")

    print(coursename)
    name = session.get("name1")
    print(name)


 #   return 'successful'




    conn = pymysql.connect(
        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",
        port=3307,
        user="root",
        password="123456",
        db="mython",
        charset="utf8"
    )
    print(conn)
    cls = conn.cursor()
    cls.execute("select mycourse1 from myuser where uname=%s", [name])
    result = cls.fetchone()
    print(result)
    result1=result[0]
    print(result1)
    if result1 is None:

        rows = cls.execute("update myuser set mycourse1 =%s where uname=%s", [coursename, name])
        conn.commit()
        return render_template('course_information.html')

    else:
        cls.execute("select mycourse2 from myuser where uname=%s", [name])
        result = cls.fetchone()
        result1 = result[0]
        if result1 is None:
            rows = cls.execute("update myuser set mycourse2 =%s where uname=%s", [coursename, name])
            conn.commit()
            return render_template('course_information.html')
        else:
            cls.execute("select mycourse3 from myuser where uname=%s", [name])
            result = cls.fetchone()
            result1 = result[0]
            if result1 is None:
                rows = cls.execute("update myuser set mycourse3 =%s where uname=%s", [coursename, name])
                conn.commit()
                return render_template('course_information.html')
            else:
                cls.execute("select mycourse4 from myuser where uname=%s", [name])
                result = cls.fetchone()
                result1 = result[0]
                if result1 is None:
                    rows = cls.execute("update myuser set mycourse4 =%s where uname=%s", [coursename, name])
                    conn.commit()
                    return render_template('course_information.html')
                else:
                    cls.execute("select mycourse5 from myuser where uname=%s", [name])
                    result = cls.fetchone()
                    result1 = result[0]
                    if result1 is None:
                        rows = cls.execute("update myuser set mycourse5 =%s where uname=%s", [coursename, name])
                        conn.commit()
                        return render_template('course_information.html')
                    else:
                        return render_template('course_information.html')


if __name__ == '__main__':
    app.run()  # 启动服务器
