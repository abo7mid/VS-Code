package Coffeedore;

public class Item {
    String name;
    double price;
    int index;
    

    public Item(String name,double price){
        
        this.name = name;
        this.price = price;

    }

    // GETTERS & SETTERS  - for name and price
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public int getIndex(){
        return this.index;
    }
    public void setIndex(int index){
        this.index = index;
    }
    public double getPrice(){
        
        return price;
    }
    public void setPrice(double price){
        this.price = price;
    }
}
