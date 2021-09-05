<?php

if (isset($_POST["submit"])) {
    $name = filter_input(INPUT_POST, 'name');
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $password = filter_input(INPUT_POST, 'password');
    $repeatPassword = filter_input(INPUT_POST, 'passRepeat');

    if (!$name || !$email || !$password || $repeatPassword) {
        header("location: ../signup.php?error=emptyinput");
        exit();
    }

    require_once "functions.inc.php";
    require_once "database.inc.php";

    // if (noMatchPassword($password, $repeatPassword)) {
    //     header("location: ../signup.php?error=passwordnomatch");
    //     exit();
    // }

    createUser($conn, $name, $email, $password);

?>