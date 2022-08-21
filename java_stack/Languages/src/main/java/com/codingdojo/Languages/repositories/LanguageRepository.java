package com.codingdojo.Languages.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.codingdojo.Languages.models.Language;

public interface LanguageRepository extends CrudRepository<Language, Long>{
 List<Language> findAll();
}
