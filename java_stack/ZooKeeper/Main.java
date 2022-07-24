package ZooKeeper;

public class Main {
    
    public static void main(String[] args){
        System.out.println("----------Gorilla---------");
        Gorilla gorilla = new Gorilla();
        gorilla.throwSomething();
        gorilla.throwSomething();
        gorilla.throwSomething();
        gorilla.eatBananas();
        gorilla.eatBananas();
        gorilla.climb();
        System.out.println("----------Bat---------");
        Bat bat = new Bat(300);
        bat.attackTown();
        bat.attackTown();
        bat.attackTown();
        bat.eatHumans();
        bat.eatHumans();
        bat.fly();
        bat.fly();
    


    }
}
