import  pymysql
def selectName(uname):
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        db="mypython",
        charset="utf8"
    )
    print(conn)
    cls = conn.cursor()
    # 前端传递的数据，进行到数据库中进行验证
    cls.execute("select * from myuser where uname=%s ", [uname])
    result = cls.fetchone()
    return result



def selectNameandPwd(uname,ubdy):
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        db="mypython",
        charset="utf8"
    )
    print(conn)
    cls = conn.cursor()
    # 前端传递的数据，进行到数据库中进行验证
    cls.execute("select * from myuser where uname=%s and ubdy=%s", [uname, ubdy])
    result = cls.fetchone()
    return result