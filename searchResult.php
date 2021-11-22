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
    <div class="search__containing" style="align-self: center; display: flex; justify-content: center; align-content: center; position: relative; flex-direction: column;">
        <form action="searchResult.php" method="post" class="search__form" style="flex-direction: column;">
            <!-- <div class="user__container input__design" style="z-index:100; align-self: center; width: 100%;">
                <div class="input__extra__container">
                    <div class="radio__container" style="margin: 0.2rem;">
                        <label for="workAddress">Filtered Search</label>
                        <input type="radio" name="searchType" id="workAddress" value="Filtered Search" checked="checked">
                    </div>

                    <div class="radio__container" style="margin: 0.2rem;">
                        <label for="homeDetailed">Preferred Home Details</label>
                        <input type="radio" name="searchType" id="homeDetailed" value="Preferred Home Details">
                    </div>

                    <div class="radio__container" style="margin: 0.2rem;">
                        <label for="prefZipcode">Preferred Zipcode</label>
                        <input type="radio" name="searchType" id="prefZipcode" value="Preferred Zipcode">
                    </div>  
                </div>
            </div> -->
            <div class="form__container__main" style="display: flex; justify-content: center; align-content: center; flex-direction: row;">
                <input type="text" name="search" class="search__result__text" placeholder="Enter a city, address, zipcode, or sqft...">
                <input type="submit" class="button search__button" name="submit">
            </div>
            <div class="user__container input__design" style="z-index:100; align-self: center; width: 40%;">
                <div class="input__extra__container" >
                    <p style="text-decoration: underline; padding-right: 1rem;">Filters:</p>
                    <div class="radio__container" style="margin: 0.2rem;">
                        <label for="crime">Crime Rate</label>
                        <input type="radio" name="filter" id="crime" value="crime">
                    </div> 
                    <div class="radio__container" style="margin: 0.2rem;">
                        <label for="medianIncome">Median Income</label>
                        <input type="radio" name="filter" id="medianIncome" value="medianIncome">
                    </div> 
                    <div class="radio__container" style="margin: 0.2rem;">
                        <label for="internet">Internet Access</label>
                        <input type="radio" name="filter" id="internet" value="internet">
                    </div> 
                    <div class="radio__container" style="margin: 0.2rem;">
                        <label for="bathroom">Bathroom</label>
                        <input type="radio" name="filter" id="bathroom" value="bathroom">
                        <!-- <input type="text" name="bathroom" id="bathroom"> -->
                    </div> 
                    <div class="radio__container" style="margin: 0.2rem;">
                        <label for="bedroom">Bedroom</label>
                        <input type="radio" name="filter" id="bedroom" value="bedroom">
                    </div> 
                </div>
            </div>
        </form>
        
        

        <?php if(isset($_SESSION["userid"]) || isset($_SESSION["useremail"])) { ?>
            <div class="zipCode__expand" style="margin-top: 1rem; ">
                <!-- <label style="width: 100%; background-color: #FFFFFF; color: #121212;" for="name">Get full details of any specific Zip Code</label> -->
                <input class="search__result__text" style="width: 50%;" type="text" id="name" placeholder="Check zip code..."> 
                <a class="button" href='javascript:setup()' id="import">Get Details</a>              
            </div>
        <?php } else { ?>
            
        <?php } ?>                
    </div>
    
    <div id="map" class="map__container" style="height: 300px; width: 350px; position: relative; z-index: 100; align-self: center;"> 
        <iframe src="mapcode/foliumhtml.html" title="test map" style="border:none;width:500px;height:450px;align-self:center; margin-top:-35%; margin-left: -21%;"></iframe>
    </div>

</section>


<!-- <section class="house__show hero__house" id="house-show"> -->
<?php


