function navOnOff() {
    var x = document.getElementById("nav");
    if (x.className === "nav") {
        x.className += " responsive";
    } else {
        x.className = "nav";
    }
}

(function () {
    var nav = document.getElementById('nav'),
    anchor = nav.getElementsByTagName('a'),
    current = window.location.pathname;
    currentAfter = current.split('/');
    for (var i = 0; i < anchor.length; i++) {
        anchorSplit = anchor[i].pathname.split('/');
        if(anchorSplit[1] == currentAfter[1]){
            anchor[i].className = "active";
            break;
        }
    }


    
})();

