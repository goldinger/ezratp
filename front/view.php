<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>ezratp</title>
</head>
<body>
<h1>Easy Ratp</h1>
<p>Stations d'alesia</p>

<?php
foreach ($stations as $station)
{
?>
        <div>
            <p><?php echo $station->id; ?></p>
            <p><?php echo $station->name; ?></p>
            <p><?php echo $station->line->reseau->name; ?> <?php echo $station->line->code; ?></p>
            <br />
        </div>
<?php
}
?>
</body>
</html>