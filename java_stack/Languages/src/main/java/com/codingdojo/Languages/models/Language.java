package com.codingdojo.Languages.models;

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

@Entity @Table(name="languages")
public class Language {
	public Language() {
		
	}
	public Language(Long id,String name,String creator,double currentVersion) {
		this.id = id;
		this.name = name;
		this.creator = creator;
		this.currentVersion = currentVersion;
	}

	@Id
	@GeneratedValue(strategy= GenerationType.IDENTITY)
	private Long id;

	@NotNull
	@Size(min=2, max=20, message="value must be more than 2 and less than 10")
	private String name;
	
	@NotNull
	@Size(min=2, max=20, message="value must be more than 2 and less than 10")
	private String creator;
	
	@NotNull
	@Max(value=1000,message="value cannot exceed 1000")
	private double currentVersion;
	
	
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

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getCreator() {
		return creator;
	}

	public void setCreator(String creator) {
		this.creator = creator;
	}

	public double getCurrentVersion() {
		return currentVersion;
	}

	public void setCurrentVersion(double currentVersion) {
		this.currentVersion = currentVersion;
	}
	

}
