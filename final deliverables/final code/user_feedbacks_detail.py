#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb;cgitb.enable()
conn=pymysql.connect(host="localhost", user="root", password="", database="agremo")
cur=conn.cursor()
q1="""select max(id) from feedback"""
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

background-repeat:no-repeat;
background-size:cover;
height:100%;
width:100%;
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
    

  <img src="bgdetails.png" style="height:100%;width:100%;" >
  
</div>

<style>
body {
  font-family: "Lato", sans-serif;
}

.sidebar {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
   margin-top:100px;
}

.sidebar a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
  transition: 0.3s;
}

.sidebar a:hover {
  color: #f1f1f1;
}

.sidebar .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
 
}

.openbtn {
  font-size: 20px;
  cursor: pointer;
  background-color: #111;
  color: white;
  padding: 10px 15px;
  border: none;
}

.openbtn:hover {
  background-color: #444;
}

#main {
  transition: margin-left .5s;
  padding: 16px;
}

/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidebar {padding-top: 15px;}
  .sidebar a {font-size: 18px;}
}
</style>



<div id="mySidebar" class="sidebar">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×</a>
  <a href="user_details.html">User Details</a>
  <a href="visualisations.html">Visualisations</a>
  <a href="https://us1.ca.analytics.ibm.com/bi/?perspective=dashboard&pathRef=.my_folders%2Fmain%2Bproject&action=view&mode=dashboard&subView=model000001847bf34b47_00000000">Dashboard</a>
  <a href="https://us1.ca.analytics.ibm.com/bi/?pathRef=.my_folders%2FCrop%2Bproduction%2Breport%2Banalysis&action=edit">Story</a>
  <a href="user_feedbacks_detail.py">Feedbacks</a>
</div>

<div id="main" style="margin-top:-620px">
  <button class="openbtn" onclick="openNav()">☰ </button>  
  
</div>
<table style="margin-left:200px;width:100%">

<tr>
<th>ID</th>
<th>Name</th>
<th>State</th>%r[0],%r[1],%r[2]""")



<script>
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}
</script>
   



</body>
</html>