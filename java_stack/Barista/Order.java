package Barista;

import java.util.ArrayList;

public class Order {


    private String name;
    private boolean ready;
    private ArrayList<Item> items;
    // private static int orderNumber = 0;

    // CONSTRUCTOR
    // No arguments, sets name to "Guest", initializes items as an empty list.

    public Order() {
        this.name = "Guest";
        this.items = new ArrayList<Item>();
        // orderNumber = orderNumber +1;
    }
    
    // OVERLOADED CONSTRUCTOR
    // Takes a name as an argument, sets name to this custom name.
    // Initializes items as an empty list.
    
    public Order(String name) {
        this.name = name;
        this.items = new ArrayList<Item>();
        // orderNumber = orderNumber +1;
    }



    // ORDER METHODS

    // Most of your code will go here,
    // so implement the getters and setters first!

    public void addItem(Item item){
        this.items.add(item);
        // System.out.println("------------receipt-----------");
        // System.out.println("-----------------------");
        // System.out.println(String.format("------- Order no %s ------",getOrderNumber()));
        // System.out.println(String.format("------- Type %s ------",item.getName()));
        // System.out.println(String.format("-------  Price %s ------",item.getPrice()));
        // System.out.println(String.format("-------  Owner %s ------",this.name));
        // System.out.println("-----------------------\n");

    }


    public String getStatusMessage(){
        // System.out.println("------- Status ------");

        if (this.ready){

            return "Your order is ready.";
        }
        return "Thank you for waiting. Your order will be ready soon.";
    }


    public double getOrderTotal(){
        // System.out.println("------- Total ------");
        double Total = 0 ;
        for(int price = 0;price < items.size();price++){
            Total = Total + items.get(price).getPrice();
        }
        return Total;
    }


    public void display(){
        
        // System.out.println("------- Display Order Info ------");
        System.out.println("Customer Name: " + this.name);
        for(int item = 0;item<items.size();item++){
            System.out.println(String.format("%s - %s",items.get(item).getName(),items.get(item).getPrice()));
            
        }
        System.out.println("Total: " + getOrderTotal());

    }

    public void close(){
        System.out.print("--------------------\n");
    }

    // GETTERS & SETTERS
    // public int getOrderNumber(){
    //     return this.orderNumber;
    // }
    public boolean isReady(){
        // System.out.println("------- isReady ------");

        return this.ready;
    }

    public void setReady(boolean ready){
        // System.out.println("------- setReady ------");

        this.ready = ready;
    }

}
