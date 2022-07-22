package Cafe_Business_Logic;

import java.util.ArrayList;

public class TestCafe {
    public static void main(String[] args) {
        CafeUtil cafe = new CafeUtil();
        System.out.println("\n----- Streak Goal Test -----");
        System.out.printf("Purchases needed by week 10: %s \n\n", cafe.getStreakGoal(11));

        System.out.println("----- Order Total Test-----");
        double prices[] = { 5.2, 2.5, 4.9, 5.7};
        System.out.printf("Order total: %s \n\n", cafe.getOrderTotal(prices));






        System.out.println("----- Display Menu Test-----");
        ArrayList<String> menu = new ArrayList<String>();
        menu.add("drip coffee");
        menu.add("cappuccino");
        menu.add("latte");
        menu.add("mocha");


        ArrayList<Double> prices_ = new ArrayList<Double>();
        prices_.add(5.1);
        prices_.add(5.2);
        prices_.add(5.3);
        prices_.add(5.4);    
        
        cafe.displayMenu(menu,prices_);

        System.out.println("\n----- Add Customer Test-----");
        ArrayList<String> customers = new ArrayList<String>();
        for(int i = 0;i<4;i++){

        cafe.addCustomer(customers);
        }

        System.out.println("\n----- Ninja Bonuses-----");
        cafe.printPriceChart("coffee", 22.5, 3);
    }
}
