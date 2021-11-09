<?php
    
$headers = array("latitude", "longitude");

// array of data
$dates = array(
    array(
        "latitude" => 1,
        "longitude" => 1
    )
);

if (($handle = fopen("mapcode/zillowdata.csv", 'r')) !== false) {
    
    // while (($data = fgetcsv($handle, 1000, ",")) !== false) {
    //     if ($data[2] == "Corona") {
    //         array_push($dates, $data[8], $data[9]);
    //     }
    // }

    $fh = fopen("coordinates.csv", "w");

    // Creates the headers
    fputcsv($fh, $headers);

    // Populate the data
    foreach($dates as $fields) {
        fputcsv($fh, $fields);
    }
    fclose($handle);
    fclose($fh);
}