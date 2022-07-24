package ZooKeeper;

public class Mammal {
    private int energyLevel;


    public Mammal(){
        this.energyLevel = 100; 
        //default energy for all Mammals
    }
    public Mammal(int energyLevel){
        this.energyLevel = energyLevel;
    }

    public int displayEnergy(){

        System.out.println("Energy level "+energyLevel);
        return this.energyLevel;
    }

    public void setEnergy(int energyLevel){
        this.energyLevel = energyLevel;
    }


}
