<?php
    include_once 'components/header.php';
?>

<section class="search__result hero">
    <form action="includes/houseDetail.inc.php" method="post" class="home__form">
        <input type="text" name="search" class="search__result">
        <input type="submit" class="button" name="submit">
    </form>
</section>

<?php
    include_once 'components/footer.php';
?>