package com.codingdojo.Languages.controllers;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.codingdojo.Languages.models.Language;
import com.codingdojo.Languages.services.LanguageService;

@Controller
public class LanguageController {
	@Autowired
	LanguageService languageService;
	//index will redirect to /languages
	@GetMapping("/")
	public String index() {
		return "redirect:/languages";
	}
	
	
	//get the form to create a language
	@GetMapping("/languages")
	public String dashboard(@ModelAttribute("language") Language language,Model model) {
		model.addAttribute("languages", languageService.getAll());
		return "create.jsp";
	}
	
	//handle the post method
	@PostMapping("languages")
	public String create(@Valid @ModelAttribute("language") Language language, BindingResult result,RedirectAttributes re,Model model) {
		if (result.hasErrors()) {
			return "create.jsp";
		}
		else {
			  languageService.create(language);
			  re.addFlashAttribute("created", "created successfully");
			  model.addAttribute("languages", language); 
			  return "redirect:/languages";
		}
	}
	
	//get the form to update a language
	@GetMapping("/languages/edit/{id}")
	public String edit(@PathVariable("id") Long id, Model model) {
		Language language = languageService.findById(id);
		model.addAttribute("language", language);
		return "edit.jsp";
	}
	@PutMapping("/languages/edit/{id}")
	public String update(@Valid @ModelAttribute("language") Language language,BindingResult res,RedirectAttributes re, Model model) {
		    if(res.hasErrors()) {
		    	return "edit.jsp";
		    }
		
		    else {
		    	
		    	languageService.update(language);
		    	re.addFlashAttribute("updated", "Language has been updated");
		    	return "redirect:/languages";
		    }
	}
	
	@GetMapping("/languages/{id}")
	public String view(@PathVariable("id") Long id, Model model) {
		Language language = languageService.findById(id);
		if(language == null) {
			return "redirect:/languages";
		}
		else {
			
		model.addAttribute("language", language);
		return "view.jsp";
		}
	}
	
	@PostMapping("/languages/{id}")
	public String delete(@PathVariable("id") Long id) {
		languageService.delete(id);
		
		return "redirect:/languages";
	}
	
	/*
	 * @PutMapping("/languages/edit/{id}") public String edit(@PathVariable("id")
	 * Long id) { return "edit.jsp";
	 * 
	 * }
	 */

}
