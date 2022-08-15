package com.codingdojo.PokeBook.controllers;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.codingdojo.PokeBook.models.Poke;
import com.codingdojo.PokeBook.services.PokeService;

@Controller
public class PokeController {

	@Autowired
	PokeService pokeService;
	
	
	
	
	
	@GetMapping("/expenses")
	public String index(@ModelAttribute("poke") Poke poke, Model model) {
		 
		 model.addAttribute("poke1", pokeService.getBooks());
//		 System.out.println(pokeService.getBooks());
		return "index.jsp";
	}
	
	
	@PostMapping("/expenses")
	public String indexPost(@Valid @ModelAttribute("poke") Poke poke, BindingResult result, RedirectAttributes re, Model model) {
		 model.addAttribute("poke1", pokeService.getBooks());

		if (result.hasErrors()) {

			return "index.jsp";
		}
		else {
			pokeService.createBook(poke);
			re.addFlashAttribute("created","the Poke has been created");
			return "redirect:/expenses";
		}
	}
}
