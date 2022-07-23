package Bank;

public class Main {
    public static void main(String[] args){
        
        BankAccount account1 = new BankAccount();

        account1.deposite();
        account1.deposite();
        account1.withdraw();
        account1.getCheckingBalance();
        account1.getSavingBalance();
        System.out.println("Your Total Balance "+ account1.totalMoney());
        // account1.checkingBalance = 500.0;  // since it is private cannot be accessed
        System.out.println(account1.getAccountNumber());

        

    }
}
