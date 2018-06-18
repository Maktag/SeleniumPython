from trial.Status import status


def Prepare_report():
    html_file = open('File_Name1.html','w')
    web_page_part_1 = """
        <!DOCTYPE html>
        <html>
        <title>Test Report</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="mt.css" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
        body,h1,h2,h3,h4,h5,h6 {font-family: "Raleway", sans-serif}
        </style>
        <body class="mt-light-grey mt-content" style="max-width:1600px">
    """
    web_page_part_2 = """
        <!-- Sidebar/menu -->
        <nav class="mt-sidebar mt-collapse mt-white mt-animate-left" style="z-index:3;width:300px;" id="mySidebar"><br>
          <div class="mt-container">
            <a href="#" onclick="mt_close()" class="mt-hide-large mt-right mt-jumbo mt-padding mt-hover-grey" title="close menu">
              <i class="fa fa-remove"></i>
            </a>
            <img src="http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg" style="width:45%;" class="mt-round"><br><br>
            <h4><b>Testing Modules</b></h4>
          </div>
          <div class="mt-bar-block">
            <a href="#portfolio" onclick="mt_close()" class="mt-bar-item mt-button mt-padding mt-text-teal"><i class="fa fa-th-large fa-fw mt-margin-right"></i>Pie Chart</a> 
            <a href="#TestExecutionDetails" onclick="mt_close()" class="mt-bar-item mt-button mt-padding"><i class="fa fa-user fa-fw mt-margin-right"></i>Test Execution Details</a> 
            <a href="#contact" onclick="mt_close()" class="mt-bar-item mt-button mt-padding"><i class="fa fa-envelope fa-fw mt-margin-right"></i>CONTACT</a>
          </div>
        </nav>
        <!-- Overlay effect when opening sidebar on small screens -->
        <div class="mt-overlay mt-hide-large mt-animate-opacity" onclick="mt_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>
    """
    web_page_part_3 = """
        <!-- !PAGE CONTENT! -->
        <div class="mt-main" style="margin-left:300px">
    """
    web_page_part_4 = """
        <!-- Header -->
          <header id="portfolio">
            <a href="#"><img src="/mtimages/avatar_g2.jpg" style="width:65px;" class="mt-circle mt-right mt-margin mt-hide-large mt-hover-opacity"></a>
            <span class="mt-button mt-hide-large mt-xxlarge mt-hover-text-grey" onclick="mt_open()"><i class="fa fa-bars"></i></span>
            <div class="mt-container">
            <h1><b>Details</b></h1>
        
                <div id="piechart" style="width:100%"></div>
                <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        
                <script type="text/javascript">
                // Load google charts
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(drawChart);
        
                // Draw the chart and set the chart values
                function drawChart() {
                  var data = google.visualization.arrayToDataTable([
                  ['Task', 'Hours per Day'],
                  ['Pass', 8],
                  ['Fail', 2],
                  ['Error', 4],
                  ['Skip', 2],
                  ['Info', 8]
                ]);
        
                  // Optional; add a title and set the width and height of the chart
                  var options = {'title':'Test Result', 'width':1150, 'height':500};
        
                  // Display the chart inside the <div> element with id="piechart"
                  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
                  chart.draw(data, options);
                }
                </script>
            <!--
            <div class="mt-section mt-bottombar mt-padding-16">
              <span class="mt-margin-right">Filter:</span> 
              <button class="mt-button mt-black">ALL</button>
              <button class="mt-button mt-white"><i class="fa fa-diamond mt-margin-right"></i>Design</button>
              <button class="mt-button mt-white mt-hide-small"><i class="fa fa-photo mt-margin-right"></i>Photos</button>
              <button class="mt-button mt-white mt-hide-small"><i class="fa fa-map-pin mt-margin-right"></i>Art</button>
            </div>
            </div> -->
        </header>
    """

    #This will show the module name and
    web_page_part_5_A = """
    <div class="mt-row-padding mt-padding-16" id="TestExecutionDetails">
    """

    web_page_part_5_B = """
                <div  id="module" class="mt-col m12">
                  <h1>Login With FaceBook</h1>
                </div>
    """

    web_page_part_5_C = """
            <div id="TestCase" class="mt-col m12">
              <p style="color:#3366cc; border-left: 6px solid #3366cc!important; border-bottom: 1px solid; padding: 0.90em 16px;">
                <b>1.</b> 
                  Login is not working.
                  <img src="http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg" style="width:10%; float:right;" class="mt-round">
              </p>     
            </div>
    """

    web_page_part_5_D = """</div>"""

    web_page_part_6 = """
         <!-- Footer -->
          <footer class="mt-container mt-padding-32 mt-dark-grey">
          </div>
          </footer>
         <!-- End page content -->
        </div>
    """

    web_page_part_7 = """
        <script>
            // Script to open and close sidebar
            function mt_open() {
                document.getElementById("mySidebar").style.display = "block";
                document.getElementById("myOverlay").style.display = "block";
            }
            
            function mt_close() {
                document.getElementById("mySidebar").style.display = "none";
                document.getElementById("myOverlay").style.display = "none";
            }
        </script>
        </body>
        </html>
    """
    html_file.write(web_page_part_1)
    html_file.write(web_page_part_2)
    html_file.write(web_page_part_3)
    html_file.write(web_page_part_4)
    html_file.write(web_page_part_5_A)
    html_file.write(web_page_part_5_B)
    html_file.write(web_page_part_5_C)
    html_file.write(web_page_part_5_D)
    html_file.write(web_page_part_6)
    html_file.write(web_page_part_7)
    html_file.close()

