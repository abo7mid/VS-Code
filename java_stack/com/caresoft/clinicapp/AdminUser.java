package com.caresoft.clinicapp;

//... imports class definition...
import java.util.ArrayList;
import java.util.Date;

public class AdminUser extends User implements HIPAACompliantUser, HIPAACompliantAdmin {
    // Inside class:

    private Integer employeeID;
    private String role;
    private ArrayList<String> securityIncidents;

    public AdminUser(Integer id) {
        super(id);
        securityIncidents = new ArrayList<String>();
    }
    // TO DO: Implement a constructor that takes an ID and a role
    public AdminUser(Integer id, String role){
        super(id);
        this.employeeID = id;
        this.role = role;
        securityIncidents = new ArrayList<String>();
    }
    // TO DO: Implement HIPAACompliantUser!

    public void newIncident(String notes) {
        String report = String.format(
                "Datetime Submitted: %s \n,  Reported By ID: %s\n Notes: %s \n",
                new Date(), this.id, notes);
        securityIncidents.add(report);
    }

    public void authIncident() {
        String report = String.format(
                "Datetime Submitted: %s \n,  ID: %s\n Notes: %s \n",
                new Date(), this.id, "AUTHORIZATION ATTEMPT FAILED FOR THIS USER");
        securityIncidents.add(report);
    }

    // TO DO: Implement HIPAACompliantAdmin!
    @Override
    public ArrayList<String> reportSecurityIncidents() {
        return securityIncidents;
    }

    @Override
    public boolean assignPin(int pin) {
        if (String.valueOf(pin).length() < 6) {

            return false;
        }
        setPin(pin);
        return true;
    }

    @Override
    public boolean accessAuthorized(Integer confirmedAuthID) {
        if (confirmedAuthID != getId()) {
            authIncident();
            return false;
        }
        return true;
    }

    // TO DO: Setters & Getters
}
