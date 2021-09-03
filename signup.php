<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign up</title>
</head>
<body>
    <section class="hero" id="hero">
        <div class="left__side">
            <h1 class="left__header header__main">Welcome Back!</h1>
            <p class="left__text">To keep connected with us please login with your info</p>
            <a href="login.php" class="button">Sign in</a>
        </div>

        <div class="right__side">
            <form action="includes/signup.inc.php" method="post" class="form" id="form">
                <h2 class="signup__title">Create Account</h2>

                <div class="name__container">
                    <label for="name">Name:</label>
                    <input type="text" name="name" id="name" class="name__input">
                </div>

                <div class="email__container">
                    <label for="email">Email:</label>
                    <input type="email" name="email" id="email" class="email__input">
                </div>

                <div class="password__container">
                    <label for="password">Password:</label>
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
</body>
</html>