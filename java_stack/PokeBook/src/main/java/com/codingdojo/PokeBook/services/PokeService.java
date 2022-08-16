package com.codingdojo.PokeBook.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.codingdojo.PokeBook.models.Poke;
import com.codingdojo.PokeBook.repositories.PokeRepository;

@Service
public class PokeService {

	@Autowired
	PokeRepository pokeRepo;
	
	public void  deletePoke(Long id) {
		 pokeRepo.deleteById(id);
		
	}

	public Poke createPoke(Poke b) {
		return pokeRepo.save(b);
		
	}
	public Poke updatePoke(Poke b) {
		return pokeRepo.save(b);
				
	}
	
	public List<Poke> getPoke() {
		return pokeRepo.findAll();
	}
	
	public Optional<Poke> findPokeApi(Long id) {
		return pokeRepo.findById(id);
	}
	
	public Poke findPoke(Long id) {
       Optional<Poke> optionalPoke = pokeRepo.findById(id);
       if(optionalPoke.isPresent()) {
           return optionalPoke.get();
       } else {
           return null;
       } 
	}
}
