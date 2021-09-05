<?php 
    include_once 'components/header.php';
?>
<div class="main__container flex__column" id="main-container">
    <img class="bg-main" src="image/main3-signup.jpg" alt="">
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
            <p class="right__text">Please enter your information to sign up now!</p>
            <form action="includes/signup.inc.php" method="post" class="form flex__column" id="form">

                <div class="name__container input__design">
                    <div class="input__extra__container">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"><path fill="none" d="M0 0h24v24H0z"/><path d="M4 22a8 8 0 1 1 16 0h-2a6 6 0 1 0-12 0H4zm8-9c-3.315 0-6-2.685-6-6s2.685-6 6-6 6 2.685 6 6-2.685 6-6 6zm0-2c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4z"/></svg>
                        <input type="text" name="name" id="name" placeholder="Name" class="name__input input__info">
                    </div>
                </div>

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

                <div class="passRepeat__container input__design">
                    <div class="input__extra__container">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"><path fill="none" d="M0 0h24v24H0z"/><path d="M18 8h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h2V7a6 6 0 1 1 12 0v1zM5 10v10h14V10H5zm6 4h2v2h-2v-2zm-4 0h2v2H7v-2zm8 0h2v2h-2v-2zm1-6V7a4 4 0 1 0-8 0v1h8z"/></svg>
                        <input type="password" name="passRepeat" id="passRepeat" placeholder="Confirm Password" class="passRepeat__input input__info">
                    </div>
                </div>

                <button type="submit" name="submit" class="button">Submit</button>
                <!-- <input type="submit" class="button"> -->
            </form>
        </div>
    </section>
</div>
<?php
    include_once 'components/footer.php';
?>