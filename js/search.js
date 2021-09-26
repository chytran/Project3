/*==================== SHOW MENU =============================*/
const navMenu2 = document.querySelector(".nav__menu2");
const navToggle2 = document.getElementById("nav-toggle2");
const navClose2 = document.getElementById("nav-close2");


/*======== Menu Show ======*/
if(navToggle2) {
    navToggle2.addEventListener("click", () => {
        // alert("hi");
        navMenu2.classList.add("show-menu2");
    })
}

/*========== Menu Hidden ===========*/
/* Validate if constant exists */
if(navClose2){
    navClose2.addEventListener("click", () => {
        // alert("hi");
        navMenu2.classList.remove("show-menu2");
    })
}
