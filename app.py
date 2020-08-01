from flask import Flask, render_template, request, flash

import pymysql

app = Flask(__name__)

# 用户安全问题，设置key值，值随意给出，给的难道越大，破解与麻烦

app.secret_key = "123344"


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

            port=3306,

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

            rows = cls.execute("insert into myuser values(null,%s,%s,%s)", [name, pwd1, bdy])

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

        port=3306,

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

            return render_template("index.html", users=result)


@app.route("/findpwd")
def findpwd():
    name = request.values.get("uname")

    bdy = request.values.get("ubdy")

    print("name", name, "bdy:", bdy)

    # 到数据库中进行查询

    conn = pymysql.connect(

        host="wtwhz.chinanorth.cloudapp.chinacloudapi.cn",

        port=3306,

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

        port=3306,

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
        
#查询用户名是否存在
@app.route("/checkUName")
def checkUName():
    name = request.args.get("name")
    print(name)
    return  mydb.selectName(name)


if __name__ == '__main__':
    app.run()  # 启动服务器
