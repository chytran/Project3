/*==================== SHOW MENU =============================*/
const navMenu = document.querySelector(".nav__menu");
const navToggle = document.getElementById("nav-toggle");
const navClose = document.getElementById("nav-close");


/*======== Menu Show ======*/
if(navToggle) {
    navToggle.addEventListener("click", () => {
        // alert("hi");
        navMenu.classList.add("show-menu");
    })
}

/*========== Menu Hidden ===========*/
/* Validate if constant exists */
if(navClose){
    navClose.addEventListener("click", () => {
        // alert("hi");
        navMenu.classList.remove("show-menu");
    })
}


/*========================== CLOUDS =========================*/
const cloud = document.querySelector(".clouds");
const exploreBtn = document.querySelector("#searching");

exploreBtn.addEventListener("click", function() {
    setTimeout(function() {
        alert("How's it going");
        console.log("hi");
    }, 4000);
});