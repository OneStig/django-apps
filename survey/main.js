var stars = document.getElementsByClassName("fa-star");

var pubgDiv;
var fortniteDiv;

var checked = false;

function pageTwoLoad() {
  pubgDiv = document.querySelector('#pubgDiv');
  fortniteDiv = document.querySelector('#fortniteDiv');

  pubgDiv.addEventListener('mouseover', function() {
    console.log("pubgHover");

    document.getElementById("labelA").innerText = "Steam's PUBG";
    document.getElementById("labelB").innerText = "Unreal's Fortnite";

    document.getElementById("img1").src = 'pubgLogo.png';
    document.getElementById("img2").src = 'fortniteLogo.png';

    if (checked != false) {
      document.getElementById("pubg").checked = true;
    }
  });

  fortniteDiv.addEventListener('mouseover', function() {
    console.log("fortniteHover");

    document.getElementById("labelB").innerText = "Steam's PUBG";
    document.getElementById("labelA").innerText = "Unreal's Fortnite";

    document.getElementById("img2").src = 'pubgLogo.png';
    document.getElementById("img1").src = 'fortniteLogo.png';

    if (checked != false) {
      document.getElementById("fortnite").checked = true;
    }
  });
}


rating = 0;

for (var i = 0; i < stars.length; i++) {
  stars[i].addEventListener('click', star(i + 1));
}

for (var i = 0; i < 5; i++) {
  var j = i + 1;
  var id = "star" + j;
  console.log(id);
  var cStar = document.getElementById(id);
  cStar.addEventListener('mouseover', hover(cStar));
}

function hover(starID) {
  console.log(starID);
}

function star(n) {
  clearAll();

  rating = n;

  for (var i = 0; i < stars.length; i++) {
    if (i < rating) {
      stars[i].className = 'fa fa-star checked';
    }
  }
}

function clearAll() {
  for (var i = 0; i < stars.length; i++) {
    stars[i].className = 'fa fa-star';
  }
}

function continueSurvey(n) {
  if (n == 1) {
    if (rating < 5) {
      document.getElementById("error").innerHTML = "*ERROR, rating can't be less than 5 stars";
    } else {
      window.location = 'page2.html';
    }
  } else if (n == 2) {
    var f = document.getElementById("pubg").checked;
    var s = document.getElementById("fortnite").checked;

    if (f == false && s == false) {
      document.getElementById("error").innerHTML = "*ERROR, please selected an option.";
    } else {
      window.location = 'page3.html';
    }
  }
}

function checkBox(name) {
  document.getElementById(name).checked = 'true';
  checked = true;
}
