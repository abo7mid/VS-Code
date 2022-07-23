package Coffeedore;

import java.util.ArrayList;

public class Order {


    private String name;
    private double total;
    private boolean ready;
    private ArrayList<Item> items;
    
    public Order(){
        items = new ArrayList<Item>();
    }
    public Order(String name){
        this.name = name;
        items = new ArrayList<Item>();
    }


    public void addItem(Item item){
        this.items.add(item);
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

}
