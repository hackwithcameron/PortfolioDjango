
function animation(x) {
    var navList = document.getElementById('navbarInfo');
    if (navList.classList.contains('show')){
        x.classList.remove("change");
    } else if (!navList.classList.contains('show')) {
        x.classList.add("change");
    }
};

//  -------Removes change class from menu hamburger if main document is clicked--------
document.getElementById('main').addEventListener('click', function(){
    var nav = document.getElementById('nav-button');
    nav.classList.remove('change');
});

//  -------Projects Modals--------
var modal1 = document.getElementById("modal1");


function projectCards(event){
    if (event.target.id == 'project1'){
        modal1.style.display = "block";
    }
    if (event.target.id == 'project2'){
        modal2.style.display = "block";
    }
    if (event.target.id == 'project3'){
        modal3.style.display = "block";
    }
};

function close1(){
    modal1.style.display = "none";
    modal2.style.display = "none";
    modal3.style.display = "none";
};


//  -------Scroll Reveal--------

var config = {
    duration: 2000,
    distance: '50px',
    viewFactor: 0.3
}

var config2 = {
    duration: 2000,
    distance: '50px',
    viewFactor: 0.3,
    origin: 'top'
}


window.sr = ScrollReveal(config);
sr.reveal('.development');
sr.reveal('#gradient2');


window.sr = ScrollReveal(config2);
sr.reveal('#gradient');



