<?php
    include_once 'includes/database.inc.php';
?>
<?php
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
        echo "<div id='map-canvas' style='width: 800px; height: 500px;'>";
    }
?>
<script>
       var map = null;
        function initialize() {

        var lat='<?php echo $latitude?>';
        var lon='<?php echo $longitude?>';
        // initialize map center on first point
        var latlng = new google.maps.LatLng(lat[0],lon[0]);
        var myOptions = {
            zoom: 10,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
        var bounds = new google.maps.LatLngBounds();

        for (var i=0, i<lat.length; i++) {
        var latlng = new google.maps.LatLng(lat[i],lon[i]);
        bounds.extend(latlng);
        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            title: "Hello World!"
        });
        }
        // zoom and center the map to show all the markers
        map.fitBounds(bounds);
        }
</script>