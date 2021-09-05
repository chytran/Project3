<?php

function noMatchPassword($password, $repeatPassword) {
    $result;
    // if true, call the error 
    if ($password !== $repeatPassword) {
        $result = true;
    }
    // if false, it passes the test
    else {
        $result = false;
    }
    return $result;
}

// If any of the input is empty
function emptyInputSignup($name, $email, $password, $repeatPassword) {
    $result;
    if (!$name || !$email || !$password || !$repeatPassword) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
}

// If the email is invalid
function invalidEmail($email) {
    $result;
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)){
        // it will send an error if true
        $result = true;
    } else {
        // it will not send a error if false
        $result = false;
    }
    return $result;
}

// If the name is invalid
function invalidName($name) {
    $result;
    if (!preg_match("/^[a-zA-Z0-9]*$/", $name)){
        // it will send an error if true
        $result = true;
    } else {
        // it will not send a error if false
        $result = false;
    }
    return $result;
}

// If the name or email exist
function uidExists($conn, $username, $email) {
    $sql = "SELECT * FROM user WHERE userName = ? OR userEmail = ?;";
    $stmt = mysqli_stmt_init($conn);
}

function createUser($conn, $name, $email, $pwd) {
    $sql = "INSERT INTO user (userName, userEmail, userPassword) VALUES (?, ?, ?);";
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../signup.php?error=stmtfailed");
        exit();
    }

    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);

    mysqli_stmt_bind_param($stmt, "sss", $name, $email, $hashedPwd);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    header("location: ../login.php?error=none");
    exit();
}
