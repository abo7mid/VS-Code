


function darkMode(element){

    // element.style.backgroundColor = "#222222";
    // element.style.color = "#ffffff"
    // element.style.width = "150px";
    // element.style.height = "50px"
    // element.innerText = "Switch to light mode"
    // console.log(element.classList.contains("light-mode"));
    if (element.classList.contains("light-mode")){
        element.innerText = "Switch to light mode";
        element.classList.add("dark-mode");  //for this class to be applied we need to remove any other classes
        element.classList.remove("light-mode");

    }
    else{
        element.innerText = "Switch to dark mode";
        element.classList.add("light-mode"); 
        element.classList.remove("dark-mode")
    }

}