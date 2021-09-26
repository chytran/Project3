<?php

$servername = "localhost:8111";
// $servername = "localhost:8111"; // Replace '8111' with your Ports ID

$dBUsername = "root";
$dBPassword = "";
$dBName = "home";

$conn = mysqli_connect($servername, $dBUsername, $dBPassword, $dBName);

if (!$conn) {
    die("Connection failed: " . mysqli_connection_error());
} else {
    // echo "Connection successful";
}