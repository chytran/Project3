<?php

if (isset($_POST["submit"])) {
    $name = filter_input(INPUT_POST, 'name');
    $lastName = filter_input(INPUT_POST, 'lastName');
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $password = filter_input(INPUT_POST, 'password');
    $repeatPassword = filter_input(INPUT_POST, 'passRepeat');

    if (!$name || !$email || !$password || !$repeatPassword) {
        header("location: ../signup.php?error=emptyinput");
        exit();
    }

    require_once "functions.inc.php";
    require_once "database.inc.php";

    if (noMatchPassword($password, $repeatPassword)) {
        header("location: ../signup.php?error=passwordnomatch");
        exit();
    }

    // Error Catching
    if (emptyInputSignup($name, $lastName, $email, $password, $repeatPassword)) {
        header("location: ../signup.php?error=emptyinput");
        exit();
    }

    if (invalidEmail($email) !== false) {
        header("location: ../signup.php?error=invalidEmail");
        exit();
    }

    if (invalidName($name) !== false) {
        header("location: ../signup.php?error=invalidName");
        exit();
    }

    if (invalidName($lastName) !== false) {
        header("location: ../signup.php?error=invalidName");
        exit();
    }

    // if username exist
    // if (uidExists($conn, $name, $email) !== false) {
    //     header("location: ../signup.php?error=usernametaken");
    //     exit();
    // }

    // Create user
    createUser($conn, $name, $lastName, $email, $password);
} 
else {
    header("location: ../login.php");
    exit();
}