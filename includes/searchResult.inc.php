
<?php 
    include_once 'database.inc.php';
?>
<div class="house__main__container">

<?php
if (isset($_POST['submit'])) {
    $search = mysqli_real_escape_string($conn, $_POST['search']); 
    $sql = "SELECT * FROM house WHERE city LIKE '%$search%'";
    $result = mysqli_query($conn, $sql);
    $resultCheck = mysqli_num_rows($result);

    if ($resultCheck > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<div class='house__info'>";
                    echo "<p class='house__address'>" . 'Address: ' . $row['Address'] . "</p>";
                    echo "<p class='house__sqft'>" . 'Sqft: ' . $row['Sqft'] . ' sqft' . "</p>";
                    echo "<p class='house__price'>" . 'Price: $' . $row['Price'] . "</p>";
                    echo "<p class='house__zipCode'>" . 'Zip Code: ' . $row['Zip Code'] . "</p>";
                    echo "<p class='house__bedroom'>" . $row['Bedroom'] . ' bedroom' . "</p>";
                    echo "<p class='house__bathroom'>" . $row['Bathroom'] . ' bathroom' . "</p>";
            echo "</div>";
        }
    }   else {
         echo "There are no results matching your search!";
    }
}
?>
</div>