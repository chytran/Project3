<?php 
    include_once 'includes/database.inc.php';
?>

<!--================ BODY =======================-->
<section class="search__result hero__house" style="background-color: black;">
    <img src="image/resultpage.jpg" alt="" class="search__img">

    <form action="searchtest.php" method="post" class="search__form" style="flex-direction: column;">
        <div class="form__container__main" style="display: flex; justify-content: center; align-content: center; flex-direction: row;">
            <input type="text" name="search" class="search__result__text" placeholder="Enter a city, address, zipcode, property type or sqft...">
            <input type="submit" class="button search__button" name="submit">
        </div>
    </form>
</section>

<?php
    if (isset($_POST['submit'])) {
        $search = filter_input(INPUT_POST, 'search');

        // Download a new excel
        header("Content-type: application/vnd.ms-excel");
        header("Content-Disposition: attachment; filename=zillowdata.csv");

        if (($handle = fopen("mapcode/zillowdata.csv", 'r')) !== false) {
            echo "<table style='width:100%' border='1'>";
                echo "<tr>";
                    echo "<th>latitude</th>";
                    echo "<th>longitude</th>";
                echo "</tr>";
                while (($data = fgetcsv($handle, 1000, ",")) !== false) {           
                    // echo "<p> $num fields in line $row: <br /></p>\n";
                    if ($data[2] == "Corona") {
                        echo "<tr>";
                            echo "<th>" . $data[8] . "</th>";
                            echo "<th>" . $data[9] . "</th>";
                        echo "</tr>";
                    }      
                    else {
                        continue;
                    }
                }
                fclose($handle);
            echo "</table>";
        } 
    }
?>