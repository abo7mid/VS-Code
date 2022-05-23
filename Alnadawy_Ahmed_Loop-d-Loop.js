
//strat point;  end point 


var speed = 5.5;
for(var miles = 2;  miles<=6;miles+=2)
{//I started the loop at value 2, because first loop will not increament
  

//How do we know we need a loop here?
//each 2 miles a device will pops out a candy
//that means in the 6 miles the device will pop out 3 candies
//three times (repetition), so we need the loop


//When should the loop stop?
//before the runner go beyond 6 miles 

//How will it know to stop?
//When the loop condition is false)

//What's the incrementing for each iteration of the loop?
// the increaminting value is 2


//What variables do we need?
//one variable, counter



if (miles == 6)
    console.log("no more candy stop running")
    else
    {
        if (speed == 5.5)
        {
            console.log(miles+" miles travelled")
            console.log("A candy pops out")
        }
    

    }



}