
console.log("#1")
console.log("")

var arr1 = [8,6,7,5,3,0,9];
for( var i = 0; i<arr1.length;i++ )
{
    console.log(arr1[i])
}
console.log("")
console.log("")



console.log("#2")
console.log("")

var arr2 = [4, 7, 13, 13, 19, 37, -2];

var sum = 0;

for (var i = 6;i>=0;i=i-1)
{
    sum = sum + arr2[i];
    console.log("index :"+arr2[i]);
    console.log("sum "+sum);
}
console.log("")
console.log("")


console.log("#3")
console.log("")

var arr3 = [6, 2, 12, 14, -24, 5, 0];

for (var i = arr3.length-1;0<=i;i-=1)
{
    if(arr3[i] > 5)
    console.log(arr3[i])

    else
    console.log("No dice.")

}