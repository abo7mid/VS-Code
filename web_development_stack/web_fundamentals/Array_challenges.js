
// Always Hungry
// Write a function that is given an array and each time the value is "food" it should console log "yummy". 
// If "food" was not present in the array console log "I'm hungry" once.
function alwaysHungry(arr) {
    // console.log(arr)
    // when to use each of var, let, const 
    var hungry = false
    being_called = 0
    for (var i = 0; i < arr.length; i++) {

        if (arr[i] == 'food') {

            hungry = false
            console.log("yummy")
        }
        else
            hungry = true
    }
    if (hungry)
        console.log("I'm hungry")
    // console.log("done")


}
alwaysHungry([3.14, "food", "pie", true, "food"]);
// // this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"







// High Pass Filter
// Given an array and a value cutoff, return a new array containing only the values larger than cutoff.
// highPass([6, 8, 3, 10, -2, 5, 9], 5);
// we expect back [6, 8, 10, 9]
function highPass(arr, cutoff) {
    var filteredArr = [];
    // your code here
    for (i = 0; i < arr.length; i++) {
        // console.log("loop",i,"arr[",i,"]",arr[i],"> cutoff",cutoff)
        if (arr[i] > cutoff)
            filteredArr.push(arr[i])
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // we expect back [6, 8, 10, 9]








// Better than average
// Given an array of numbers return a count of how many of the numbers are larger than the average. teh average of 10,10,10 is 10*3/3,or (10+10+10)/3
function betterThanAverage(arr) {
    var sum = 0;
    var count = 0
    // calculate the average
    for (i = 0; i < arr.length; i++)// this loop to get the sum of the array item
        sum = sum + arr[i]
    // console.log("average", sum / arr.length) // the average

    for (i = 0; i < arr.length; i++) //this loop to check if an item is greater than average
        if (arr[i] > (sum / arr.length))
            count = count + 1
    // count how many values are greated than the average
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]); //the average 5.5
console.log(result); // we expect back 4









// Array Reverse
// Write a function that will reverse the values an array and return them.
function reverse(arr) {
    // your code here
    new_array = []
    for (i = 0; arr.length > i;) {

        new_array.push(arr.pop())

    }
    arr = new_array
    return arr;
}
var result = reverse(["a", "b", "c", "d", "e"]);
console.log('test',result); // we expect back ["e", "d", "c", "b", "a"]





function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    // your code here
    for (i = 0; i < n; i++) {
        if (fibArr.length == n) {
            break;
        }
        fibArr.push((fibArr[i] + fibArr[i + 1]))
    }

    return fibArr;
}
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]