function navOnOff() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

(function () {
    var nav = document.getElementById('myTopnav'),
    anchor = nav.getElementsByTagName('a'),
    current = window.location;
    for (var i = 0; i < anchor.length; i++) {
        if(anchor[i].href == current) {
            anchor[i].className = "active";
        }
    }
    
})();