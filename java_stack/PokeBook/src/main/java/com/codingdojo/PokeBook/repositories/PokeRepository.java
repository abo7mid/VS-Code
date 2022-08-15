package com.codingdojo.PokeBook.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.codingdojo.PokeBook.models.Poke;

public interface PokeRepository extends CrudRepository<Poke, Long>{
  List<Poke> findAll();
}
