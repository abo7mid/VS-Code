package com.example;

public class Painting extends Art {

	String paintType;
	
	public Painting(String paintType) {
		this.paintType = paintType;
	}
	@Override
	public void viewArt() {
		// TODO Auto-generated method stub
		System.out.println(paintType);
		
	}

}
