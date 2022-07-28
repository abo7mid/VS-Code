package com.example;

import java.util.ArrayList;

public class Museum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Art a = new Art();
		Painting p1 = new Painting("Oil");    //Oil, Watercolor, Acrylic
		Painting p2 = new Painting("Watercolor");
		Painting p3 = new Painting("Acrylic");
        Sculpture s1 = new Sculpture("Marble");//Marble, Bronze, Porcelain
        Sculpture s2 = new Sculpture("Bronze");
        
        ArrayList<Art> museum = new ArrayList<Art>();
        museum.add(p1);
        museum.add(p2);
        museum.add(p3);
        museum.add(s1);
        museum.add(s2);
        
        p1.viewArt();
        p3.viewArt();
        s1.viewArt();
        p2.viewArt();
        s2.viewArt();
        
        
        
	}

}