Prepare_report()

# f = open('helloworld.html', 'w')

# message = """

# <!DOCTYPE html>
# <html>
# <title>Test Report</title>
# <meta charset="UTF-8">
# <meta name="viewport" content="width=device-width, initial-scale=1">
# <link rel="stylesheet" type="text/css" href="mt.css" />
# <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
# <style>
# body,h1,h2,h3,h4,h5,h6 {font-family: "Raleway", sans-serif}
# </style>
# <body class="mt-light-grey mt-content" style="max-width:1600px">

# <!-- Sidebar/menu -->
# <nav class="mt-sidebar mt-collapse mt-white mt-animate-left" style="z-index:3;width:300px;" id="mySidebar"><br>
#   <div class="mt-container">
#     <a href="#" onclick="mt_close()" class="mt-hide-large mt-right mt-jumbo mt-padding mt-hover-grey" title="close menu">
#       <i class="fa fa-remove"></i>
#     </a>
#     <img src="http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg" style="width:45%;" class="mt-round"><br><br>
#     <h4><b>Testing Modules</b></h4>
#   </div>
#   <div class="mt-bar-block">
#     <a href="#portfolio" onclick="mt_close()" class="mt-bar-item mt-button mt-padding mt-text-teal"><i class="fa fa-th-large fa-fw mt-margin-right"></i>Pie Chart</a> 
#     <a href="#TestExecutionDetails" onclick="mt_close()" class="mt-bar-item mt-button mt-padding"><i class="fa fa-user fa-fw mt-margin-right"></i>Test Execution Details</a> 
#     <a href="#contact" onclick="mt_close()" class="mt-bar-item mt-button mt-padding"><i class="fa fa-envelope fa-fw mt-margin-right"></i>CONTACT</a>
#   </div>
# 
# </nav>
# 
# <!-- Overlay effect when opening sidebar on small screens -->
# <div class="mt-overlay mt-hide-large mt-animate-opacity" onclick="mt_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

