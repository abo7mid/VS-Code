package com.caresoft.clinicapp;

import java.util.ArrayList;
//... imports class definition...
import java.util.Date;
public class Physician extends User implements HIPAACompliantUser {
    

    // Inside class:    
    private ArrayList<String> patientNotes;

    public Physician(Integer id) {
        super(id);
    }

	
    // TO DO: Constructor that takes an ID
    // TO DO: Implement HIPAACompliantUser!
    @Override
    public boolean assignPin(int pin) {
        if(String.valueOf(pin).length() != 4){

            return false;
        }
        
        setPin(pin);
        return true;
    }

    @Override
    public boolean accessAuthorized(Integer confirmedAuthID) {
        if(confirmedAuthID == getId()){
            return true;
        }
        return false;
    }
	
    public void newPatientNotes(String notes, String patientName, Date date) {
        String report = String.format(
            "Datetime Submitted: %s \n", date);
        report += String.format("Reported By ID: %s\n", this.id);
        report += String.format("Patient Name: %s\n", patientName);
        report += String.format("Notes: %s \n", notes);
        this.patientNotes.add(report);
    }


	
    // TO DO: Setters & Getters
}
