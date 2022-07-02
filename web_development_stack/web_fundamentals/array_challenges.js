//Array Challenges
// Always Hungry 




// High Pass Filter



// Better than average



//all the above challenges are done on an other system but not pushed to github yet




// Array Reverse
// Write a function that will reverse the values an array and return them.

function reverse(arr) {
    // your code here
    new_array = []
    for(i = 0;arr.length>i;){

        new_array.push(arr.pop())
        
    }
    arr = new_array
    return arr;
}
   
// var result = reverse(["a", "b", "c", "d", "e"]);
// console.log(result); // we expect back ["e", "d", "c", "b", "a"]





function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    // your code here
    for(i=0;i<n;i++){
        if(fibArr.length == n){
            break;
        }
        fibArr.push((fibArr[i]+fibArr[i+1]))
    }

    return fibArr;
}
   
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
