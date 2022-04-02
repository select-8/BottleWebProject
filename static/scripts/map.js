var map = L.map('bottle-map').setView([53.450140, -7.266155], 6);

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery � <a href="https://www.mapbox.com/">Mapbox</a>',
    minZoom: 0,
    maxZoom: 20,
    ext: 'png',
    subdomains: 'abcd'
}).addTo(map);
map.on('click', function (e) {

    var data = JSON.stringify({ 'data': { 'long': e.latlng.lng, 'lat': e.latlng.lat } });
    console.log(data);
    let url = '/mapdata'
    let xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(data);

});
