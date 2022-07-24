package ZooKeeper;

public class Bat extends Mammal{ 
    private int energyLevel; //300


    public Bat(){
        this.energyLevel = 300;
        displayEnergy();
        
    }

    public Bat(int energyLevel){
        super(energyLevel);
        this.energyLevel = displayEnergy();
        
    }
    public void fly(){
        System.out.println("the bat has flown, click click click click");
        setEnergy(this.energyLevel = this.energyLevel - 50);
        displayEnergy();
    }
    public void eatHumans(){
        System.out.println("the bat has eaten");
        setEnergy(this.energyLevel = this.energyLevel + 25);
        displayEnergy();
        
    }
    public void attackTown(){
        System.out.println("the bat attacks a town");
        setEnergy(this.energyLevel = this.energyLevel - 100);
        displayEnergy();
        
    }
    
}
