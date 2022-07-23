package Orders_Items;

import java.util.ArrayList;

// import java.util.ArrayList;
public class TestOrders {
    public static void main(String[] args) {
    
        // Menu items

        Item item1 = new Item("mocha",5.5);
        Item item2 = new Item("latte",5.4);
        Item item3 = new Item("drip coffee",2.5);
        // item3.name = "drip coffee";
        // item3.price = 2.5;
        
        Item item4 = new Item("capuccino",4.5);
        // item4.name = "capuccino";
        // item4.price = 4.5;

        // Order order1 = new Order();
        // order1.name = "Cindhuri";
        // order1.items.add(item1);
        // order1.items.add(item2);
        // System.out.println(order1.items.size());

        // for(int i = 0;i<order1.items.size();i++){
        //     System.out.println(order1.items.get(i).name);
        // }


        

        
        // Order variables -- order1, order2 etc.
        Order order1 = new Order();
        order1.name = "Cindhuri";
        
        Order order2 = new Order();
        order2.name = "Jimmy";
        order2.items.add(item1);
        order2.total = order2.total + item1.price;
        
        Order order3 = new Order();
        order3.name = "Noah";
        order3.items.add(item4);


        Order order4 = new Order();
        order4.name = "Sam";
        order4.items.add(item2);
        order4.total = order4.total + item2.price;

        //Cindhuri’s order is now ready. Update her status.

        //based on the assignment lists, Cindhuri (order1) has not added any item (coffee product) yet.
        //How I supposed to make an order and say to the customer your order is ready while the customer has not yet chosen the item???
        //Am I miss understood this question?


        order4.items.add(item2);
        order4.items.add(item2);
        order4.total = order4.total + item2.price*2;

        //Jimmy order now is ready
        order2.ready = true;







        // Application Simulations
        // Use this example code to test various orders' updates
        System.out.printf("Order1: %s\n", order1); //print package name + class name + object location address 
        System.out.printf("Total: %s\n", order1.total); // since it is not yet inititalized, java will assign 0.0 to it.   
        System.out.printf("item1 name: %s\n", item1.name);
        System.out.printf("item1 price: %s\n", item1.price);
        System.out.printf("Name: %s\n", order2.name);
        System.out.printf("Total: %s\n", order2.total);
        System.out.printf("Ready: %s\n", order2.ready);
        System.out.printf("Items: %s\n", order2.items);
    }
}