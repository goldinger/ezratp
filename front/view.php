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
foreach ($minutes as $minute)
{
?>
        <h3>
            <?php echo $minute; ?>
        </h3>
<?php
}
?>
</body>
</html>