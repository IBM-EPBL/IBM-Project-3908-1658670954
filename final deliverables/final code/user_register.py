#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb;cgitb.enable()
conn=pymysql.connect(host="localhost", user="root", password="", database="agremo")
cur=conn.cursor()
q1="""select max(id) from register"""
cur.execute(q1)
r=cur.fetchone()
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
</div>""")



print("""

  <div class="container" style="margin-top:10px;height:600px;width:100%">
    

  <img src="regbg.jpeg" style="height:100%;width:100%;" >
 
  <form action="#" style="margin-top:-500px;margin-left: 550px;" autocomplete="off">  
  
   
    <b>Email:  </b>"""%(id))
print("""
    <input type="email" id="email" name="username"/> <br>    
    <br>  
<b>Password:  </b>
    <input type="Password" id="pass" name="password"> <br>   
    <br>  
<b>Re-type password: </b> 
    <input type="Password" id="repass" name="repass">
    <br><br>
	<b> <label> Name: </label></b>      
    <input type="text" name="name" size="15"/> <br> <br>  
    <label>   
    <b> Gender :  </b>
        </label>
        <b><input type="radio" name="male"/> Male   
        <input type="radio" name="female"/> Female 
        <input type="radio" name="other"/> Other </b> 
        <br>  
        <br>  
          
        <label>  
    
   
        <b>Phone :  </b>
    </label>  
    <input type="text" name="country code"  value="+91" size="2"/>   
    <input type="text" name="phone" size="10"/> <br> <br>  
   
     

<b> <label> State: </label>   </b>      
    <input type="text" name="state" size="15"/> 
    
     <br> <br>  
    <b><a href="user_login.html"> <input type="button" value="Submit" style="margin-left: 80px;"/> </a> </b>
    </form>  

</div>


</body>
</html>"""%(id))
f=cgi.FieldStorage()
sub=f.getvalue("submit")
if sub !=None:
    userid = f.getvalue("id")
    username = f.getvalue("username")
    password = f.getvalue("password")
    name = f.getvalue("name")
    gender = f.getvalue("gender")
    phone = f.getvalue("phone")
    state= f.getvalue("state")
 


 


        q = """insert into register(id,username,password,name,gender,phone,state)values('%s','%s','%s','%s','%s','%s','%s' )"""%(id,username,password,name,gender,state)
        cur.execute(q)
        conn.commit()
        conn.close()

        

        print("""
          <script>
             alert("Registration successful");
             location.href="user_login.py";
          </script>
        """)
    else:
        print("""
          <script>
             alert("Login invalid");
             location.href="user_register.py";
          </script>   
           """)