if (isset($_POST['submit'])) {
    $searchType = filter_input(INPUT_POST, 'searchType');
    $filter = filter_input(INPUT_POST, 'filter');
    $bathroomFilter = filter_input(INPUT_POST, 'bathroom');

    if ($filter == "crime") {
        $search = mysqli_real_escape_string($conn, $_POST['search']); 
        $sql = "SELECT *
                FROM house  
                LEFT JOIN house2 ON house.zipCode = house2.zipCode
                WHERE 
                house.City LIKE '%$search%' OR 
                house.Sqft LIKE '%$search%' OR
                house.Address LIKE '%$search%' OR 
                house2.zipCode LIKE '%$search%'
                ORDER BY house2.crime
                ";
        $result = mysqli_query($conn, $sql);
        $resultCheck = mysqli_num_rows($result);

        // Query 2
        $sql1 = "SELECT * FROM house2 WHERE 
        zipCode LIKE '%$search%'
        ";
        $result1 = mysqli_query($conn, $sql1);
        $resultCheck1 = mysqli_num_rows($result1);

        // Query 3
        $sql2 = "SELECT Price FROM house WHERE 
        zipCode LIKE '%$search%'
        order by Price desc
        limit 1
        ";
        $result2 = mysqli_query($conn, $sql2);
        $resultCheck2 = mysqli_num_rows($result2);

        
        // If the query result is not empty, list all items
        // Start of full container
        echo "<section class='house__show hero__house__2' id='house-show'>";
            echo " <img src='image/blue1.jpg' alt='' class='search__img'>";
            // Left Side
            if ($resultCheck > 0) {
                echo "<section class='house__show__2'>";
                while ($row = mysqli_fetch_assoc($result)) {
                    echo "<div class='house__info' style='width: 95%; height: 204px; background-color: #FEFEFA; margin-top: 0.5rem; margin-bottom: 0.3rem; border-bottom: 0.5px #F8F8F8 solid;'>";
                        echo "<p class='house__address' style='padding-left: 0.5rem; font-size: 1.3rem;'>" . 'Address: ' . $row['Address'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 0.5rem;'>" . 'Sqft: ' . $row['Sqft'] . ' sqft' . "</p>";
                        echo "<p class='house__price' style='padding-left: 0.5rem;'>" . 'Price: $' . $row['Price'] . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 0.5rem;'>" . 'Zip Code: ' . $row['zipCode'] . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 0.5rem;'>" . $row['Bedroom'] . ' bedroom' . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . $row['Bathroom'] . ' bathroom' . "</p>";               
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . "crime rate at zip code" . "(" . $row['zipCode'] . ")" . ": " . $row['crime'] . "</p>"; 
                    echo "</div>";
                }
                echo "</section>";

                // $csvfile = fopen('/mapcode/result.csv', 'w');
                // fputcsv($csvfile, $row);

            }  else {
                echo "There are no results matching your search!";
            }

            // Right Side
            if ($resultCheck1 > 0) {
                echo "<section class='house__show__2'>";
                while ($row1 = mysqli_fetch_assoc($result1)) {
                    echo "<div class='house__info' style='margin-left: 0.5rem; width: 95%; margin-top: 0.5rem; border: 0.5px solid #121212; background-color: #FEFEFA; color: #121212; padding: 0.5rem;'>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-weight: 700; font-size: 1.5rem;'>" . 'Zip Code: ' . $row1['zipCode'] . "</p>";
                        while ($row2 = mysqli_fetch_assoc($result2)) {
                            echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Highest Priced House: $' . $row2['Price'] . "</p>";
                        }
                        echo "<p class='house__address' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Median Income: $' . $row1['medianIncome'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Bachelor Degrees: ' . $row1['bachelor'] . ' degrees' . "</p>";
                        echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Master Degrees: ' . $row1['gradSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'High School Degrees: ' . $row1['highSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Internet Access: ' . $row1['internetAccess'] . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Crimes: ' . $row1['crime'] . "</p>";
                    echo "</div>";
                }
                echo "</section>";

            }  else {
                echo "Only displays info from zip code searches";
            }
        // End
        echo "</section>";
    }
    if ($filter == "medianIncome") {
        $search = mysqli_real_escape_string($conn, $_POST['search']); 
        $sql = "SELECT *
                FROM house  
                LEFT JOIN house2 ON house.zipCode = house2.zipCode
                WHERE 
                house.City LIKE '%$search%' OR 
                house.Sqft LIKE '%$search%' OR
                house.Address LIKE '%$search%' OR 
                house2.zipCode LIKE '%$search%'
                ORDER BY house2.medianIncome
                ";
        $result = mysqli_query($conn, $sql);
        $resultCheck = mysqli_num_rows($result);

        // Query 2
        $sql1 = "SELECT * FROM house2 WHERE 
        zipCode LIKE '%$search%'
        ";
        $result1 = mysqli_query($conn, $sql1);
        $resultCheck1 = mysqli_num_rows($result1);

        // Query 3
        $sql2 = "SELECT Price FROM house WHERE 
        zipCode LIKE '%$search%'
        order by Price desc
        limit 1
        ";
        $result2 = mysqli_query($conn, $sql2);
        $resultCheck2 = mysqli_num_rows($result2);

        
        // If the query result is not empty, list all items
        // Start of full container
        echo "<section class='house__show hero__house__2' id='house-show'>";
        echo " <img src='image/blue1.jpg' alt='' class='search__img'>";
            // Left Side
            if ($resultCheck > 0) {
                echo "<section class='house__show__2'>";
                while ($row = mysqli_fetch_assoc($result)) {
                    echo "<div class='house__info' style='width: 95%; height: 204px; background-color: #FEFEFA; margin-top: 0.5rem; margin-bottom: 0.3rem; border-bottom: 0.5px #F8F8F8 solid;'>";
                        echo "<p class='house__address' style='padding-left: 0.5rem; font-size: 1.3rem;'>" . 'Address: ' . $row['Address'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 0.5rem;'>" . 'Sqft: ' . $row['Sqft'] . ' sqft' . "</p>";
                        echo "<p class='house__price' style='padding-left: 0.5rem;'>" . 'Price: $' . $row['Price'] . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 0.5rem;'>" . 'Zip Code: ' . $row['zipCode'] . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 0.5rem;'>" . $row['Bedroom'] . ' bedroom' . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . $row['Bathroom'] . ' bathroom' . "</p>";               
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . "crime rate at zip code " . "(" . $row['zipCode'] . ")" . ": " . $row['crime'] . "</p>"; 
                    echo "</div>";
                }
                echo "</section>";

            }  else {
                echo "There are no results matching your search!";
            }

            // Right Side
            if ($resultCheck1 > 0) {
                echo "<section class='house__show__2'>";
                while ($row1 = mysqli_fetch_assoc($result1)) {
                    echo "<div class='house__info' style='margin-left: 0.5rem; width: 95%; margin-top: 0.5rem; border: 0.5px solid #121212; background-color: #FEFEFA; color: #121212; padding: 0.5rem;'>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-weight: 700; font-size: 1.5rem;'>" . 'Zip Code: ' . $row1['zipCode'] . "</p>";
                        while ($row2 = mysqli_fetch_assoc($result2)) {
                            echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Highest Priced House: $' . $row2['Price'] . "</p>";
                        }
                        echo "<p class='house__address' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Median Income: $' . $row1['medianIncome'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Bachelor Degrees: ' . $row1['bachelor'] . ' degrees' . "</p>";
                        echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Master Degrees: ' . $row1['gradSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'High School Degrees: ' . $row1['highSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Internet Access: ' . $row1['internetAccess'] . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Crimes: ' . $row1['crime'] . "</p>";
                    echo "</div>";
                }
                echo "</section>";

            }  else {
                echo "Only displays info from zip code searches";
            }
        // End
        echo "</section>";
    }
    if ($filter == "internet") {
        $search = mysqli_real_escape_string($conn, $_POST['search']); 
        $sql = "SELECT *
                FROM house  
                LEFT JOIN house2 ON house.zipCode = house2.zipCode
                WHERE 
                house.City LIKE '%$search%' OR 
                house.Sqft LIKE '%$search%' OR
                house.Address LIKE '%$search%' OR 
                house2.zipCode LIKE '%$search%'
                ORDER BY house2.internetAccess
                ";
        $result = mysqli_query($conn, $sql);
        $resultCheck = mysqli_num_rows($result);

        // Query 2
        $sql1 = "SELECT * FROM house2 WHERE 
        zipCode LIKE '%$search%'
        ";
        $result1 = mysqli_query($conn, $sql1);
        $resultCheck1 = mysqli_num_rows($result1);

        // Query 3
        $sql2 = "SELECT Price FROM house WHERE 
        zipCode LIKE '%$search%'
        order by Price desc
        limit 1
        ";
        $result2 = mysqli_query($conn, $sql2);
        $resultCheck2 = mysqli_num_rows($result2);

        
        // If the query result is not empty, list all items
        // Start of full container
        echo "<section class='house__show hero__house__2' id='house-show'>";
        echo " <img src='image/blue1.jpg' alt='' class='search__img'>";
            // Left Side
            if ($resultCheck > 0) {
                echo "<section class='house__show__2'>";
                while ($row = mysqli_fetch_assoc($result)) {
                    echo "<div class='house__info' style='width: 95%; height: 204px; background-color: #FEFEFA; margin-top: 0.5rem; margin-bottom: 0.3rem; border-bottom: 0.5px #F8F8F8 solid;'>";
                        echo "<p class='house__address' style='padding-left: 0.5rem; font-size: 1.3rem;'>" . 'Address: ' . $row['Address'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 0.5rem;'>" . 'Sqft: ' . $row['Sqft'] . ' sqft' . "</p>";
                        echo "<p class='house__price' style='padding-left: 0.5rem;'>" . 'Price: $' . $row['Price'] . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 0.5rem;'>" . 'Zip Code: ' . $row['zipCode'] . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 0.5rem;'>" . $row['Bedroom'] . ' bedroom' . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . $row['Bathroom'] . ' bathroom' . "</p>";               
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . "crime rate at zip code" . "(" . $row['zipCode'] . ")" . ": " . $row['crime'] . "</p>"; 
                    echo "</div>";
                }
                echo "</section>";

            }  else {
                echo "There are no results matching your search!";
            }

            // Right Side
            if ($resultCheck1 > 0) {
                echo "<section class='house__show__2'>";
                while ($row1 = mysqli_fetch_assoc($result1)) {
                    echo "<div class='house__info' style='margin-left: 0.5rem; width: 95%; margin-top: 0.5rem; border: 0.5px solid #121212; background-color: #FEFEFA; color: #121212; padding: 0.5rem;'>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-weight: 700; font-size: 1.5rem;'>" . 'Zip Code: ' . $row1['zipCode'] . "</p>";
                        while ($row2 = mysqli_fetch_assoc($result2)) {
                            echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Highest Priced House: $' . $row2['Price'] . "</p>";
                        }
                        echo "<p class='house__address' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Median Income: $' . $row1['medianIncome'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Bachelor Degrees: ' . $row1['bachelor'] . ' degrees' . "</p>";
                        echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Master Degrees: ' . $row1['gradSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'High School Degrees: ' . $row1['highSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Internet Access: ' . $row1['internetAccess'] . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Crimes: ' . $row1['crime'] . "</p>";
                    echo "</div>";
                }
                echo "</section>";

            }  else {
                echo "Only displays info from zip code searches";
            }
        // End
        echo "</section>";
    }
    if ($filter == "bathroom") {
        $search = mysqli_real_escape_string($conn, $_POST['search']); 
        // $bathroomSearch = mysqli_real_escape_string($conn, $_POST['bathroom']); 

        $sql = "SELECT *
                FROM house  
                LEFT JOIN house2 ON house.zipCode = house2.zipCode
                WHERE 
                house.City LIKE '%$search%' OR 
                house.Sqft LIKE '%$search%' OR
                house.Address LIKE '%$search%' OR 
                house2.zipCode LIKE '%$search%'
                ORDER BY house.bathroom
                ";
        $result = mysqli_query($conn, $sql);
        $resultCheck = mysqli_num_rows($result);

        // Query 2
        $sql1 = "SELECT * FROM house2 WHERE 
        zipCode LIKE '%$search%'
        ";
        $result1 = mysqli_query($conn, $sql1);
        $resultCheck1 = mysqli_num_rows($result1);

        // Query 3
        $sql2 = "SELECT Price FROM house WHERE 
        zipCode LIKE '%$search%'
        order by Price desc
        limit 1
        ";
        $result2 = mysqli_query($conn, $sql2);
        $resultCheck2 = mysqli_num_rows($result2);

        
        // If the query result is not empty, list all items
        // Start of full container
        echo "<section class='house__show hero__house__2' id='house-show'>";
        echo " <img src='image/blue1.jpg' alt='' class='search__img'>";
            // Left Side
            if ($resultCheck > 0) {
                echo "<section class='house__show__2'>";
                while ($row = mysqli_fetch_assoc($result)) {
                    echo "<div class='house__info' style='width: 95%; height: 204px; background-color: #FEFEFA; margin-top: 0.5rem; margin-bottom: 0.3rem; border-bottom: 0.5px #F8F8F8 solid;'>";
                        echo "<p class='house__address' style='padding-left: 0.5rem; font-size: 1.3rem;'>" . 'Address: ' . $row['Address'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 0.5rem;'>" . 'Sqft: ' . $row['Sqft'] . ' sqft' . "</p>";
                        echo "<p class='house__price' style='padding-left: 0.5rem;'>" . 'Price: $' . $row['Price'] . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 0.5rem;'>" . 'Zip Code: ' . $row['zipCode'] . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 0.5rem;'>" . $row['Bedroom'] . ' bedroom' . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . $row['Bathroom'] . ' bathroom' . "</p>";               
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . "crime rate at zip code" . "(" . $row['zipCode'] . ")" . ": " . $row['crime'] . "</p>"; 
                    echo "</div>";
                }
                echo "</section>";

            }  else {
                echo "There are no results matching your search!";
            }

            // Right Side
            if ($resultCheck1 > 0) {
                echo "<section class='house__show__2'>";
                while ($row1 = mysqli_fetch_assoc($result1)) {
                    echo "<div class='house__info' style='margin-left: 0.5rem; width: 95%; margin-top: 0.5rem; border: 0.5px solid #121212; background-color: #FEFEFA; color: #121212; padding: 0.5rem;'>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-weight: 700; font-size: 1.5rem;'>" . 'Zip Code: ' . $row1['zipCode'] . "</p>";
                        while ($row2 = mysqli_fetch_assoc($result2)) {
                            echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Highest Priced House: $' . $row2['Price'] . "</p>";
                        }
                        echo "<p class='house__address' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Median Income: $' . $row1['medianIncome'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Bachelor Degrees: ' . $row1['bachelor'] . ' degrees' . "</p>";
                        echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Master Degrees: ' . $row1['gradSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'High School Degrees: ' . $row1['highSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Internet Access: ' . $row1['internetAccess'] . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Crimes: ' . $row1['crime'] . "</p>";
                    echo "</div>";
                }
                echo "</section>";

            }  else {
                echo "Only displays info from zip code searches";
            }
        // End
        echo "</section>";
    }
    if ($filter == "bedroom") {
        $search = mysqli_real_escape_string($conn, $_POST['search']); 
        
        $sql = "SELECT *
                FROM house  
                LEFT JOIN house2 ON house.zipCode = house2.zipCode
                WHERE 
                house.City LIKE '%$search%' OR 
                house.Sqft LIKE '%$search%' OR
                house.Address LIKE '%$search%' OR 
                house2.zipCode LIKE '%$search%'
                ORDER BY house.bedroom
                ";
        $result = mysqli_query($conn, $sql);
        $resultCheck = mysqli_num_rows($result);

        // Query 2
        $sql1 = "SELECT * FROM house2 WHERE 
        zipCode LIKE '%$search%'
        ";
        $result1 = mysqli_query($conn, $sql1);
        $resultCheck1 = mysqli_num_rows($result1);

        // Query 3
        $sql2 = "SELECT Price FROM house WHERE 
        zipCode LIKE '%$search%'
        order by Price desc
        limit 1
        ";
        $result2 = mysqli_query($conn, $sql2);
        $resultCheck2 = mysqli_num_rows($result2);

        
        // If the query result is not empty, list all items
        // Start of full container
        echo "<section class='house__show hero__house__2' id='house-show'>";
        echo " <img src='image/blue1.jpg' alt='' class='search__img'>";


        
            // Left Side
            if ($resultCheck > 0) {
                echo "<section class='house__show__2'>";
                while ($row = mysqli_fetch_assoc($result)) {
                    echo "<div class='house__info' style='width: 95%; height: 204px; background-color: #FEFEFA; margin-top: 0.5rem; margin-bottom: 0.3rem; border-bottom: 0.5px #F8F8F8 solid;'>";
                        echo "<p class='house__address' style='padding-left: 0.5rem; font-size: 1.3rem;'>" . 'Address: ' . $row['Address'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 0.5rem;'>" . 'Sqft: ' . $row['Sqft'] . ' sqft' . "</p>";
                        echo "<p class='house__price' style='padding-left: 0.5rem;'>" . 'Price: $' . $row['Price'] . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 0.5rem;'>" . 'Zip Code: ' . $row['zipCode'] . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 0.5rem;'>" . $row['Bedroom'] . ' bedroom' . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . $row['Bathroom'] . ' bathroom' . "</p>";               
                        echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . "crime rate at zip code" . "(" . $row['zipCode'] . ")" . ": " . $row['crime'] . "</p>"; 
                    echo "</div>";
                }
                echo "</section>";
            }  else {
                echo "There are no results matching your search!";
            }

            // Right Side
            if ($resultCheck1 > 0) {
                echo "<section class='house__show__2'>";
                while ($row1 = mysqli_fetch_assoc($result1)) {
                    echo "<div class='house__info' style='margin-left: 0.5rem; width: 95%; margin-top: 0.5rem; border: 0.5px solid #121212; background-color: #FEFEFA; color: #121212; padding: 0.5rem;'>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-weight: 700; font-size: 1.5rem;'>" . 'Zip Code: ' . $row1['zipCode'] . "</p>";
                        while ($row2 = mysqli_fetch_assoc($result2)) {
                            echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Highest Priced House: $' . $row2['Price'] . "</p>";
                        }
                        echo "<p class='house__address' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Median Income: $' . $row1['medianIncome'] . "</p>";
                        echo "<p class='house__sqft' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Bachelor Degrees: ' . $row1['bachelor'] . ' degrees' . "</p>";
                        echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Master Degrees: ' . $row1['gradSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__zipCode' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'High School Degrees: ' . $row1['highSchool'] . ' degrees' . "</p>";
                        echo "<p class='house__bedroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Internet Access: ' . $row1['internetAccess'] . "</p>";
                        echo "<p class='house__bathroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Crimes: ' . $row1['crime'] . "</p>";
                    echo "</div>";
                }
                echo "</section>";

            }  else {
                echo "Only displays info from zip code searches";
            }
        // End
        echo "</section>";
    }
    // else if ($searchType == "Filtered Search"){
    //     // echo '<script>alert("Must click a filter preference on Filtered Search")</script>';
    // }

    //================= Preferred Searched =======================//
    // if ($searchType == "Preferred Home Details") {
    //     $search = mysqli_real_escape_string($conn, $_POST['search']); 
    //     $sql = "SELECT * FROM house WHERE 
    //             City LIKE '%$search%' OR 
    //             Sqft LIKE '%$search%' OR
    //             Address LIKE '%$search%' OR 
    //             zipCode LIKE '%$search%'
    //             ";
    //     $result = mysqli_query($conn, $sql);
    //     $resultCheck = mysqli_num_rows($result);
        
    //     // Query 2
    //     $sql1 = "SELECT * FROM house2 WHERE 
    //             zipCode LIKE '%$search%'
    //             ";
    //     $result1 = mysqli_query($conn, $sql1);
    //     $resultCheck1 = mysqli_num_rows($result1);

    //     // Query 3
    //     $sql2 = "SELECT Price FROM house WHERE 
    //             zipCode LIKE '%$search%'
    //             order by Price desc
    //             limit 1
    //             ";
    //     $result2 = mysqli_query($conn, $sql2);
    //     $resultCheck2 = mysqli_num_rows($result2);


    //     // If the query result is not empty, list all items
    //     // Start of full container
    //     echo "<section class='house__show hero__house__2' id='house-show'>";

    //         // Left Side
    //         if ($resultCheck > 0) {
    //             echo "<section class='house__show__2'>";
    //             while ($row = mysqli_fetch_assoc($result)) {
    //                 echo "<div class='house__info' style='height: 204px;'>";
    //                     echo "<p class='house__address' style='padding-left: 0.5rem; font-size: 1.3rem;'>" . 'Address: ' . $row['Address'] . "</p>";
    //                     echo "<p class='house__sqft' style='padding-left: 0.5rem;'>" . 'Sqft: ' . $row['Sqft'] . ' sqft' . "</p>";
    //                     echo "<p class='house__price' style='padding-left: 0.5rem;'>" . 'Price: $' . $row['Price'] . "</p>";
    //                     echo "<p class='house__zipCode' style='padding-left: 0.5rem;'>" . 'Zip Code: ' . $row['zipCode'] . "</p>";
    //                     echo "<p class='house__bedroom' style='padding-left: 0.5rem;'>" . $row['Bedroom'] . ' bedroom' . "</p>";
    //                     echo "<p class='house__bathroom' style='padding-left: 0.5rem;'>" . $row['Bathroom'] . ' bathroom' . "</p>";
    //                 echo "</div>";
    //             }
    //             echo "</section>";

    //         }  else {
    //             echo "There are no results matching your search!";
    //         }

    //         // Right Side
    //         if ($resultCheck1 > 0) {
    //             echo "<section class='house__show__2'>";
    //             while ($row1 = mysqli_fetch_assoc($result1)) {
    //                 echo "<div class='house__info' style='border: 2px solid #121212; padding: 0.5rem;'>";
    //                     echo "<p class='house__zipCode' style='padding-left: 1rem; font-weight: 700; font-size: 1.5rem;'>" . 'Zip Code: ' . $row1['zipCode'] . "</p>";
    //                     while ($row2 = mysqli_fetch_assoc($result2)) {
    //                         echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Highest Priced House: $' . $row2['Price'] . "</p>";
    //                     }
    //                     echo "<p class='house__address' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Median Income: $' . $row1['medianIncome'] . "</p>";
    //                     echo "<p class='house__sqft' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Bachelor Degrees: ' . $row1['bachelor'] . ' degrees' . "</p>";
    //                     echo "<p class='house__price' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Master Degrees: ' . $row1['gradSchool'] . ' degrees' . "</p>";
    //                     echo "<p class='house__zipCode' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'High School Degrees: ' . $row1['highSchool'] . ' degrees' . "</p>";
    //                     echo "<p class='house__bedroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Internet Access: ' . $row1['internetAccess'] . "</p>";
    //                     echo "<p class='house__bathroom' style='padding-left: 1rem; font-size: 1.3rem;'>" . 'Crimes: ' . $row1['crime'] . "</p>";
    //                 echo "</div>";
    //             }
    //             echo "</section>";

    //         }  else {
    //             echo "Only displays info from zip code searches";
    //         }
    //     // End
    //     echo "</section>";
    // }
}

// if (isset($_POST['submit']) && $searchType == "Preferred Home Details") {
//     $search = mysqli_real_escape_string($conn, $_POST['search']); 
//     $sql = "SELECT * FROM house WHERE 
//             City LIKE '%$search%' OR 
//             Sqft LIKE '%$search%' OR
//             Address LIKE '%$search%' OR 
//             zipCode LIKE '%$search%'
//             ";
//     $result = mysqli_query($conn, $sql);
//     $resultCheck = mysqli_num_rows($result);

//     // Attempt to create a map with php
//     // Query 2
//     $sql1 = "SELECT * FROM house2";
//     $result1 = mysqli_query($conn, $sql1);
//     $resultCheck1 = mysqli_num_rows($result1);
    
//     if ($resultCheck1 > 0) {
//         while ($row1 = mysqli_fetch_assoc($result1)) {
//             $latitude = $row1["Latitude"];
//             $longitude = $row1["Longitude"];
//             $locations[]=array ( 'lat'=>$latitude, 'lng'=>$longitude);
//         }
//     }

//     // If the query result is not empty, list all items
//     if ($resultCheck > 0) {
//         echo "<section class='house__show hero__house' id='house-show'>";
//         while ($row = mysqli_fetch_assoc($result)) {
//             echo "<div class='house__info'>";
//                 echo "<p class='house__address'>" . 'Address: ' . $row['Address'] . "</p>";
//                 echo "<p class='house__zipCode'>" . 'Zip Code: ' . $row['zipCode'] . "</p>";
//                 echo "<p class='house__price'>" . 'Price: $' . $row['Price'] . "</p>";
//                 echo "<p class='house__bedroom'>" . $row['Bedroom'] . ' bedroom' . "</p>";
//                 echo "<p class='house__bathroom'>" . $row['Bathroom'] . ' bathroom' . "</p>";
//             echo "</div>";
//         }
//         echo "</section>";
//     }  else {
//          echo "There are no results matching your search!";
//     }
// }

?>

<script src="js/search.js"></script>
<script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyA7IZt-36CgqSGDFK8pChUdQXFyKIhpMBY&sensor=true" type="text/javascript"></script>
<script>
    function setup() {
        const message = document.getElementById("name").value;
        // alert(`<a id="import" href="ms-excel:ofe|u|file:///C:/Users/kevin/OneDrive/Documents/excel/ACS Housing Summary, ${message}.xlsx">Open in Excel</a>`);
        // console.log(message);
        document.getElementById("import").innerHTML = `<a style="color: #FFF;" id="import" href="ms-excel:ofe|u|file:///C:/xampp/htdocs/Project3/excel/HousingSummary/ACS Housing Summary, ${message}.xlsx">Open in Excel</a>`;
    }
</script>
<?php
    include_once 'components/footer.php';
?>