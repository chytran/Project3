<?php
    include_once 'components/header.php';
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
<section class="search__result hero" style="background-color: black;">
    <img src="image/result.jpg" alt="" class="search__img">

    <form action="includes/houseDetail.inc.php" method="post" class="search__form">
        <input type="text" name="search" class="search__result">
        <input type="submit" class="button" name="submit">
    </form>
</section>

<script src="js/search.js"></script>

<?php
    include_once 'components/footer.php';
?>