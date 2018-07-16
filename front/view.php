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
        <h3>
            <?php echo htmlspecialchars($station['name']); ?>
        </h3>
<?php
}
?>
</body>
</html>