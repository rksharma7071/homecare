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