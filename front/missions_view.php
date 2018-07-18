<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>EZ RATP</title>
</head>
<body>
<h1>Easy Ratp</h1>
<h2>Station : <?php echo $stationName; ?></h2>
<h2>Line : <?php echo $lineName ?></h2>
        <?php
        foreach ($missions as $mission)
        {
            ?>
            <p><?php echo $mission ?></p>
            <?php
        }
        ?>
</body>
</html>