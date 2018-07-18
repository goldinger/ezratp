<?php
require('model.php');

$data = $_GET["data"];
$stationName = $data;
$stations = getStationsByName(str_replace('+', ' ', $stationName));

require('station_view.php');