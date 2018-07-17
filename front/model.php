<?php

$base_url = "https://ezratp.sghir.me/api/";

function getStationsByName($stationName)
{
    global $base_url;
    $response = file_get_contents($base_url . "stations?stationName=" . $stationName);
    $response = json_decode($response);
    return $response;
}

function getNextMissions($lineId, $stationId, $sens)
{
    global $base_url;
    $response = file_get_contents($base_url . "arduino/nextMissions?lineId=" . $lineId . "&stationId=" . $stationId . "&sens=" . $sens);
    $response = json_decode($response);
    return $response;
}

function getDirections($lineId)
{
    global $base_url;
    $response = file_get_contents($base_url . "directions/" . $lineId);
    $response = json_decode($response);
    return $response;
}