package com.codingdojo.lookify.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.codingdojo.lookify.models.Song;

import com.codingdojo.lookify.repositories.SongRepo ;

@Service
public class SongService {
	@Autowired
	SongRepo songRepo;
	
	public void  delete(Long id) {
		 songRepo.deleteById(id);
		
	}

	public Song create(Song b) {
		return songRepo.save(b);
		
	}
	public Song update(Song b) {
		return songRepo.save(b);
				
	}
	
	public List<Song> getAll() {
		return songRepo.findAll();
	}
	
	public Optional<Song> findSongApi(Long id) {
		return songRepo.findById(id);
	}

	
	public Song findById(Long id) {
       Optional<Song> optionalSong = songRepo.findById(id);
       if(optionalSong.isPresent()) {
           return optionalSong.get();
       } else {
           return null;
       } 
	}
	
	
	
	 public List<Song> findByName(String name) {
		   List<Song> artist = songRepo.findByArtist(name);
		   return  artist;
		   
	 }
	 
	 
	 
	public List<Song> top10() {
		return songRepo.findTop10ByOrderByRatingDesc();
	}
}
