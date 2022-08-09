package Calculator;

public class Calculator2 {


    private Double operandOne = 0.0;
    private Double operandTwo = 0.0;
    private String operation;
    private Double result = 0.0;
    private boolean addSet = false;
    private boolean subSet = false;
    private boolean mulSet = false;
    private boolean divSet = false;
    private boolean equSet = false;

    public void performOperation(Double operand) {
        if(this.operandOne != 0){

            this.operandTwo = operand;
        }
        else{
            this.operandOne = operand;

        }
    }


    public void performOperation(String operation) {
        if(operation.equals("+")){
            // this.operation = operation;

            addSet = true;
        }
        if(operation.equals("-")){
            // this.operation = operation;
            
            subSet = true;
        }
        if(operation.equals("*")){
            // this.operation = operation;
            
            mulSet = true;
        }
        if(operation.equals("/")){
            // this.operation = operation;
            
            divSet = true;
        }
        if(operation.equals("=")){
            // this.operation = operation;

            equSet = true;
        }

        }





        
        public void getResults() {
        if(addSet){
            System.out.print("addSet\n");
            result = operandOne + operandTwo;
        } 
        if(subSet){
            System.out.print("subSet\n");
            result = operandOne - operandTwo;
        } 
        if(mulSet){
            System.out.print("mulSet\n");
            result = operandOne * operandTwo;
        } 
        if(divSet){
            System.out.print("divSet\n");
            result = operandOne / operandTwo;
        } 
        
        if(equSet){

                System.out.print(this.result+"\n");
            }
        }


    }

