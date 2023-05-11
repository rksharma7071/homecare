var hideTimer;

function showDiv() {
    clearTimeout(hideTimer);
    document.getElementById("products-dropdown").style.display = "block";
}

function hideDiv() {
    hideTimer = setTimeout(function() {
        document.getElementById("products-dropdown").style.display = "none";
    }, 100); // 2 seconds
}

function startHideTimer() {
    hideTimer = setTimeout(function() {
        document.getElementById("products-dropdown").style.display = "none";
    }, 100); // 2 seconds
}

function showDiv1() {
    clearTimeout(hideTimer1);
    document.getElementById("products-dropdown1").style.display = "block";
}

function hideDiv1() {
    hideTimer1 = setTimeout(function() {
        document.getElementById("products-dropdown1").style.display = "none";
    }, 100); // 2 seconds
}

function startHideTimer1() {
    hideTimer1 = setTimeout(function() {
        document.getElementById("products-dropdown1").style.display = "none";
    }, 100); // 2 seconds
}