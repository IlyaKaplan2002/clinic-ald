function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className.includes("topnav") && !x.className.includes("responsive")) {
        x.className += " responsive";
    } else {
        x.className = "topnav nav-list-adaptive";
    }
}
