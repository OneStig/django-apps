var stars = document.getElementsByClassName("fa-star");

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
    }
  }
}
