let map;

function initMap() {
 const  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
   map.addListener('click', function () {
       console.log(map.position.latLng);
   })
}

window.initMap = initMap;