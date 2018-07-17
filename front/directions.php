<?php
require('model.php');

$data = explode(",,", $_GET["stationData"]);
$stationId = $data[0];
$stationName = $data[1];
$lineId = $data[2];
$lineName = $data[3];
$directions = getDirections($lineId)->directions;

require('direction_view.php');