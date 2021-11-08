<?php



if (($handle = fopen("mapcode/zillowdata.csv", 'r')) !== false) {
    echo "<table style='width:100%' border='1'>";
        echo "<tr>";
            echo "<th>address</th>";
            echo "<th>latitude</th>";
            echo "<th>longitude</th>";
        echo "</tr>";
        while (($data = fgetcsv($handle, 1000, ",")) !== false) {
            
            // echo "<p> $num fields in line $row: <br /></p>\n";
            
            if ($data[2] == "Corona") {
                echo "<tr>";
                    echo "<th>" . $data[0] . "</th>";
                    echo "<th>" . $data[8] . "</th>";
                    echo "<th>" . $data[9] . "</th >";
                echo "</tr>";
            }      
            else {
                continue;
            }
        }
        fclose($handle);
    echo "</table>";
}

header("Content-type: application/vnd.ms-excel");
header("Content-Disposition: attachment; filename=coordinates.xls");

echo shell_exec("python3 C:/xampp/htdocs/Project3/foliumtest.py");

?>