var colors = ['#000000', '#FFFFFF', '#FF0000', '#FF6A00', '#FFD800', '#00FF00', '#0000FF', '#4800FF'];
// colors.length = 8, last is 7
var ccolor = 0;

function refresh() {
  window.location = window.location;
}

function search() {
  var searchItem = document.getElementById("searchInput").value;
  if (searchItem != "") {
    searchItem = "https://www.google.com/search?q=" + searchItem;
    window.location = searchItem;
  }
}

function randomColor() {
  var base16 = "0123456789ABCDEF";
  var hex = "";

  for (var i = 0; i < 6; i++) {
    var r = Math.floor(Math.random() * 16);
    hex += base16[r];
  }

  hex = "#" + hex;

  setColor(hex);
}

function cycleColors() {
  if (ccolor == colors.length - 1) {
    ccolor = 0;
  } else {
    ccolor ++;
  }

  setColor(colors[ccolor]);
}

function setColor(hexColor) {
  var allHeaders = document.querySelectorAll("h1");

  for (var i = 0; i < allHeaders.length; i++) {
    allHeaders[i].style.color = hexColor;
  }

  document.getElementById("currentColor").innerHTML = "Current Hex: " + hexColor;
}
