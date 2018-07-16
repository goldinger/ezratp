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
        <p><?php echo $station->id; ?> - <?php echo $station->name; ?>
            <br><?php echo $station->line->id?> - <?php echo $station->line->reseau->name; ?> <?php echo $station->line->code; ?>
        </p>
<?php
}
?>
</body>
</html>