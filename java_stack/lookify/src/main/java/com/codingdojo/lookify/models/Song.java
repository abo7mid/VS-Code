package com.codingdojo.lookify.models;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.persistence.Table;
import javax.validation.constraints.Max;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

import org.springframework.format.annotation.DateTimeFormat;

@Entity @Table(name="songs")
public class Song {
	
	public Song( Long id,String name,int rating,String artist) {
		this.id = id;
		this.name = name;
		this.rating = rating;
		this.artist = artist;
	}

	public Song() {
		
	}
	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private Long id;

	@NotNull
	@Size(min=5, max=20, message="Characters must be more 5")
	private String name;
	
	@NotNull
	@Size(min=5, max=20, message="Characters must be more 5")
	private String artist;
	
	@NotNull
	@Max(value=10, message="value must be more than 1 and less than 10")
	private int rating;
	
	
	
	@Column(updatable=false)
	@DateTimeFormat(pattern="yyyy-MM-dd")
	private Date created_at;
	
	@DateTimeFormat(pattern="yyyy-MM-dd")
	private Date updated_at;
	
	@PrePersist
	protected void onCreate() {
		this.created_at = new Date();
	}
	
	@PreUpdate
	protected void onUpdate() {
		this.updated_at = new Date();
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	public String getArtist() {
		return artist;
	}
	
	public void setArtist(String artist) {
		this.artist = artist;
	}

	public int getRating() {
		return rating;
	}

	public void setRating(int rating) {
		this.rating = rating;
	}
	public Long getId() {
		return id;
	}
	/*
	 * public void setId(Long id) { this.id = id; }
	 */
	
}
