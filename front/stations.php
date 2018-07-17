<?php
require('model.php');

$data = $_GET["data"];
$stationName = $data;
$stations = getStationsByName($stationName);

require('station_view.php');