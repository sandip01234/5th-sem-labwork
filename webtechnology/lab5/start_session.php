<?php
session_start();
$_SESSION["user"] = "JohnDoe";
echo "Session started. User is: " . $_SESSION["user"];
?>
