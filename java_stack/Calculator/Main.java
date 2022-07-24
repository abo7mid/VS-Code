package Calculator;

public class Main {
    public static void main(String[] args){
        Calculator calc = new Calculator();
        calc.setOperandOne(10.5);
        calc.setOperandTwo(5.2);
        calc.setOperation("+");
        calc.performOperation();
        System.out.println(calc.getResults());
    }
}
