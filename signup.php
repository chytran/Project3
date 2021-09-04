<?php 
    include_once 'components/header.php';
?>
<div class="main__container flex__column" id="main-container">
    <img class="bg-main" src="image/search-background.jpg" alt="">
    <section class="hero flex__row signup__container" id="hero">
        <div class="left__side flex-column">
            <div class="message__container flex__column">
                <img class="bg" src="image/signup.jpg" alt="">
                <div class="message__holder flex__column">
                    <h1 class="left__header header__main">Welcome Back!</h1>
                    <p class="left__text">To keep connected with us please login with your info</p>
                    <a href="login.php" class="button">Sign in</a>
                </div>
            </div>
        </div>

        <div class="right__side flex__column">
            <h2 class="signup__title">Create Account</h2>
            <form action="includes/signup.inc.php" method="post" class="form" id="form">

                <div class="name__container">
                    <input type="text" name="name" id="name" class="name__input">
                </div>

                <div class="email__container">           
                    <input type="email" name="email" id="email" class="email__input">
                </div>

                <div class="password__container">
                    <input type="password" name="password" id="password" class="password__input">
                </div>

                <div class="passRepeat__container">
                    <label for="passRepeat">Password Confirmation:</label>
                    <input type="text" name="passRepeat" id="passRepeat" class="passRepeat__input">
                </div>

                <input type="submit" class="button">
            </form>
        </div>
    </section>
</div>
<?php
    include_once 'components/footer.php';
?>