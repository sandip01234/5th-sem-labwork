<?php
function sum() {
    $args = func_get_args();
    $total = 0;

    foreach ($args as $arg) {
        $total += $arg;
    }

    return $total;
}

echo "Sum of 2 numbers: " . sum(5, 10) . "<br>";
echo "Sum of 3 numbers: " . sum(5, 10, 15) . "<br>";
?>
