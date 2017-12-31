
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
