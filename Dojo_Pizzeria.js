function pizzaOven(crustType, sauseType, chesse, toppings) {
    var pizza = {}

    pizza.crustType = crustType;
    pizza.sauseType = sauseType;
    pizza.chesse = chesse;
    pizza.toppings = toppings;


    return pizza;
}

var p1 = pizzaOven("deep dish","traditional",["mozzarella"],["pepperoni","sausage"]);
var p2 = pizzaOven("hand tossed","marinara",["mozzarella","feta"],["mushrooms","olives","onions"]);
var p3 = pizzaOven("Diavola","Tomato","Mozzarella",["Hot Italian salami", "Hot chili peppers"]);
var p4 = pizzaOven("Margherita","San Marzano tomatoes", "mozzarella", ["fresh basil", "salt","extra-virgin olive oil"]);


console.log(p1);

