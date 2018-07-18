<?php
require('model.php');

$data = explode(",,", $_GET["data"]);
$stationId = $data[0];
$stationName = $data[1];
$lineId = $data[2];
$lineName = $data[3];
$sens = $data[4];
$missions = getNextMissions($lineId, $stationName, $sens);

require('missions_view.php');