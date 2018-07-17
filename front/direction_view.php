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
            <option value="
                <?php echo $station->id; ?>,,
                <?php echo $station->name; ?>,,
                <?php echo $station->line->id; ?>,,
                <?php echo $station->line->reseau->name; ?> <?php echo $station->line->code; ?>,,
                <?php echo $direction->sens; ?>
            ">
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