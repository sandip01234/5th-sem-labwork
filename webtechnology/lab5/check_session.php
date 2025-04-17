<?php
session_start();
if (isset($_SESSION["user"])) {
    echo "Session still exists. User: " . $_SESSION["user"];
} else {
    echo "Session not set.";
}
?>
