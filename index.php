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

<!--============= MAIN =============-->
<main class="main">
    <!--============= HOME =============-->
    <section class="home" id="home">
        <img src="image/search-background.jpg" alt="" class="home__img">

        <div class="home__container container grid">
            <div class="home__data">
                <span class="home__data-subtitle">Discover your place</span>
                <h1 class="home__data-title">Explore The <br> Best <br> Beautiful <br> Houses</h1>
                <a href="#" class="button">Explore</a>
            </div>

            <div class="smoke" id="smoke">
                <ul class="smoke1">
                    <ul>
                        <li>z</li>
                        <li>z</li>
                        <li>z</li>
                        
                    </ul>
                    <ul>
                        <li>z</li>
                        <li>z</li>
                        <li>z</li>
                        <li>z</li>
                        <li>z</li>

                    </ul>
                    <ul>
                        <li>z</li>
                        <li>z</li>
                        <li>z</li>
                        <li>z</li>

                    </ul>
                    <ul>
                        <li>z</li>
                        <li>z</li>
                        <li>z</li>
                    </ul>
                </ul>
            </div>

            <div class="home__social">
                <a href="https://facebook.com/" target="_blank" class="home__social-link">
                    <i class="ri-facebook-box-fill"></i>
                </a>
                <a href="https://instagram.com/" target="_blank" class="home__social-link">
                    <i class="ri-instagram-fill"></i>
                </a>
                <a href="https://twitter.com/" target="_blank" class="home__social-link">
                    <i class="ri-twitter-fill"></i>
                </a>
            </div>

            <div class="home__info">
                <div>
                    <span class="home__info-title">5 best houses to visit</span>
                    <a href="#" class="button button--flex button--link home__info-button">
                        More <i class="ri-arrow-right-line"></i>
                    </a>
                </div>

                <div class="home__info-overlay">
                    <img src="/assets/img/home2.jpg" alt="" class="home__info-img">
                </div>
            </div>
        </div>
    </section>
</main>
<script src="js/main.js"></script>

<?php
    include_once 'components/footer.php';
?>