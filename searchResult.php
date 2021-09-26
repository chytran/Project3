<?php
    include_once 'components/header.php';
?>

<?php 
    include_once 'includes/database.inc.php';
?>

<header class="header" id="header">
    <nav class="nav container">
        <a href="#" class="nav__logo">Home</a>

        <div class="nav__menu" id="nav-menu">
            <ul class="nav__list">
                <li class="nav__item">
                    <a href="#home" class="nav__link">Home</a>
                </li>
                <li class="nav__item">
                    <a href="#about" class="nav__link">About</a>
                </li>
                <li class="nav__item">
                    <a href="#discover" class="nav__link">Discover</a>
                </li>
                <li class="nav__item">
                    <a href="login.php" class="nav__link">Login</a>
                </li>
            </ul>

            <i class="ri-close-line nav__close" id="nav-close"></i>
        </div>

        <div style="cursor: pointer;" class="nav__toggle" id="nav-toggle">
            <i class="ri-function-line"></i>
        </div>
    </nav>
</header>

<!--================ BODY =======================-->
<section class="search__result hero__house" style="background-color: black;">
    <img src="image/resultpage.jpg" alt="" class="search__img">

    <form action="includes/houseDetail.inc.php" method="post" class="search__form">
        <input type="text" name="search" class="search__result">
        <input type="submit" class="button" name="submit">
    </form>

    <div class="map__container" style="height: 400px; width: 100%;">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3172.370930560317!2d-121.89211318474916!3d37.3337261798421!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fccbb4e751f57%3A0x7bb970c4219e6acd!2sSan%20Jos%C3%A9%20Museum%20of%20Art!5e0!3m2!1sen!2sus!4v1632683176648!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
    </div>

</section>

<section class="house__show hero__house" id="house-show">
    <?php
        $sql = "SELECT * FROM houses;";
        $result = mysqli_query($conn, $sql);
        $resultCheck = mysqli_num_rows($result);

        if ($resultCheck > 0) {
            while ($row = mysqli_fetch_assoc($result)) {
                echo "<div class='house__info'>";
                     echo "<p class='house__address'>" . $row['address'] . "</p>";
                     echo "<p class='house__sqft'>" . $row['sqft'] . "</p>";
                     echo "<p class='house__price'>" . $row['price'] . "</p>";
                echo "</div>";

                
            }
        }

    ?>
</section>


<script src="js/search.js"></script>

<?php
    include_once 'components/footer.php';
?>