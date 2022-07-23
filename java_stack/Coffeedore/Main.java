package Coffeedore;

public class Main {
    public static void main(String[] args) {
        coffeKiosk coff = new coffeKiosk();
        coff.addMenuItem("banana", 2.0);
        coff.addMenuItem("Coffee", 1.50);
        coff.addMenuItem("latte", 4.50);
        coff.addMenuItem("capuccino", 3.0);
        coff.addMenuItem("muffin", 4.0);
        coff.newOrder();

    }
}
