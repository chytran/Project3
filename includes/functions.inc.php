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
function emptyInputSignup($name, $email, $lastName, $password, $repeatPassword) {
    $result;
    if (!$name || !$lastName || !$email || !$password || !$repeatPassword) {
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

    if  (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../signup.php?error=stmtfailed");
        exit();
    }

    mysqli_stmt_bind_param($stmt, "ss", $username, $email);
    mysqli_stmt_execute($stmt);

    $resultData = mysqli_stmt_get_result($stmt);

    if ($row = mysqli_fetch_assoc($resultData)) {
        return $row;
    }
    else {
        $result = false;
        return $result;
    }

    mysqli_stmt_close($stmt);
}

function createUser($conn, $name, $lastName, $email, $pwd, $userType) {
    $sql = "INSERT INTO user (userName, userLastName, userEmail, userPassword, userType) VALUES (?, ?, ?, ?, ?);";
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../signup.php?error=stmtfailed");
        exit();
    }

    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);

    mysqli_stmt_bind_param($stmt, "sssss", $name, $lastName,  $email, $hashedPwd, $userType);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    header("location: ../login.php?error=none");
    exit();
}

function emptyInputLogin($email, $password) {
    $result;
    if (empty($email) || empty($password)) {
        $result = true;
    }
    else {
        $result = false;
    }
    return $result;
}


function loginUser($conn, $username, $password) {
    $uidExists = uidExists($conn, $username, $username);

    if ($uidExists === false) {
        header("location: ../login.php?error=wronglogin");
        exit();
    }

    $pwdHashed = $uidExists["userPassword"];
    $checkPwd = password_verify($password, $pwdHashed);

    if($checkPwd === false) {
        header("location: ../login.php?error=wrongpassword");
        exit();
    }

    else if ($checkPwd === true) {
        session_start();
        $_SESSION["userid"] = $uidExists["id"];
        $_SESSION["userEmail"] = $uidExists["userEmail"];
        header("location: ../index.php");
        exit();
    }
}
