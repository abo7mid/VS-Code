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
	
	public void  deleteBook(Long id) {
		 pokeRepo.deleteById(id);
		
	}

	public Poke createBook(Poke b) {
		return pokeRepo.save(b);
		
	}
	public Poke updateBook(Poke b) {
		return pokeRepo.save(b);
				
	}
	
	public List<Poke> getBooks() {
		return pokeRepo.findAll();
	}
	
	public Optional<Poke> findBookApi(Long id) {
		return pokeRepo.findById(id);
	}
	public Poke findBook(Long id) {
       Optional<Poke> optionalBook = pokeRepo.findById(id);
       if(optionalBook.isPresent()) {
           return optionalBook.get();
       } else {
           return null;
       } 
	}
}
