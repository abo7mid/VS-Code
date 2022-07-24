package ZooKeeper;

public class Gorilla extends Mammal{
    private int energyLevel;
    public Gorilla() {
        this.energyLevel = displayEnergy();
    }

    public void throwSomething() {
        System.out.println("the gorill has thrown banana peel at people ");//you should stop giving her bananas Ms zoo keeper

        //lose energy  -5
        this.energyLevel = this.energyLevel - 5;
        System.out.println("Gorilla Energy "+this.energyLevel);

        // this.displayEnergy();

        

    }

    public void eatBananas() {
        System.out.println("the gorilla has eaten a banana");
        //gain energy 10
        this.energyLevel = this.energyLevel + 10;
        System.out.println("Gorilla Energy "+this.energyLevel);
    }
    
    public void climb() {
        System.out.println("the gorilla has climbed a tree");
        //lose energy 10
        this.energyLevel = this.energyLevel - 10;
        System.out.println("Gorilla Energy "+this.energyLevel);
    }
    
    // public void testMethod(){
    // 
    //     System.out.println("Gorilla Method");
    // }
}
