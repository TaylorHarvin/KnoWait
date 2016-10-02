<?php 

$myArray = array(5,6,7,8,9);

$command = escapeshellcmd('python3 NeuralNetwork.py '.implode(",",$myArray));
$output = shell_exec($command);
echo $output;
print_r( error_get_last());
?>