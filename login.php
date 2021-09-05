<?php 
    include_once 'components/header.php';
?>

<!--=============== Login ==============-->
<div class="main__container flex__column" id="main-container">
    <img class="bg-main" src="image/main3-signup.jpg" alt="">
    <section class="hero flex__row signup__container" id="hero">
        <div class="left__side flex-column">
            <div class="message__container flex__column">
                <img class="bg" src="image/signup.jpg" alt="">
                <div class="message__holder flex__column">
                    <h1 class="left__header header__main">Welcome Back!</h1>
                    <p class="left__text">To keep connected with us please login with your info</p>
                    <a href="signup.php" class="button">Register Now</a>
                </div>
            </div>
        </div>

        <div class="right__side flex__column">
            <h2 class="signup__title">Sign in</h2>
            <p class="right__text">Please enter your information to sign up now!</p>
            <form action="includes/signup.inc.php" method="post" class="form flex__column" id="form">

                <div class="email__container input__design"> 
                    <div class="input__extra__container">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"><path fill="none" d="M0 0h24v24H0z"/><path d="M3 3h18a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zm17 4.238l-7.928 7.1L4 7.216V19h16V7.238zM4.511 5l7.55 6.662L19.502 5H4.511z"/></svg>
                        <input type="email" name="email" id="email" placeholder="Email" class="email__input  input__info">
                    </div> 
                </div>

                <div class="password__container input__design">
                    <div class="input__extra__container">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"><path fill="none" d="M0 0h24v24H0z"/><path d="M19 10h1a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V11a1 1 0 0 1 1-1h1V9a7 7 0 1 1 14 0v1zM5 12v8h14v-8H5zm6 2h2v4h-2v-4zm6-4V9A5 5 0 0 0 7 9v1h10z"/></svg>
                        <input type="password" name="password" id="password" placeholder="Password" class="password__input input__info">
                    </div>
                </div>

                <input type="submit" class="button">
            </form>
        </div>
    </section>
</div>

<?php
    include_once 'components/footer.php';
?>