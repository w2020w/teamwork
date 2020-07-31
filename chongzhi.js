var upwd1_flag=false;
var upwd2_flag = false;

function  checkPwd(){
    pwd = document.getElementById("pid").value;
    var reg=/^[A-Za-z0-9]{8,}$/;
    var result = reg.test(pwd);
    //alert("密码长度至少是8位")
    span = document.getElementById("sid");
    if (result==true){
        span.innerHTML="<font color='green'>密码格式正确</font>";
        upwd1_flag=true;
    }else{
        span.innerHTML="<font color='red'>密码长度至少是8位</font>";
        upwd1_flag=false;
    }

}

function  checkPwd1(){
    pwd = document.getElementById("pid1").value;
    var reg=/^[A-Za-z0-9]{8,}$/;
    var result = reg.test(pwd);
    //alert("密码长度至少是8位")
    span = document.getElementById("sid1");
    if (result==true){
        span.innerHTML="<font color='green'>密码格式正确</font>";
        upwd2_flag=true;
    }else{
        span.innerHTML="<font color='red'>密码长度至少是8位</font>";
        upwd2_flag=false;
    }

}

function checkAll() {
    if(upwd1_flag==true & upwd2_flag==true){
        alert("true")
        return true;
    }else{
        alert("false")
        return false;
    }
}