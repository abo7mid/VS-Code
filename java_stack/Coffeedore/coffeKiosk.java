package Coffeedore;

import java.util.ArrayList;

public class coffeKiosk {

    private ArrayList<Item> menu;
    private ArrayList<Order> orders;

    public coffeKiosk() {
        this.menu = new ArrayList<Item>();
        this.orders = new ArrayList<Order>();
    }

    public void addMenuItem(String name, Double price) {
        Item item1 = new Item(name, price);
        this.menu.add(item1);
        item1.setIndex(menu.indexOf(item1));

    }

    public void displayMenu() {
        for (int i = 0; i < menu.size(); i++) {
            System.out.println(String.format("%s %s -- %s", i, menu.get(i).name, menu.get(i).price));
        }
    }

    public void newOrder() {
        System.out.println("Please enter customer name for new order:");
        String name = System.console().readLine();
        // Your code:
        // Create a new order with the given input string
        // Show the user the menu, so they can choose items to add.
        Order order1 = new Order(name);

        this.orders.add(order1);/////////////////////////
        displayMenu();

        // Prompts the user to enter an item number
        System.out.println("Please enter a menu item index or q to quit:");
        String itemNumber = System.console().readLine();
        // Write a while loop to collect all user's order items
        while (!itemNumber.equals("q")) {

            // Get the item object from the menu, and add the item to the order
            // Ask them to enter a new item index or q again, and take their input
            int i = Integer.parseInt(itemNumber);
            if (i < menu.size()) {

                Item item = menu.get(i);
                order1.addItem(item);
            } else {
                System.out.println("Sorry we do not have it");
            }
            System.out.println("Please enter the index of the coffee you would like to order, or press q to exit");
            itemNumber = System.console().readLine();

        }
        // After you have collected their order, print the order details
        // as the example below. You may use the order's display method.
        order1.display();
        this.orders.add(order1);
    }



}
