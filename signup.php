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
        <form action="includes/signup.inc.php" class="form" id="form">
            <h2 class="signup__title">Sign up</h2>

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
                <label for="passRepeat">Name</label>
                <input type="text" name="passRepeat" id="passRepeat" class="passRepeat__input">
            </div>

            <input type="submit" class="button">
        </form>
    </section>
</body>
</html>