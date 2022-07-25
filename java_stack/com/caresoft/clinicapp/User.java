package com.caresoft.clinicapp;

public class User {
    protected Integer id;
    protected int pin;
    
    // TO DO: Getters and setters
    public int getPin(){
        return this.pin;
    }
    protected void setPin(int pin){ // only inherated classes will access this functions
        this.pin = pin;
    }

    protected void setId(Integer id){
        this.id = id;
    }

    public int getId(){
        return this.id;
    }

	// Implement a constructor that takes an ID
    public User(Integer id){
        this.id = id;
    }
}
