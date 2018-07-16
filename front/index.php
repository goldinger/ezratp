<?php
require('model.php');

$stations = getStationsByName('Alesia');
//$minutes = getNextMissions('77','1913-2238', 'A');

require('view.php');