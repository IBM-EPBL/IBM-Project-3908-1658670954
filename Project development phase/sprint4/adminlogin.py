#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb;cgitb.enable()
print("""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>LOGIN FORM</title>
	<style>
	  .head{
	  background-image:url('images/he.jpg');
	  position:fixed;
	  width:100%;
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
	  
	  
	</style>
    <link rel="stylesheet" href="styles/style.css">
   <script src="https://kit.fontawesome.com/a076d05399.js"></script>
   <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" type="text/css" href="styles/bootstrap/css/bootstrap.min.css">
  <link  rel="icon" type="logo/icon" href="images/mus.png">
  
  <script src="styles/bootstrap/jquery/jquery.min.js"></script>
  <script src="styles/bootstrap/js/bootstrap.min.js"></script>

  </head>
  <body>
  
  <div class="full">
  
	<div class="container-fluid" class="jumbotron text-center">
	<div class="head">
    <div class="row">
	
		<div class="col-sm-2"><img class="img-circle" height="90px" width="90px" 
			src="images/mus.png"></div>
			<div class="col-lg-10"><h1 width="100%" style="margin-left:-250px; color:white" class="glow"><b class="text-default">MUSICAL SHOWROOM</b></h1></div>
			</div>
			</div>
			</div> 	
			</div>
<div class="container-fluid">	
<div class="row">		
    <div class="bg-img"  style="background: url('images/bg.jpg')">
      <div class="content">
        <img src='images/icon.jpg' class="img-circle" height="100px" width="100px" style="margin-bottom:10px">
        <form action="#" autocomplete="off">
          <div class="field">
            <span class="fa fa-user"></span>
            <input type="text"  name="uname" required placeholder="Username">
          </div>
          <div class="field space">
            <span class="fa fa-lock"></span>
            <input type="password" class="pass-key" name="psw" required placeholder="Password">
            <span class="show">SHOW</span>
          </div>
          <br>
          <div class="field">
            <input type="submit"  name="submit" value="LOGIN">
          </div>
		  <br>
		  <div class="field">
            <input type="reset" value="CANCEL" onclick = "location.href ='index.html';">
          </div>
        </form>
		<br>
       
        
      </div>
    </div>
	</div>
	</div>
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
</html>
""")
conn=pymysql.connect(host="localhost",user="root",password="",database="musical")
cur=conn.cursor()
f=cgi.FieldStorage()
usr = f.getvalue("uname")
pwd = f.getvalue("psw")
v = f.getvalue("submit")
if v != None:

    q = """select id from admin where uname='%s' and psw='%s'"""%(usr, pwd)
    cur.execute(q)
    r = cur.fetchone()
    if r != None:
        print("""
                    <script>
        			alert("Login successfull");
                    location.href="admindashboard.py";
                    </script>
                """)
    else:
        print("""
                    <script>
                      alert("Login invalid");
                      location.href="adminlogin.py";
                    </script>
                """)



