<?php
    $row = 1;
    if (($handle = fopen("mapcode/zillowdata.csv", 'r')) !== false) {
        while (($data = fgetcsv($handle, 1000, ",")) !== false) {
            $num = count($data);
            // echo "<p> $num fields in line $row: <br /></p>\n";
            $row++;
            if ($data[2] == "Corona") {
                echo $data[8] . "<br />\n";
                echo $data[9] . "<br />\n";
                echo "<br />\n";
            }      
            else {
                continue;
            }
        }
        fclose($handle);
    }
    // $csv = fopen('mapcode/zillowdata.csv', 'r');

    // while ($row = fgetcsv($csv)) {
    //     if ($row[2] == "Van Nuys") {
    //         echo implode(',', $row);
    //         echo "\n";
    //     }
    // }

    // fclose($csv);
?>