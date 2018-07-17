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
<form action="missions.php">
    <select name="data" size="10">
        <?php
        foreach ($directions as $direction)
        {
            ?>
            <option value="<?php echo $stationId; ?>,,<?php echo $stationName; ?>,,<?php echo $lineId; ?>,,<?php echo $lineName; ?>,,<?php echo $direction->sens; ?>">
                <?php echo $direction->name; ?>
            </option>
            <?php
        }
        ?>
    </select>
    <br><br>
    <input type="submit">
</form>
</body>
</html>