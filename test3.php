<?php

header("Content-type: application/vnd.ms-excel");
header("Content-Disposition: attachment; filename=chillyfacts.xls");

if (($handle = fopen("mapcode/zillowdata.csv", 'r')) !== false) {
    echo "<table style='width:100%' border='1'>";
        while (($data = fgetcsv($handle, 1000, ",")) !== false) {
            $num = count($data);
            // echo "<p> $num fields in line $row: <br /></p>\n";
            $row++;
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

?>