# <!-- !PAGE CONTENT! -->
# <div class="mt-main" style="margin-left:300px">

  # <!-- Header -->
  # <header id="portfolio">
  #   <a href="#"><img src="/mtimages/avatar_g2.jpg" style="width:65px;" class="mt-circle mt-right mt-margin mt-hide-large mt-hover-opacity"></a>
  #   <span class="mt-button mt-hide-large mt-xxlarge mt-hover-text-grey" onclick="mt_open()"><i class="fa fa-bars"></i></span>
  #   <div class="mt-container">
  #   <h1><b>Details</b></h1>
  # 
  #       <div id="piechart" style="width:100%"></div>
  #       <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  # 
  #       <script type="text/javascript">
  #       // Load google charts
  #       google.charts.load('current', {'packages':['corechart']});
  #       google.charts.setOnLoadCallback(drawChart);
  # 
  #       // Draw the chart and set the chart values
  #       function drawChart() {
  #         var data = google.visualization.arrayToDataTable([
  #         ['Task', 'Hours per Day'],
  #         ['Pass', 8],
  #         ['Fail', 2],
  #         ['Error', 4],
  #         ['Skip', 2],
  #         ['Info', 8]
  #       ]);
  # 
  #         // Optional; add a title and set the width and height of the chart
  #         var options = {'title':'Test Result', 'width':1150, 'height':500};
  # 
  #         // Display the chart inside the <div> element with id="piechart"
  #         var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  #         chart.draw(data, options);
  #       }
  #       </script>
  #   <!--
  #   <div class="mt-section mt-bottombar mt-padding-16">
  #     <span class="mt-margin-right">Filter:</span> 
  #     <button class="mt-button mt-black">ALL</button>
  #     <button class="mt-button mt-white"><i class="fa fa-diamond mt-margin-right"></i>Design</button>
  #     <button class="mt-button mt-white mt-hide-small"><i class="fa fa-photo mt-margin-right"></i>Photos</button>
  #     <button class="mt-button mt-white mt-hide-small"><i class="fa fa-map-pin mt-margin-right"></i>Art</button>
  #   </div>
  #   </div> -->
  # </header>

  # <!-- Images of Me -->
  # <div class="mt-row-padding mt-padding-16" id="TestExecutionDetails">
  #   <div  id="module" class="mt-col m12">
  #     <h1>Login With FaceBook</h1>
  #   </div>
  # 
  #   <div id="TestCase" class="mt-col m12">
  #     <p style="color:#3366cc; border-left: 6px solid #3366cc!important; border-bottom: 1px solid; padding: 0.90em 16px;">
  #       <b>1.</b> 
  #         Login is not working.
  #         <img src="http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg" style="width:10%; float:right;" class="mt-round">
  #     </p>     
  #   </div>
  # </div>

# <!--
#   <div class="mt-container mt-padding-large" style="margin-bottom:32px">
#     <h4><b>About Me</b></h4>
#     <p>Just me, myself and I, exploring the universe of unknownment. I have a heart of love and an interest of lorem ipsum and mauris neque quam blog. I want to share my world with you. Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla. Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.</p>
#     <hr>
#     -->
#
#   <!-- First Photo Grid-->
# <!--
#   <div class="mt-row-padding">
#     <div class="mt-third mt-container mt-margin-bottom">
#       <img src="/mtimages/mountains.jpg" alt="Norway" style="width:100%" class="mt-hover-opacity">
#       <div class="mt-container mt-white">
#         <p><b>Lorem Ipsum</b></p>
#         <p>Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.</p>
#       </div>
#     </div>
#   </div>
#
#   </div>
#   -->


#   <!-- Footer -->
#   <footer class="mt-container mt-padding-32 mt-dark-grey">
# 
# 
#   </div>
#   </footer>
# 
# 
# 
# <!-- End page content -->
# </div>

# <script>
# // Script to open and close sidebar
# function mt_open() {
#     document.getElementById("mySidebar").style.display = "block";
#     document.getElementById("myOverlay").style.display = "block";
# }
# 
# function mt_close() {
#     document.getElementById("mySidebar").style.display = "none";
#     document.getElementById("myOverlay").style.display = "none";
# }
# </script>
# 
# </body>
# </html>
# """