$(document).ready(function(){
	// alert("Hi Vu")
	$.getJSON("http://ip-api.com/json/?callback=?", function(data) {
    var table_body = "";
    // console.log("Hi", data)
    table_body += data.city
    var longing = data.lon
    // console.log(longing)
    var latty = data.lat
    // console.log(latty)
    $("#GeoResults").html(table_body);

});
})