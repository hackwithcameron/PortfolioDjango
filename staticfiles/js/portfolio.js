
function animation(x) {
    let navList = document.getElementById('navbarInfo');
    if (navList.classList.contains('show')){
        x.classList.remove("change");
    } else if (!navList.classList.contains('show')) {
        x.classList.add("change");
    }
}

//  -------Removes change class from menu hamburger if main document is clicked--------
document.getElementById('main').addEventListener('click', function(){
    let nav = document.getElementById('nav-button');
    nav.classList.remove('change');
});

//  -------Projects Modals--------
let modal1 = document.getElementById("modal1");
let modal2 = document.getElementById("modal2");
let modal3 = document.getElementById("modal3");
let navBar = document.getElementById("navBar")

let cards = document.getElementsByClassName('projectCard');


function projectCards(event){
    for (let i = 0; i < cards.length; i++){
        cards[i].classList.add('move');
    }
    navBar.style.display = "none";
    if (event.target.id === 'project1'){
        modal1.style.display = "block";
    }
    if (event.target.id === 'project2'){
        modal2.style.display = "block";
    }
    if (event.target.id === 'project3'){
        modal3.style.display = "block";
    }
}

function close1(){
    for (let i = 0; i < cards.length; i++){
        cards[i].classList.remove('move');
    }
    modal1.style.display = "none";
    modal2.style.display = "none";
    modal3.style.display = "none";
    navBar.style.display = "flex";

}

let img = document.getElementById('');
let text = document.getElementById('');

//  -------Scroll Reveal--------

let config = {
    duration: 2000,
    distance: '50px',
    viewFactor: 0.3
}

const config2 = {
    duration: 2000,
    distance: '50px',
    viewFactor: 0.3,
    origin: 'top'
};


window.sr = ScrollReveal(config);
sr.reveal('.development');
sr.reveal('.projectCard');
sr.reveal('#gradient2');


window.sr = ScrollReveal(config2);
sr.reveal('#gradient');


//  -------NavBar Adjustment--------
let page = window.location.pathname;                // Gets url of current page
let navContainer = document.getElementById("nav-container");

if(page === '/' || page === '/#aboutLabel/'){           // Checks to see if url is homepage
    navContainer.style.height = 0;              // Sets navbar container height to 0
}




