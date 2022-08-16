package com.codingdojo.PokeBook.controllers;

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

import com.codingdojo.PokeBook.models.Poke;
import com.codingdojo.PokeBook.services.PokeService;

@Controller
public class PokeController {

	@Autowired
	PokeService pokeService;
	
	
  // Create Book code
	@GetMapping("/expenses")
	public String get(@ModelAttribute("poke") Poke poke, Model model) {
		 
		 model.addAttribute("poke1", pokeService.getPoke());
		return "index.jsp";
	}
	
	
	@PostMapping("/expenses")
	public String post(@Valid @ModelAttribute("poke") Poke poke, BindingResult result, RedirectAttributes re, Model model) {
		 model.addAttribute("poke1", pokeService.getPoke());

		if (result.hasErrors()) {

			return "index.jsp";
		}
		else {
			pokeService.createPoke(poke);
			re.addFlashAttribute("created","the Poke has been created");
			return "redirect:/expenses";
		}
	}
	
	
	
	
	
	
	
	// update book code
	@GetMapping("/expenses/edit/{id}")
	public String edit(@PathVariable("id") Long id, Model model) {
		Poke poke  = pokeService.findPoke(id);
		model.addAttribute("poke", poke);
		model.addAttribute("poke1", pokeService.getPoke());

		return "edit.jsp";
	}
	
	
	@PutMapping(value="/expenses/edit/{id}")
	public String update(@Valid @ModelAttribute("poke") Poke poke, BindingResult result, RedirectAttributes re, Model model) {
		model.addAttribute("poke1", pokeService.getPoke());

		
		if (result.hasErrors()) {
			
			return "edit.jsp";
		}
		else {
			pokeService.updatePoke(poke);
			re.addFlashAttribute("updated",poke.getExpense()+" has been updated successfully");
			return "redirect:/expenses";
		}
	}
}
