<?php

function getStationsByName($stationName)
{
    $response = file_get_contents("https://ezratp.sghir.me/api/stations?stationName=" . $stationName);
    $response = json_decode($response);
    return $response;
}