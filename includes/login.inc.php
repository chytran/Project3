<?php

if (isset($_POST["submit"])) {
    $email = filter_input(INPUT_POST, 'email');
    $password = filter_input(INPUT_POST, 'password');

    require_once 'database.inc.php';
    require_once 'functions.inc.php';

    if (emptyInputLogin($email, $password) !== false) {
        header("location: ../login.php?error=emptyinput");
        exit();
    }

    loginUser($conn, $email, $password);
} 
else {
    header("location: ../login.php");
    exit();
}