package ZooKeeper;

public class Mammal {
    private int energyLevel;


    public Mammal(){
        this.energyLevel = 100;
    }

    public int displayEnergy(){

        System.out.println("Energy level "+energyLevel);
        return this.energyLevel;
    }


    // testing override, this methods is for practicing method overriding
    //     public void testMethod(){
    //         System.out.println("Mammal method");
    //     }
}
