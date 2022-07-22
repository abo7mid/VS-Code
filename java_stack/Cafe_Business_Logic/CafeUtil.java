package Cafe_Business_Logic;

import java.util.ArrayList;


public class CafeUtil{
    
        int getStreakGoal(){
            int sums = 0;
            for(int i = 0;i<=10;i++){
                sums = sums + i;
            }
            return sums;
        }

        int getStreakGoal(int numWeeks){
            int sums = 0;
            for(int i = 0;i<=numWeeks;i++){
            sums = sums + i;
            }
            return sums;
        }

        double getOrderTotal(double[] prices){
            double total = 0;
            for(int i = 0;i<prices.length;i++){
            total = total + prices[i];
                
            }
            return total;
        }

        void displayMenu(ArrayList<String> menuItems){
            // for(String menuitem: menuItems){
            //     System.out.println(menuitem);
            // }
            for(int i = 0;i<menuItems.size();i++ ){
                System.out.println(String.format("%s %s",i, menuItems.get(i)));
            }
            
        }


        boolean displayMenu(ArrayList<String> menuItems, ArrayList<Double> prices){
            if(menuItems.size() != prices.size()){
                return false;

            }
            for(int i = 0;i<menuItems.size();i++){

                System.out.println(String.format("%s %s -- $%s", i+1,menuItems.get(i),prices.get(i)));
            }

            return true;
        }

        void addCustomer(ArrayList<String> customers){
            System.out.println("Please enter your name:");
            String name = System.console().readLine();
            System.out.println("Hello, "+ name);
            System.out.println(String.format("There are %s people in front of you ",customers.size()));
            customers.add(name);
            System.out.println(customers);
            
            
        }

        void printPriceChart(String product, double price,int maxQuantity){
            System.out.println(product);
            for(int quantity =1;quantity<=maxQuantity;quantity++){
                System.out.println(String.format("%s - $%s",quantity,price*quantity));
                
            }
            
        }

    

}