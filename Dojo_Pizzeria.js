// function pizzaOven(crustType, sauseType, chesse, toppings) {
//     var pizza = {}

//     pizza.crustType = crustType;
//     pizza.sauseType = sauseType;
//     pizza.chesse = chesse;
//     pizza.toppings = toppings;


//     return pizza;
// }

// var p1 = pizzaOven("deep dish","traditional",["mozzarella"],["pepperoni","sausage"]);
// var p2 = pizzaOven("hand tossed","marinara",["mozzarella","feta"],["mushrooms","olives","onions"]);
// var p3 = pizzaOven("Diavola","Tomato","Mozzarella",["Hot Italian salami", "Hot chili peppers"]);
// var p4 = pizzaOven("Margherita","San Marzano tomatoes", "mozzarella", ["fresh basil", "salt","extra-virgin olive oil"]);


// console.log(p1);







function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
console.log(pizza1);

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(pizza2);

var crustTypes = [
    "deep dish",
    "hand tossed",
    "thin and crispy",
    "cauliflower",
    "gluten free",
    "hawaiian bread"
];

var sauceTypes = [
    "traditional",
    "marinara",
    "bbq",
    "white sauce",
    "nacho cheese",
    "tikka masala"
];

var cheeses = [
    "mozzarella",
    "cheddar",
    "feta",
    "swiss cheese",
    "blue cheese",
    "goat cheese",
    "provolone",
    "parmesan",
    "vegan cheese"
];

var toppings = [
    "pepperoni",
    "sausage",
    "chicken",
    "corn",
    "olives",
    "bell peppers",
    "onions",
    "mushrooms",
    "anchovies"
];

function randomRange(max, min) {
    return Math.floor(Math.random() * max - min) + min;
}

function randomPick(arr) {
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}

function randomPizza() {
    var pizza = {};
    pizza.crustType = randomPick(crustTypes);
    pizza.sauceType = randomPick(sauceTypes);
    pizza.cheeses = [];
    pizza.toppings = [];
    for(var i=0; i<randomRange(5, 1); i++) {
        pizza.cheeses.push(randomPick(cheeses));
    }
    for(var i=0; i<randomRange(4, 0); i++) {
        pizza.toppings.push(randomPick(toppings));
    }
    return pizza;
}

console.log(randomPizza());



// Math.floor(0.60) returns 0    rounds a number DOWNWARDS to the nearest integer

// for(i = 10;i>0;i--)
// {
//     var rand = Math.random() // returns a value between 0 and 1   always 0.some 17 floating points  ex 0.5741956958081573

//     nearestInt = Math.floor(rand * 10)
//     console.log(rand +" * 10 ="+ nearestInt)
// }
// console.log("loop ends")