#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb;cgitb.enable()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <title>AGRIMUS</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="styles/styles/css/style.css">
<link rel="icon"type="image/ico" href="images/mus.png">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<link rel="stylesheet" href="https://bootstrap.bundle.min.js/bootstrap.bundle.js">
<link rel="stylesheet" type="text/css" href="styles/bootstrap/css/bootstrap.min.css">
</head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<script src="styles/styles/js/jquery.min.js"></script>
<script src="styles/styles/js/bootstrap.min.js"></script>
<style>

.header1{
height:90px;

background-color:black;
border:2px solid black;
}

.rel{

position:absolute;
top:10%;
margin-left:0px;
}




.glow {
  font-size: 50px;
  color: #fff;
  text-align: center;
  animation: glow 1s ease-in-out infinite alternate;
}

@-webkit-keyframes glow {
  from {
    text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #e60073, 0 0 40px #e60073, 0 0 50px #e60073, 0 0 60px #e60073, 0 0 70px #e60073;
  }

  to {
    text-shadow: 0 0 20px #fff, 0 0 30px #ff4da6, 0 0 40px #ff4da6, 0 0 50px #ff4da6, 0 0 60px #ff4da6, 0 0 70px #ff4da6, 0 0 80px #ff4da6;
  }
}
body
{
background-image:url('images/download.jpg');
background-repeat:no-repeat;
background-size:cover;
}


</style>
<body>

<div>
      <div class="header1">
<img class="img-circle" style="margin-top:3px"  src="logo.jpeg" alt="logo" width="75px" height="75px">
<div class="rel">
<h1 width="100%" style="margin-left:500px; color:white; margin-top:-50px" class="glow"><b class="text-default" style="fontsize:40px" >AGRIMUS</b></h1>
</div>
</div>
</div>





  <div class="container" style="margin-top:10px;height:600px;width:100%">
    

  <img src="loginbg.jpg" style="height:100%;width:100%;" >
  <form action="#" autocomplete="off" style="margin-top:-500px;margin-left:500px">
    <div class="field">
      <span class="fa fa-user"></span>
     <label style="font-family:'Times New Roman', Times, serif;font-size:20px">Enter the username:</label> <input type="text"  name="username" required placeholder="Username">
    </div>
    <div class="field space">
      <span class="fa fa-lock"></span>
      <label style="font-family:'Times New Roman', Times, serif;font-size:20px">Enter the password:</label> <input type="password" class="pass-key" name="password" required placeholder="Password">
      
    </div>
    <br>
    <div class="field">
      <input type="submit"  name="submit" value="LOGIN" style="margin-left:100px" onclick = "location.href ='details.html';">
      <input type="reset" value="CANCEL" onclick = "location.href ='index.html';">
    </div>
    <br>
	
    
  </form>
  
</div>
<script>
      const pass_field = document.querySelector('.pass-key');
      const showBtn = document.querySelector('.show');
      showBtn.addEventListener('click', function(){
       if(pass_field.type === "password"){
         pass_field.type = "text";
         showBtn.textContent = "HIDE";
         showBtn.style.color = "#3498db";
       }else{
         pass_field.type = "password";
         showBtn.textContent = "SHOW";
         showBtn.style.color = "#222";
       }
      });
    </script>


</body>

</html>""")
conn = pymysql.connect(host="localhost", user="root", password="", database="agremo")
cur = conn.cursor()
f = cgi.FieldStorage()
username = f.getvalue("username")
password = f.getvalue("password")
v = f.getvalue("submit")
if v != None:

    q = """select id from register where username='%s' and password='%s'""" % (username, password)
    cur.execute(q)
    r = cur.fetchone()
    if r != None:
        print("""
                    <script>
        			  alert("Login successfull");
                      location.href="details.html";
                    </script>
        """)
    else:
        print("""
                    <script>
                      alert("Login invalid");
                      location.href="user_login.py";
                    </script>
        """)

