<?php
    session_start();
    session_destroy();
    // if(isset($_SESSION['user'])) {
    //     session_destroy();
    //     echo  "<script>location.href='../login.php'</script>";
    //     // header("location: ../index.php");
    // }
    // else {

    //     echo "There was an error to the logout";
    // }
?>