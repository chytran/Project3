<?php
    session_start();
?>
<?php
    include_once 'components/header.php';
?>

<?php 
    include_once 'includes/database.inc.php';
?>

<header class="header" id="header">
    <nav class="nav container">
        <a href="index.php" class="nav__logo">Home</a>

        <div class="nav__menu" id="nav-menu">
            <ul class="nav__list">
                <li class="nav__item">
                    <a href="index.php" class="nav__link">Home</a>
                </li>
                <li class="nav__item">
                    <a href="searchResult.php" class="nav__link">Search</a>
                </li>
                <li class="nav__item">
                    <?php if(isset($_SESSION["userid"]) || isset($_SESSION["useremail"])) { ?>
                        <a href="includes/logout.inc.php" class="nav__link">Logout</a>
                    <?php } else { ?>
                        <a href="login.php" class="nav__link">Login</a>
                    <?php } ?>
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

    <form action="searchResult.php" method="post" class="search__form">
        <input type="text" name="search" class="search__result__text" placeholder="Enter a city, address, zipcode, property type or sqft...">
        <input type="submit" class="button search__button" name="submit">
    </form>
    
    <?php if(isset($_SESSION["userid"]) || isset($_SESSION["useremail"])) { ?>
        <div class="zipCode__expand">
            <input type="text" id="name"> 
            <a href='javascript:setup()' id="import">Get Details</a>              
        </div>
    <?php } else { ?>
        
    <?php } ?>
    
    <div id="map" class="map__container" style="height: 400px; width: 350px; position: relative; z-index: 100;">
        <!-- <iframe style="position: relative; z-index: 100;" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3172.370930560317!2d-121.89211318474916!3d37.3337261798421!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fccbb4e751f57%3A0x7bb970c4219e6acd!2sSan%20Jos%C3%A9%20Museum%20of%20Art!5e0!3m2!1sen!2sus!4v1632683176648!5m2!1sen!2sus" width="350" height="400" style="border:0;" allowfullscreen="" loading="lazy"></iframe> -->
    </div>

</section>

<section class="house__show hero__house" id="house-show">
<?php
if (isset($_POST['submit'])) {
    $search = mysqli_real_escape_string($conn, $_POST['search']); 
    $sql = "SELECT * FROM house WHERE 
            City LIKE '%$search%' OR 
            Sqft LIKE '%$search%' OR
            Address LIKE '%$search%' OR 
            zipCode LIKE '%$search%'
            ";
    $result = mysqli_query($conn, $sql);
    $resultCheck = mysqli_num_rows($result);

    // Attempt to create a map with php
    // Query 2
    $sql1 = "SELECT * FROM house";
    $result1 = mysqli_query($conn, $sql1);
    $resultCheck1 = mysqli_num_rows($result1);

    if ($resultCheck1 > 0) {
        while ($row1 = mysqli_fetch_assoc($result1)) {
            $latitude = $row1["Latitude"];
            $longitude = $row1["Longitude"];
            $locations[]=array ( 'lat'=>$latitude, 'lng'=>$longitude);
        }
    }
    
    // If the query result is not empty, list all items
    if ($resultCheck > 0) {
        echo "<section class='house__show hero__house' id='house-show'>";
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<div class='house__info'>";
                echo "<p class='house__address'>" . 'Address: ' . $row['Address'] . "</p>";
                echo "<p class='house__sqft'>" . 'Sqft: ' . $row['Sqft'] . ' sqft' . "</p>";
                echo "<p class='house__price'>" . 'Price: $' . $row['Price'] . "</p>";
                echo "<p class='house__zipCode'>" . 'Zip Code: ' . $row['zipCode'] . "</p>";
                echo "<p class='house__bedroom'>" . $row['Bedroom'] . ' bedroom' . "</p>";
                echo "<p class='house__bathroom'>" . $row['Bathroom'] . ' bathroom' . "</p>";
            echo "</div>";
        }
        echo "</section>";
    }  else {
         echo "There are no results matching your search!";
    }
}
?>

<script src="js/search.js"></script>
<script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyA7IZt-36CgqSGDFK8pChUdQXFyKIhpMBY&sensor=true" type="text/javascript"></script>
<script>
    function setup() {
        const message = document.getElementById("name").value;
        // alert(`<a id="import" href="ms-excel:ofe|u|file:///C:/Users/kevin/OneDrive/Documents/excel/ACS Housing Summary, ${message}.xlsx">Open in Excel</a>`);
        // console.log(message);
        document.getElementById("import").innerHTML = `<a id="import" href="ms-excel:ofe|u|file:///C:/xampp/htdocs/Project3/excel/HousingSummary/ACS Housing Summary, ${message}.xlsx">Open in Excel</a>`;
    }
</script>
<?php
    include_once 'components/footer.php';
?>