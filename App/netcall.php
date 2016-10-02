<?php
// Execute python script
$num = rand(0,96);
$year = rand(2016,2016);
$month = rand(8,11);
$date = rand(1,30);

$file_name = "NeuralNetwork.py";
$data = "FallData";
$weigh = "nnWeights_Fall2016";
if (file_exists($file_name))
{
    //echo "File exists"."<br>";

    $command1 = escapeshellcmd("python $file_name $item");
    $output1 = shell_exec($command1);
    $command2 = escapeshellcmd("python $file_name procin $weigh $num $year $month $date");
    $output2 = shell_exec($command2);
    //echo $command2."<br>";
    echo $output2."<br>";
}
else
{
    echo "No file exits"."<br>";
}
?>