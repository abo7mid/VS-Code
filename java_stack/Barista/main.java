package Barista;

public class main {

    public static void main(String[] args){

        Item coffee = new Item("Coffee", 10+10*0.15); //10 the price 10*0.15 is the vat
        Item tea = new Item("tea", 2+3*0.15);
        Item water = new Item("water", 1);
        

        
        
        Order order1 = new Order();
        Order order2 = new Order();
        Order order3 = new Order("Muhmmed");
        Order order4 = new Order("Ahmed");
        Order order5 = new Order("Awadh");
        
        order1.addItem(coffee);
        order1.addItem(water);
        order1.setReady(true);
        System.out.println(order1.getStatusMessage());
        order1.display();
        order1.close();
        
        
        order2.addItem(tea);
        // order2.setReady(true);
        System.out.println(order2.getStatusMessage());
        order2.display();
        order2.close();
        

        
        order3.addItem(tea);
        order3.addItem(water);
        System.out.println(order3.getStatusMessage());
        // System.out.println(order3.getOrderTotal());
        order3.display();
        order3.close();

        order4.addItem(tea);
        order4.addItem(coffee);
        System.out.println(order4.getStatusMessage());
        // System.out.println(order4.getOrderTotal());
        order4.display();
        order4.close();

        order5.addItem(water);
        order5.addItem(coffee);
        System.out.println(order5.getStatusMessage());
        // System.out.println(order5.getOrderTotal());
        order5.display();
        order5.close();
        

        // System.out.println(order1.getStatusMessage());
        // order1.display();
        // order2.display();
    }

}
