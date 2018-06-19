

def Prepare_report(test_report, test_modules, page_name):

    # html_file = open(page_name.replace(' ', '')+'.html','w')
    html_file = open('index.html', 'w')
    web_page_part_1 = "<!DOCTYPE html><html><title>Test Report</title><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1'>        " \
                      "<link rel='stylesheet' type='text/css' href='mt.css' /><link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Raleway'>        " \
                      "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>        " \
                      "<style>        " \
                      "body,h1,h2,h3,h4,h5,h6 {font-family: 'Raleway', sans-serif}        " \
                      "</style>        " \
                      "<body class='mt-light-grey mt-content' style='max-width:1600px'>"
    web_page_part_2 = "<!-- Sidebar/menu --><nav class='mt-sidebar mt-collapse mt-white mt-animate-left' style='z-index:3;width:300px;' id='mySidebar'><br>" \
                      "<div class='mt-container'><a href='#' onclick='mt_close()' class='mt-hide-large mt-right mt-jumbo mt-padding mt-hover-grey' title='close menu'>" \
                      "<i class='fa fa-remove'></i></a><img src='http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg' style='width:45%;' class='mt-round'><br><br>" \
                      "<h4><b>Testing Modules</b></h4></div><div class='mt-bar-block'><a href='#portfolio' onclick='mt_close()' class='mt-bar-item mt-button mt-padding mt-text-teal'>" \
                      "<i class='fa fa-th-large fa-fw mt-margin-right'></i>Pie Chart</a>" \
                      "<a href='#TestExecutionDetails' onclick='mt_close()' class='mt-bar-item mt-button mt-padding'><i class='fa fa-user fa-fw mt-margin-right'></i>Test Execution Details</a>" \
                      "<a href='#contact' onclick='mt_close()' class='mt-bar-item mt-button mt-padding'><i class='fa fa-envelope fa-fw mt-margin-right'></i>CONTACT</a></div>" \
                      "</nav><!-- Overlay effect when opening sidebar on small screens -->" \
                      "<div class='mt-overlay mt-hide-large mt-animate-opacity' onclick='mt_close()' style='cursor:pointer' title='close side menu' id='myOverlay'></div>"
    web_page_part_3 = "<!-- !PAGE CONTENT! --> <div class='mt-main' style='margin-left:300px'>"
    web_page_part_4 = "<!-- Header --><header id=\"portfolio\">" \
                      "<a href=\"#\"><img src=\"/mtimages/avatar_g2.jpg\" style=\"width:65px;\" class=\"mt-circle mt-right mt-margin mt-hide-large mt-hover-opacity\"></a>" \
                      "<span class='mt-button mt-hide-large mt-xxlarge mt-hover-text-grey' onclick='mt_open()'><i class='fa fa-bars'></i></span>" \
                      "<div class='mt-container'><h1><b>Details</b></h1>" \
                      "<div id=\"piechart\" style=\"width:100%\"></div>" \
                      "<script type='text/javascript' src='https://www.gstatic.com/charts/loader.js'></script>" \
                      "                              <script type='text/javascript'>" \
                      "                                google.charts.load('current', {'packages':['corechart']});" \
                      "                                google.charts.setOnLoadCallback(drawChart);" \
                      "                                function drawChart() {" \
                      "                                  var data = google.visualization.arrayToDataTable([" \
                      "                                  ['Task', 'Hours per Day']," \
                      "                                  ['Pass', 8]," \
                      "                                  ['Fail', 2]," \
                      "                                  ['Error', 4]," \
                      "                                  ['Skip', 2]," \
                      "                                  ['Info', 8]" \
                      "                                ]);" \
                      "                                  var options = {'title':'Test Result', 'width':1150, 'height':500};" \
                      "                                 var chart = new google.visualization.PieChart(document.getElementById('piechart'));" \
                      "                                 chart.draw(data, options);" \
                      "                               }" \
                      "                               </script>" \
                      "                           <!--" \
                      "                            <div class='mt-section mt-bottombar mt-padding-16'>" \
                      "                              <span class='mt-margin-right'>Filter:</span>" \
                      "                              <button class='mt-button mt-black'>ALL</button>" \
                      "                              <button class='mt-button mt-white'><i class='fa fa-diamond mt-margin-right'></i>Design</button>" \
                      "                              <button class='mt-button mt-white mt-hide-small'><i class='fa fa-photo mt-margin-right'></i>Photos</button>" \
                      "                              <button class='mt-button mt-white mt-hide-small'><i class='fa fa-map-pin mt-margin-right'></i>Art</button>" \
                      "                            </div>" \
                      "                            </div> -->" \
                      "                        </header>"

    web_page_part_6 = "<!-- Footer -->" \
                      "          <footer class='mt-container mt-padding-32 mt-dark-grey'>" \
                      "          </div>" \
                      "          </footer>" \
                      "         <!-- End page content -->" \
                      "        </div>    "

    web_page_part_7 = "<script>         " \
                      "// Script to open and close sidebar            " \
                      "function mt_open() {                " \
                      "document.getElementById('mySidebar').style.display = 'block';                " \
                      "document.getElementById('myOverlay').style.display = 'block';            }" \
                      "function mt_close() {" \
                      "document.getElementById('mySidebar').style.display = 'none';" \
                      "document.getElementById('myOverlay').style.display = 'none';" \
                      "}" \
                      "</script>" \
                      "</body>" \
                      "</html>"


    html_file.write(web_page_part_1)
    html_file.write(web_page_part_2)
    html_file.write(web_page_part_3)
    html_file.write(web_page_part_4)

    for module in test_modules:
        html_file.write("<div class='mt-row-padding mt-padding-16' id='TestExecutionDetails'>")
        html_file.write("<div  id='module' class='mt-col m12'><h1>")
        html_file.write(module)
        html_file.write("</h1></div><div id='TestCase' class='mt-col m12'>")

        for test_id in test_report['All_Cases'].keys():
            commment_with_status = test_report['All_Cases'][test_id]
            comment = commment_with_status[:-1]
            status = commment_with_status.replace(commment_with_status[:-1], '')
            if status == 'P':
                html_file.write("<p style='color:#3366cc; border-left: 6px solid #3366cc!important; "
                            "border-bottom: 1px solid; padding: 0.90em 16px;'><b>" +test_id+". </b>" +comment+""
                            "<img src = 'http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg' style = 'width:10%; float:right;' class ='mt-round' >")
            elif status == 'F':
                html_file.write("<p style='color:#dc3912; border-left: 6px solid #dc3912!important; "
                            "border-bottom: 1px solid; padding: 0.90em 16px;'><b>" +test_id+". </b>" +comment+""
                            "<img src = 'http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg' style = 'width:10%; float:right;' class ='mt-round' >")
            elif status == 'E':
                html_file.write("<p style='color:#ff9900; border-left: 6px solid #ff9900!important; "
                            "border-bottom: 1px solid; padding: 0.90em 16px;'><b>" +test_id+". </b>" +comment+""
                            "<img src = 'http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg' style = 'width:10%; float:right;' class ='mt-round' >")
            elif status == 'S':
                html_file.write("<p style='color:#109618; border-left: 6px solid #109618!important; "
                            "border-bottom: 1px solid; padding: 0.90em 16px;'><b>" +test_id+". </b>" +comment+""
                            "<img src = 'http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg' style = 'width:10%; float:right;' class ='mt-round' >")
            elif status == 'I':
                html_file.write("<p style='color:#990099; border-left: 6px solid #990099!important; "
                            "border-bottom: 1px solid; padding: 0.90em 16px;'><b>" +test_id+". </b>" +comment+""
                            "<img src = 'http://www.medocity.com/wp-content/uploads/2017/05/Medocity-Logo.-Full_website.jpg' style = 'width:10%; float:right;' class ='mt-round' >")

        html_file.write("</div></div>")


    html_file.write(web_page_part_6)
    html_file.write(web_page_part_7)
    html_file.close()
