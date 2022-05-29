
// Print odds 1-20
for (var i = 0; i<=20;i+=1){
    if(i%2!=0){
        console.log("odd number :"+i)
    }
}
console.log("*************")

// Decreasing Multiples of 3
for(var i = 100;i>=0;i--){
    if(i%3==0){
        console.log(i)
    }
}
console.log("*************")

// Print the sequence
for(var i = 4;i>=-3.5;i=i-1.5){
    
        console.log(i)
}
console.log("*************")

//Sigma
var sum = 0;
for(var i = 1;i<=100;i++){
    sum  += i;
    console.log(sum);
}
console.log("*************")


//Factorial
var product = 1;
for(i=1;i<=12;i+=1){

    product = product * i;
    console.log(product)
}