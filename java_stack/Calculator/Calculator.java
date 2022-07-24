package Calculator;

public class Calculator {

    private Double operandOne = 0.0;
    private Double operandTwo = 0.0;
    private String operation;
    private Double result = 0.0;

    public void setOperandOne(Double operandOne) {
        this.operandOne = operandOne;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public void setOperandTwo(Double operandTwo) {
        this.operandTwo = operandTwo;
    }

    public void performOperation() {
        if (this.operation.equals("+")){
            System.out.println("addition");
            this.result = operandOne + operandTwo;
            
        }
        if (this.operation.equals("-")){
            System.out.println("subtraction");
            this.result = operandOne - operandTwo;

        }
    }

    public Double getResults() {
        return result;
    }
}
