<?php

function getStationsByName($stationName)
{
    $response = file_get_contents("https://ezratp.sghir.me/api/stations?stationName=" . $stationName);
    $response = json_decode($response);
    return $response;
}

function getNextMissions($lineId, $stationId, $sens)
{
    $response = file_get_contents("https://ezratp.sghir.me/api/nextMissions?lineId=' . $lineId . '&stationId=" . $stationId . '&sens=' . $sens);
    echo $response;
    $response = json_decode($response);
    return $response;
}