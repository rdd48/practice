mapboxgl.accessToken = mapToken;

campgroundObj = JSON.parse(campgroundData)

const map = new mapboxgl.Map({
    container: 'map', // container ID
    style: 'mapbox://styles/mapbox/streets-v11', // style URL
    center: campgroundObj.geometry.coordinates, // starting position [lng, lat]
    zoom: 9 // starting zoom
});

const nav = new mapboxgl.NavigationControl();
map.addControl(nav, 'top-left');

const marker = new mapboxgl.Marker()
    .setLngLat(campgroundObj.geometry.coordinates)
    .setPopup(
        new mapboxgl.Popup({ offset: 25 })
            .setHTML(
                `<h3>${campgroundObj.title}</h3><p>${campgroundObj.location}</p>`
            )
    )
    .addTo(map);