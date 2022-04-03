var map = L.map('bottle-map').setView([53.450140, -7.266155], 6);

L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
    minZoom: 6,
    maxZoom: 8,
    ext: 'png',
    subdomains: 'abcd'
}).addTo(map);
map.setZoom(7);

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


function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );

    data = JSON.parse(xmlHttp.responseText)
    return data;
};

function addMarker(lat,long,value,colour) {
    var circle = L.circle([lat, long], {
        color: colour,
        radius: value*4
    }).addTo(map);
};

var data = httpGet('http://localhost:5555/show/raw')
console.log(data);
for (let i = 0; i < data.length; i++) {
    if (data[i][2] !== null) {
        addMarker(data[i][3],data[i][2],data[i][4],data[i][5]);
      };
  };


