public class CafeJava {
   public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = " your total is $";
        String weOweYou = ", we owe you ";
	String youOweUs = ", you owe us ";

        // Menu variables (add yours below)
        double mochaPrice = 6.5;
        double dripCoffeePrice = 5.5;
        double lattePrice = 4.5;
        double cappuccinoPrice = 3.5;	
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri ";
        String customer2 = "Sam ";
        String customer3 = "Jimmy ";
        String customer4 = "Noah ";

        // Order completions (add yours below)
        boolean isReadyOrder1 = true;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = true;
        boolean isReadyOrder4 = true;
    
    
    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        System.out.println(generalGreeting + customer1); // Displays "Welcome to Cafe Java, Cindhuri"
    	// ** Your customer interaction print statements will go here ** //
	
        //System.out.println(customer1 + " ordered a coffee.");
        if (isReadyOrder1 == false){ //equivlant to if (!isReadyOrder1){  	
              System.out.println(customer1 + pendingMessage);
	      System.out.println("==========================");
	}	
        else{
	     
              System.out.println(customer1 + readyMessage+displayTotalMessage+dripCoffeePrice);
	      System.out.println("==========================");
	}










        System.out.println(generalGreeting + customer4);
	
        if (isReadyOrder4 == false){ //equivlant to if (!isReadyOrder1){  	
              System.out.println(customer4 + pendingMessage);
	      System.out.println("==========================");
	      
	}	
        else{
	     
              System.out.println(customer4 + readyMessage);
	      System.out.println(displayTotalMessage+cappuccinoPrice);
	      System.out.println("==========================");
	}













	System.out.println(generalGreeting + customer2); 
	
        if (isReadyOrder2 == false){ //equivlant to if (!isReadyOrder1){  	
              System.out.println(customer2 + pendingMessage);
	      System.out.println("==========================");
	}	
        else{
	     
              System.out.println(customer2 + readyMessage);
	      System.out.println(displayTotalMessage+(lattePrice*2));
	      System.out.println("==========================");
	}	

       











	System.out.println(generalGreeting + customer3); 
	
        if (isReadyOrder3 == false){ //equivlant to if (!isReadyOrder1){  	
              System.out.println(customer3 + pendingMessage);
	      System.out.println("==========================");
	}	
        else{
	     
	     
              System.out.println(customer3 + readyMessage);
	      System.out.println(displayTotalMessage + dripCoffeePrice);
	      
	     
              System.out.println("says "+customer3 + ", This is not what I ordered bro!!");
              double newPrice = dripCoffeePrice - lattePrice;
              if(newPrice > 0) {
	             System.out.println("Sorry mr "+customer3+ "about that and this a free pancake " + weOweYou + newPrice);
	             System.out.println("==========================");
              }
              
              else{
                     System.out.println("Sorry mr "+customer3+ "about that and this a free pancake " + youOweUs + newPrice);
	             System.out.println("==========================");
	       
      	      }	      
	}


   }
}

