function initMap () {

    var myLatlng = new google.maps.LatLng(51.794212, 21.095994);
    var warLatlng = new google.maps.LatLng(52.155644, 21.034461);
    var lubLatlng = new google.maps.LatLng(51.215681, 22.626974);
    var lodLatlng = new google.maps.LatLng(51.762849, 19.437676);

var mapOptions = {
    zoom: 7,
    center: myLatlng,
    scrollwheel: false,
    zoomControl: true,
    mapTypeControl: false,
    scaleControl: true,
    streetViewControl: false,
    rotateControl: false,
    fullscreenControl: false
};

var map = new google.maps.Map(
	document.getElementById('map'),
  mapOptions
);

var markerWar = new google.maps.Marker({
    position: warLatlng,
    map: map
});

var markerLub = new google.maps.Marker({
    position: lubLatlng,
    map: map
});

var markerLod = new google.maps.Marker({
    position: lodLatlng,
    map: map
});

// okienko dla biura w Warszawie

var infowindowWar = new google.maps.InfoWindow({
    content: '<strong>GIAP sp. z o.o.</strong><br>\
		Aleja Komisji Edukacji Narodowej 85/87<br>02-777 Warszawa'
});

markerWar.addListener('click', function() {
    infowindowWar.open(map, markerWar);
});

// okienko dla biura w Lublinie

var infowindowLub = new google.maps.InfoWindow({
    content: '<strong>GIAP sp. z o.o.</strong><br>\
		Droga Męczenników Majdanka 181<br>20-325 Lublin'
});

markerLub.addListener('click', function() {
    infowindowLub.open(map, markerLub);
});

// okienko dla biura w Łodzi

var infowindowLod = new google.maps.InfoWindow({
    content: '<strong>GIAP sp. z o.o.</strong><br>\
    Łąkowa 3/5<br>90-562 Łódź'
});

markerLod.addListener('click', function() {
    infowindowLod.open(map, markerLod);
});

infowindowsa.open(map, markerLub);

}