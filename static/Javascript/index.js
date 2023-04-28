function onMenuClick() {
    var navbar = document.getElementById('navigation-bar');
    var responsive_class_name = 'responsive'
    
    navbar.classList.toggle(responsive_class_name)

}

const searchInput = document.getElementById("search-input");
const searchButton = document.getElementById("search-button");
const recipeCards = document.getElementsByClassName("recipe-card");

searchButton.addEventListener("click", () => {
  const searchText = searchInput.value.toLowerCase();
  
  for (let i = 0; i < recipeCards.length; i++) {
    const recipeName = recipeCards[i].getElementsByClassName("recipe-name")[0].textContent.toLowerCase();
    const receipeCuisines = recipeCards[i].getElementsByClassName("recipe-cuisine")[0].textContent.toLowerCase();    
    if (recipeName.includes(searchText) || receipeCuisines.includes(searchText)) {
      recipeCards[i].style.display = "block";
    } else {
      recipeCards[i].style.display = "none";
    }
  }
});



/* Navbar dropdown*/

// Get the dropdown container
var dropdown = document.getElementsByClassName("dropdown");

// Loop through all dropdown containers and add a click event listener
for (var i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    // Toggle the dropdown menu visibility
    this.classList.toggle("active");
    var dropdownContent = this.getElementsByClassName("dropdown-content")[0];
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

// Close the dropdown menu if the user clicks outside of it
window.addEventListener("click", function(event) {
  if (!event.target.matches(".dropbtn")) {
    var dropdowns = document.getElementsByClassName("dropdown");
    for (var i = 0; i < dropdowns.length; i++) {
      var dropdownContent = dropdowns[i].getElementsByClassName("dropdown-content")[0];
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
        dropdowns[i].classList.remove("active");
      }
    }
  }
});
