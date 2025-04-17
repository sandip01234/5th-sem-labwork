<?php
$filename = "file.txt";

// a. Create the file and b. Write name and roll number
file_put_contents($filename, "Name: John Doe\nRoll No: 12345");

// c. Read the file
$contents = file_get_contents($filename);

// d. Add current date
$contents .= "\nDate: " . date("Y-m-d H:i:s");
file_put_contents($filename, $contents);

// e. (Already handled by file_put_contents)

// f. Rename the file
rename("file.txt", "test.txt");

echo "File operations completed.";
?>
