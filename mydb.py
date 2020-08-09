import  pymysql
def selectName(uname):
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
    cls.execute("select * from myuser where uname=%s ", [uname])
    result = cls.fetchone()
    if result is None:
        return "false"
    else:
       return "true"
