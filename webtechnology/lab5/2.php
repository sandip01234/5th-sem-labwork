<?php
$numbers = [1, 2, 3, 4, 5];
$squares = [];

foreach ($numbers as $number) {
    $squares[] = $number * $number;
}

print_r($squares);
?>
