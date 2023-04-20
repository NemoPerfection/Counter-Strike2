function burgerMenuAction() {
    let mobileMenu = document.getElementById("mobile_menu");

    if (mobileMenu.style.display === "none") {
        mobileMenu.style.display = "block";
    } else {
        mobileMenu.style.display = "none";
    }
}