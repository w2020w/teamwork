var uname_flag=false;
var upwd1_flag=false;
var upwd2_flag=false;

function  checkName() {

    //获取网页当中输入框里的内容
    uname  =  document.getElementById("uid").value;
    //通过value获取输入框中的值
    var reg=/^[a-z]{3,}$/;
    var result = reg.test(uname);
    //alert(result)
    span = document.getElementById("usid");
    if (result==true){
        //将用户名发送到服务器端，校验用户名是否存在
        //http://127.0.0.1:5000/checkName?uname='xiaoming'
        //1.发送的请求和用户名   2.接收后端传递过来的数据
       $.getJSON("checkUName?name="+uname,function(res) {

            result = ""+res;
           if(result=="true"){

               span.innerHTML="<font color='red'>名字已经存在</font>";
               uname_flag = false;
           }else{

               span.innerHTML="<font color='green'>可以注册</font>";
               uname_flag = true;
           }
       })

    }else{
        span.innerHTML="<font color='red'>用户名需由小写字母组成且长度至少三位</font>";
        uname_flag = false;
    }
}

    function checkmyPwd() {
        mypwd = document.getElementById("myid").value;
        var reg=/^[A-Za-z0-9]{8,}$/;
        var result = reg.test(mypwd);
        //alert("密码长度至少是八位")
        span = document.getElementById("upid");
        if (result==true){
            span.innerHTML="<font color='green'>密码格式正确</font>";
            upwd1_flag=true;
        }else {
            span.innerHTML="<font color='red'>密码长度至少是8位</font>";
            upwd1_flag=false;
        }
    }

    function checkmyPwd1() {
        mypwd1 = document.getElementById("myid").value;
        var reg=/^[A-Za-z0-9]{8,}$/;
        var result = reg.test(mypwd1);
        //alert("密码长度至少是8位")
        span = document.getElementById("upid1");
        if (result==true){
            span.innerHTML="<font color='green'>密码格式正确</font>";
            upwd2_flag=true;
        }else {
            span.innerHTML="<font color='red'>密码长度至少是8位</font>";
            upwd2_flag=false;
        }
    }
   function checkAll() {
    if(uname_flag==true & upwd1_flag==true & upwd2_flag==true){
        alert("true");
        return true;
    }else{
        alert("false");
        return false;
    }
}
