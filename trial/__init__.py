# import requests, json
#
# data = {'userName':'sam@yopmail.com','password':'Qwerty11'}
# r = requests.post(url = 'https://cerebellum.medocity.net/v2/login', data = data)
# # print(r.status_code)
# print(r.json())
# dict = r.json()
# if len(dict)>1:
#     print(dict['session'])
#     print(len(dict['session']))
#     print(dict['message'])
#     dict2 = dict['message']
#     print(dict2['fullName'])

f = open('helloworld.html','w')

message = """


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=iso-8859-1"/>
<title>Wicked CSS 3d bar chart using only CSS3</title>
<link rel="stylesheet" type="text/css" href="css/style.css"/>
<style>

/* BASIC RESET */
ul,ol,li,h1,h2,h3,h4,h5,h6,pre,form,body,macbook,p,blockquote,fieldset,input{margin:0; padding:0;}

/* HTML ELEMENTS */
body { background: -moz-radial-gradient(#364D58,#000); background: -webkit-gradient(radial, center center,10,center center,1000, from(#364D58), to(#000)); color:#555; background-color:#151f23; }
h1 { font: bold 50px Helvetica, Arial, Sans-serif; text-align: center; color: #eee; text-shadow: 0px 2px 6px #333; }
h1 small{ font-size: 20px; text-transform:uppercase; letter-spacing: 14px; display: block; color: #ccc; margin-top:10px; }
h2 a { display: block; text-decoration: none; margin: 0 0 30px 0; font: italic 40px Georgia, Times, Serif;  text-align: center; color: #bfe1f1; text-shadow: 0px 2px 6px #333; }
h2 a:hover { color: #90bcd0; }

/* COMMON CLASSES */
.break { clear:both; }

/* WRAPPER */
#wrapper { width:800px; margin:40px auto; }

/* CONTENT */
#content { }
#content h2 { font: bold 30px Helvetica, Arial, Sans-serif; color:#eee; text-shadow: 0px 2px 6px #333; margin-left:400px; padding-top:20px; }

/* BAR CHART */
#bar { list-style:none; margin:70px 0 0 200px; width:400px; }
#bar li { margin-top:-40px; }

/* First top should have a different colour */
#bar li:first-child div.top { background-color:rgba(186,211,215,0.5); }

/* Last bottom should have a shadow */
#bar li:last-child div.bottom { -moz-box-shadow: 0 10px 10px hsla(0,0%,0%,.2); -webkit-box-shadow: 0 100px 30px hsla(0,0%,0%,.2); box-shadow: 0 100px 30px hsla(0,0%,0%,.2); }

/* Ellipse top */
#bar li div.top { background-color:rgba(140,172,176,0.5); position:relative;
	width:100px; height:40px; -moz-border-radius: 100px/40px; -webkit-border-radius: 100px 40px; border-radius: 100px/40px; }
#bar li div.top img { margin-left:18px; margin-top:-32px; display:none; }

/* Bar bottom */
#bar li div.bottom { background-color:rgba(184,203,205,0.5); margin-top:-40px; position:relative;
	width:100px; -moz-border-radius: 100px/40px; -webkit-border-radius: 100px 40px; border-radius: 100px/40px; }
#bar li div.bottom div.infobox { padding:40px 0 0 200px; }
#bar li div.bottom div.infobox h3 { font-family:Georgia,serif,Times; }
#bar li div.bottom div.infobox p { font-family:"Lucida Grande",Arial,Helvetica,Sans-Serif; }

/* General hover actions */
#bar li:hover div.top img { display:inline; }
#bar li:hover div.bottom div.infobox { color:#eee; text-shadow: 0px 5px 5px #111; }

/* iPhone bar */
#iphone div.top { z-index:99; }
#iphone div.bottom { z-index:98; height:150px; }
#iphone:hover div.top { z-index:999; background-color:#1f81ac; }
#iphone:hover div.bottom { z-index:998; background-color:#1a6c90;
	background:-moz-linear-gradient(-90deg, #1a6c90, #14506b); background:-webkit-gradient(linear, 0 top, 0 bottom, from(#1a6c90), to(#14506b)); }

/* MacBook bar */
#macbook div.top { z-index:97; }
#macbook div.bottom { z-index:96; height:200px; }
#macbook:hover div.top { z-index:997; background-color:#bc003c; }
#macbook:hover div.bottom { z-index:996; background-color:#9d0032;
	background:-moz-linear-gradient(-90deg, #9d0032, #7a0027); background:-webkit-gradient(linear, 0 top, 0 bottom, from(#9d0032), to(#7a0027)); }

/* iPod bar */
#ipod div.top { z-index:95; }
#ipod div.bottom { z-index:94; height:250px; }
#ipod:hover div.top { z-index:995; background-color:#d98f23; }
#ipod:hover div.bottom { z-index:994; background-color:#b6781e;
	background:-moz-linear-gradient(-90deg, #b6781e, #916018); background:-webkit-gradient(linear, 0 top, 0 bottom, from(#b6781e), to(#916018)); }

/* Cinema Display bar */
#cinema div.top { z-index:93; }
#cinema div.bottom { z-index:92; height:100px; }
#cinema:hover div.top { z-index:993; background-color:#7da864; }
#cinema:hover div.bottom { z-index:992; background-color:#698d54;
	background:-moz-linear-gradient(-90deg, #698d54, #506b40); background:-webkit-gradient(linear, 0 top, 0 bottom, from(#698d54), to(#506b40)); }

/* Mac Mini bar */
#macmini div.top { z-index:91; }
#macmini div.bottom { z-index:90; height:120px; }
#macmini:hover div.top { z-index:991; background-color:#3f1150; }
#macmini:hover div.bottom { z-index:990; background-color:#340e43;
	background:-moz-linear-gradient(-90deg, #340e43, #1a0721); background:-webkit-gradient(linear, 0 top, 0 bottom, from(#340e43), to(#1a0721)); }

#apple { margin-top:-70px; position:relative; z-index:-999; }
#apple p { float:right; padding-top:247px; }

</style>
</head>
<body>
<div id="wrapper">
	<h1>Wicked CSS3 3d bar chart<small>using only CSS3</small></h1>
	<h2><a href="http://www.marcofolio.net/" title="Visit Marcofolio.net">Marcofolio.net</a></h2>
	<div id="content">
		<h2>Apple products</h2>
		<ul id="bar">
			<li id="iphone">
				<div class="top">
					<img src="images/iphone.png" alt="iPhone" />
				</div>
				<div class="bottom">
					<div class="infobox">
						<h3>iPhone</h3>
						<p>80,1</p>
					</div>
				</div>
			</li>
			<li id="macbook">
				<div class="top">
					<img src="images/macbook.png" alt="MacBook" />
				</div>
				<div class="bottom">
					<div class="infobox">
						<h3>MacBook</h3>
						<p>102,6</p>
					</div>
				</div>
			</li>
			<li id="ipod">
				<div class="top">
					<img src="images/ipod.png" alt="iPod" />
				</div>
				<div class="bottom">
					<div class="infobox">
						<h3>iPod</h3>
						<p>198,4</p>
					</div>
				</div>
			</li>
			<li id="cinema">
				<div class="top">
					<img src="images/cinema.png" alt="Cinema Display" />
				</div>
				<div class="bottom">
					<div class="infobox">
						<h3>Cinema&nbsp;Display</h3>
						<p>38,2</p>
					</div>
				</div>
			</li>
			<li id="macmini">
				<div class="top">
					<img src="images/macmini.png" alt="Mac Mini" />
				</div>
				<div class="bottom">
					<div class="infobox">
						<h3>Mac&nbsp;Mini</h3>
						<p>55,6</p>
					</div>
				</div>
			</li>
		</ul>
		<div id="apple">
			<img src="images/apple.png" alt="Apple Inc" />
			<p>Numbers in millions sold<br />*Numbers are fictional</p>
		</div>
	</div>
</div>
</body>
</html>







<!DOCTYPE html>
<html lang="en-US">
<body>

<h1>My Web Page</h1>

<div id="piechart"></div>

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Task', 'Hours per Day'],
  ['Work', 8],
  ['Eat', 2],
  ['TV', 4],
  ['Gym', 2],
  ['Sleep', 8]
]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'My Average Day', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}
</script>

</body>
</html>
"""

f.write(message)
f.close()