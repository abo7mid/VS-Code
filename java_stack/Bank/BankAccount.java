package Bank;


public class BankAccount {
    

    private double checkingBalance;
    private double savingsBalance;
    private static int numberOfAccounts;
    private static Double totalAmountOfMoney;
    private long accountNumber ;
    // private static String OUT_OF_OPTIONS = "0001";
    // private static String INSUFFICIENT_MONEY = "0002";
    // private static String OUT_OF_SERVICE = "0003";
    // private static String OUT_OF_MONEY = "0004";

    public BankAccount(){
        numberOfAccounts = numberOfAccounts + 1;
        this.accountNumber = genUserAccountNumber();
    }


    public double getCheckingBalance(){
        return checkingBalance;
    }
    public double getSavingBalance(){
        return checkingBalance;
    }

    public void deposite(){
        System.out.println("Which account do you want to deposite the money to?");
        System.out.println("1) Savings account\n2) Checking account");
        String value  = System.console().readLine();
        int account =  Integer.parseInt(value);
        if(account == 1 || account == 2)
        { // extra code needed for handling unexpected inputs such as letters since the user can insert letters
            
        System.out.println("insert the amount of money that you want to deposite :");
        String amount  = System.console().readLine();
        // String s = String.valueOf(account);
        if(account == 1){
            System.out.println("You've chosen Savings account");
            this.savingsBalance = Double.parseDouble(amount);
            System.out.println("Money has been deposited Successfuly to account "+value);
            System.out.println("Savings account balance "+this.savingsBalance);
        }
        
        else if(account == 2){
            
            System.out.println("You've chosen Checking account");
            this.checkingBalance = Double.parseDouble(amount);
            System.out.println("Money has been deposited Successfuly to account "+value);
            System.out.println("Checking account balance "+this.checkingBalance);
        }

        else{

            System.out.println("No such option found, try again please");
        }
    }
    else{

        System.out.println("No such option found, try again please ");
    }




    }

    public void withdraw(){
        System.out.println("Which account do you want to withdraw the money from?");
        System.out.println("1) Savings account\n2) Checking account");
        String value  = System.console().readLine();
        int account =  Integer.parseInt(value);
        if(account == 1 || account == 2){ // extra code needed for handling unexpected inputs such as letters since the user can insert letters
        
        System.out.println("insert the amount of money that you want to withdraw :");
        String amount  = System.console().readLine();
        // String s = String.valueOf(account);
        if(account == 1){
            
            if(Double.parseDouble(amount) > this.savingsBalance){
                System.out.println("Insufficient funds!");
                
            }
            else{

                this.savingsBalance = this.savingsBalance - Double.parseDouble(amount);
                System.out.println(String.format("your withdrawl is %s your balance is %s",Double.parseDouble(amount),this.savingsBalance));
                System.out.println("Total balance "+totalAmountOfMoney);
                System.out.println("Savings account balance "+this.savingsBalance);
            }
        }
        
        else if(account == 2){
            
            if(Double.parseDouble(amount) > this.checkingBalance){
                System.out.println("Insufficient funds!");
                
            }
            else{

                this.checkingBalance = this.checkingBalance - Double.parseDouble(amount);
                System.out.println(String.format("your withdrawl is %s your balance is %s",Double.parseDouble(amount),this.checkingBalance));
                System.out.println("Checking account balance "+this.checkingBalance);
            }
        }

        else{

            System.out.println("No such option found, try again please");

        }
    }
    else{
        System.out.println("No such option found, try again please ");

    }

    }

    public double totalMoney(){
        return this.checkingBalance+this.savingsBalance;
    }

    private long genUserAccountNumber(){
        long random = (long)  Math.floor(Math.random() * ( 999999999 - 111111111 + 1) + 1111111111);
        return random; 

    }
    public long getAccountNumber(){
        return this.accountNumber;
    }

}


