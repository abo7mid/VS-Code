var max = document.querySelectorAll("#max");
var min = document.querySelectorAll("#min");

var C = document.querySelector('[value="C"]');
var F = document.querySelector('[value="F"]');

C.addEventListener("click",selectCelsius);
F.addEventListener("click",selectFahrenheit);

function selectCelsius(){
    console.log(C);
    for(var i = 0; i<max.length;i++){

        max[i].innerText = 0;
        max[i].innerText = 10;

    }

}


function selectFahrenheit(){
    console.log(F);
    for(var i = 0; i<max.length;i++){

        max[i].innerText = 10;
        min[i].innerText = 0
    }

}




