// avaScript for Sidebar & Dropdown

function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
}
function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
}
function toggleDropdown() {
    var x = document.getElementById("supportDropdown");
    if (x.classList.contains("w3-show")) {
        x.classList.remove("w3-show");
    } else {
        x.classList.add("w3-show");
    }
}



// Search POPUP Toggle 

function togglePopup() {
    var popup = document.getElementById('popup');
    popup.style.display = (popup.style.display === 'block') ? 'none' : 'block';
}



// Our Products 
let currentSlide = 0;

function moveSlide(step) {
    const slides = document.querySelectorAll(".slider .w3-card-4");
    const totalSlides = slides.length;
    const slider = document.querySelector(".slider");

    currentSlide += step;


    if (currentSlide < 0) {
        currentSlide = totalSlides - 1;
    } 
   
    else if (currentSlide >= totalSlides) {
        currentSlide = 0;
    }

    
    const newTransformValue = -currentSlide * 100 + "%";
    slider.style.transform = `translateX(${newTransformValue})`;
}