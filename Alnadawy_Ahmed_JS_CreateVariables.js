
var height = 42;  

var age = 11; 
// we could make the vars to receive the height and age values from the userinput, but it is not stated in the task to do so :)
// actually, I'm not sure what is the function that takes the userinput and store it in a variable :(

//if rider's height is less than 42 inches, he is not allowed to ride
if (height < 42)
{
    console.log("The rider is not tall enough to ride the rollercoaster");
}


//if a rider's age is not over (greater than) 10 years, he is not allowed to ride
if(age < 11)
{
    console.log("The rider is not old enough to ride the rollercoaster");

}

//if the rider's height is equal to or greater than 42 inches, let him ride. and if the rider's age is equal to or greater than 10 years, let him ride

if (height >= 42 && age >= 11)
{
    console.log("Come in please, You're allowed to ride");

}

//I used stackoverflow.com as reference because I'v forgotten how multible conditions work, I'v tried "and" operator first and it turn out to be && :)