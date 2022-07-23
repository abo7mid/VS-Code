package Barista;

public class Item {

    // MEMBER VARIABLES
    private String name;
    private double price;
    private static int instances; // to store how many instances (Items) got created 
    // private int orderNumber = 0;

    
    // CONSTRUCTOR
    //   Takes a name and price as arguments 
    //   and sets them accordingly
    
    public Item(String name,double price){
        
        this.name = name;
        this.price = price;
        instances = instances +1;
    }

    // GETTERS & SETTERS  - for name and price
    public String getName(){
        return name;
    }
    public static int getInstances(){
        return instances;
    }

    public double getPrice(){
        return price;
    }


    public void setName(String name){
        this.name = name;
    }

    public void setPrice(double price){
        this.price = price;
    }

}


