﻿<!DOCTYPE html>
<?php
    // Execute python script
    $num = rand(0,96);
    $year = rand(2016,2016);
    $month = rand(8,11);
    $date = rand(1,30);

    $file_name = "NeuralNetwork.py";
    $data = "FallData";
    $weigh = "nnWeights_Fall2016";
    if (file_exists($file_name))
    {
        //echo "File exists"."<br>";

        $command1 = escapeshellcmd("python $file_name $item");
        $output1 = shell_exec($command1);
        $command2 = escapeshellcmd("python $file_name procin $weigh $num $year $month $date");
        $output2 = shell_exec($command2);
        //echo $command2."<br>";
       //echo $output2."<br>";
    }
    else
    {
        echo "No file exits"."<br>";
    }
?>
<html ng-app lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <title>KnoWait -- NOW</title>
    <link href="bootstrap-3.3.7-dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="/bootstrap-btn/css/bootstrap.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.8/angular.min.js"></script>
    <script src="js/knowait.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="bootstrap-3.3.7-dist/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="css/knowait.css">
    <link rel="icon" href="img/knowait_icon.png">
    <style>
        #map {
            width: 100%;
            height: 400px;
            background-color: grey;
        }
    </style>
</head>
<body>
    <div id="overlay">
        <div id="progstat"></div>
        <div id="progress"></div>
    </div>

    <div id="container">
        <div id="main">
            <!--<div class="center-cropped">
            </div>-->
            <img src="img/index_background.png" class="backgroundImageView" alt="Image of Line At Chik-fil-A" />
            <img src="img/dark_filter.png" class="darkFilter" />

            <!--Navbar-->
            <nav class="navbar navbar-default">
                <div class="container-fluid">
                    <!-- Brand and toggle get grouped for better mobile display -->
                    <div class="navbar-header white-box">
                        <button type="button" class="navbar-toggle collapsed navbar-toggle-label" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar white-box"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href="#"><img src="img/knowait_logo_1250x1250.png" class="menu-logo white-box" /></a>
                    </div>
                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                        <ul class="nav navbar-nav navbar-right ul-menu">
                            <li class="li-menu"><a href="#">NAVIGATION</a></li>
                            <li class="li-menu"><a href="#">OPENINGS</a></li>
                            <li class="li-menu"><a href="#">WAITIMES</a></li>
                            <li class="li-menu"><a href="#">DAYLIGHT</a></li>
                            <li class="li-menu about-padding white-box"><a href="#">ABOUT</a></li>
                        </ul>
                    </div><!-- /.navbar-collapse -->
                </div><!-- /.container-fluid -->
            </nav>
                <div class="col-md-9" id="white-box">
                    <h3>NAVIGATION</h3>
                    <div id="map"></div>
<script>
      function initMap() {
        var uluru = {lat: -25.363, lng: 131.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
      }

                    </script>
            
                </div>
            <div class="col-md-3" id="white-box">
                <div>
                    <label>Name:</label>
                    <input type="text" ng-model="yourName" placeholder="Enter a name here">
                    <hr>
                    
                </div>
            </div>

</div>
                <div class="col-md-12" id="white-box">
                    <h1><?php echo round($output2/60,2); ?> min. wait at {{yourName}}.</h1>
                    
                </div>
            

        </div>

    </div>
    <script
src ="https://maps.googleapis.com/maps/api/js?key=AIzaSyDfU_WzZr8o1pWJ75-fxMuKAiGUtd5KdBk&callback=initMap"
    async defer></script>
</body>
</html>