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
    }
?>
<script>
       //var myLatLng = {lat: -25.363, lng: 131.044};
       function initMap() {
        var myLatLng = {lat: -25.363, lng: 131.044};

        var map = new google.maps.Map(document.getElementById('map'), {
          center: myLatLng,
          scrollwheel: false,
          zoom: 4
         });

        <?php for($i=0;$i<sizeof($locations);$i++)
        { ?>
         var marker = new google.maps.Marker({
          map: map,
          position: {lat: <?php echo $locations[$i]['lat']?>,lng: <?php echo $locations[$i]['lng']?>},
          title: 'Service'
        });
        <?php } ?>
       }
</script>