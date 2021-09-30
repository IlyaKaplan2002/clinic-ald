function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className.includes("topnav") && !x.className.includes("responsive")) {
    x.className += " responsive";
  } else {
    x.className = "mobile-menu topnav nav-list-adaptive";
  }
}
