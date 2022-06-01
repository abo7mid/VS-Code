var btn1 = document.querySelector(".btn1");
btn1.addEventListener("click",btnClicked);

function btnClicked(){
    var count1 = document.querySelector(".count1");
    count1.innerText = parseInt(count1.innerText)+1;
}



var btn2 = document.querySelector(".btn2");
btn2.addEventListener("click",btn2Clicked);

function btn2Clicked(){
    var count2 = document.querySelector(".count2");
    count2.innerText = parseInt(count2.innerText)+1;
}


var btn3 = document.querySelector(".btn3");
btn3.addEventListener("click",btn3Clicked);

function btn3Clicked(){
    var count3 = document.querySelector(".count3");
    count3.innerText = parseInt(count3.innerText)+1;
}
