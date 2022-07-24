package ZooKeeper;

public class Gorilla extends Mammal{

    private int energyLevel;


    public Gorilla() {        
        this.energyLevel = displayEnergy();

    }
    public Gorilla(int energyLevel) {  
        // this will allow to change default energyLevel value      
        super(energyLevel);
        this.energyLevel = energyLevel;
        displayEnergy();
    }

    public void throwSomething() {
        System.out.println("the gorill has thrown banana peel at people ");//you should stop giving her bananas Ms zoo keeper
        this.energyLevel = this.energyLevel - 5;
        System.out.println("Gorilla Energy "+this.energyLevel);

    }

    public void eatBananas() {
        System.out.println("the gorilla has eaten a banana");
        this.energyLevel = this.energyLevel + 10;
        System.out.println("Gorilla Energy "+this.energyLevel);
    }
    
    public void climb() {
        System.out.println("the gorilla has climbed a tree");
        this.energyLevel = this.energyLevel - 10;
        System.out.println("Gorilla Energy "+this.energyLevel);
    }
    

}
