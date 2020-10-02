var $ = function(id) { return document.getElementById(id); }

var hostsUp = 5;//hardcoding for testing
var hostsDown = 0;
var ipAddr;

var bannerStats = function(){
    $('up').innerHTML = "Hosts up:" + hostsUp;

}


window.onload = function() {
//generates banner info
    bannerStats();

}