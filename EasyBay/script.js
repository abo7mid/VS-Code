var btn1 = document.querySelector(".btn1");
btn1.addEventListener("click",Hide);


var cookies = document.querySelector(".cookies");


function Hide(){
    cookies.remove();
}





var hover1 = document.getElementById("replace");

hover1.addEventListener("mouseover",change);
hover1.addEventListener("mouseout",back);

function change(){
    document.getElementById("replace").src  = "assets/succulents-2.jpg";
}


function back(){
    document.getElementById("replace").src  = "assets/succulents-1.jpg";

}








// // show cart itmes
var cart = document.querySelector(".cart");
cart.addEventListener("click",showcartlist);


function showcartlist(){
    alert("Your cart is empty");
}
