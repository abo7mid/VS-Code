package Calculator;

public class Main {
    public static void main(String[] args){
        Calculator2 calc = new Calculator2();
        calc.performOperation(10.5);
        calc.performOperation("+");
        
        calc.performOperation(5.2);
        calc.performOperation("*");
        calc.performOperation(10.0);

    
        calc.performOperation("=");
        calc.getResults();
    }
}
