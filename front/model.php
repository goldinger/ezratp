<?php

function getStationsByName($stationName)
{
    $response = file_get_contents("https://ezratp.sghir.me/api/stations?stationName=" . $stationName);
    $response = json_decode($response);
    return $response;
}

function getNextMissions($lineId, $stationId, $sens)
{
    $response = file_get_contents("https://ezratp.sghir.me/api/arduino/nextMissions?lineId=' . $lineId . '&stationId=" . $stationId . '&sens=' . $sens);
    $response = json_decode($response);
    return $response;
}