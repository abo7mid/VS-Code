package com.example;

public class Sculpture extends Art {
	
	String material;

	public Sculpture(String material) {
		this.material = material;
	}
	@Override
	public void viewArt() {
		// TODO Auto-generated method stub
		System.out.println(material);

	}

}
