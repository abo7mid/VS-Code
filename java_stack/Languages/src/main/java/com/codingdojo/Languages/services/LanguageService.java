package com.codingdojo.Languages.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.codingdojo.Languages.models.Language;
import com.codingdojo.Languages.repositories.LanguageRepository;

@Service
public class LanguageService {
	@Autowired
	LanguageRepository languageRepo;
	
	public void  delete(Long id) {
		 languageRepo.deleteById(id);
		
	}

	public Language create(Language b) {
		return languageRepo.save(b);
		
	}
	public Language update(Language b) {
		return languageRepo.save(b);
				
	}
	
	public List<Language> getAll() {
		return languageRepo.findAll();
	}
	
	public Optional<Language> findLanguageApi(Long id) {
		return languageRepo.findById(id);
	}
	
	public Language findById(Long id) {
       Optional<Language> optionalLanguage = languageRepo.findById(id);
       if(optionalLanguage.isPresent()) {
           return optionalLanguage.get();
       } else {
           return null;
       } 
	}
}
