var uname_flag=false;
var upwd1_flag=false;
var upwd2_flag=false;

    function checkName() {
        uname = document.getElementById(uid).value
        var result = reg.test(uname)
        //alert(result)
        span = document.getElementById("sid")
        if (result == true) {
            //将用户名发送到服务器端，校验用户名是否存在
            $getJSON("checkUName?name=" + uname, function (res) {
                result = " " + res
                if (result == "true") {
                    span.innerHTML = "<font color='red'>用户名已经存在</font>"
                    uname_flag = false
                } else {
                    alert("2")
                    span.innerHTML = "<font color='green'>可以注册</font>"
                    uname_flag = true
                }
            })

        }
    }

    function checkPwd() {
        pwd = document.getElementById(pid).value
        var reg=/^[A-Za-z0-9]{8,}$/;
        var result = reg.test(pwd)
        //alert("密码长度至少是八位")
        span = document.getElementById("upid")
        if (result==true){
            span.innerHTML="<font color='green'>密码格式正确</font>"
            upwd1_flag=true
        }else {
            span.innerHTML="<font color='red'>密码长度至少是六位</font>"
            upwd1_flag=false
        }
    }

    function checkPwd1() {
        pwd1 = document.getElementById(pid1).value
        var reg=/^[A-Za-z0-9]{8,}$/;
        var result = reg.test(pwd1)
        //alert("密码长度至少是八位")
        span = document.getElementById("upid1")
        if (result==true){
            span.innerHTML="<font color='green'>密码格式正确</font>"
            upwd2_flag=true
        }else {
            span.innerHTML="<font color='red'>密码长度至少是六位</font>"
            upwd2_flag=false
        }
    }

    function checkAll() {
    if(uname_flag==true & upwd1_flag==true & upwd2_flag==true){
        alert("true")
        return true;
    }else{
        alert("false")
        return false;
          }
    }