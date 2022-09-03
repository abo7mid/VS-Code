package com.codingdojo.lookify.controllers;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.codingdojo.lookify.models.Song;
import com.codingdojo.lookify.services.SongService;

@Controller
public class LookifyController {

	public LookifyController() {

	}

	@Autowired
	SongService songService;

	@GetMapping("/")
	public String index() {
		return "index.jsp";
	}

	@GetMapping("/dashboard")
	public String dashboard(@ModelAttribute("song") Song song, Model model) {
		model.addAttribute("songs", songService.getAll());
		return "dashboard.jsp";
	}

	@GetMapping("/songs/new")
	public String create(@ModelAttribute("song") Song song) {
		return "new.jsp";
	}

	@PostMapping("/songs/new")
	public String save(@Valid @ModelAttribute("song") Song song, BindingResult res, RedirectAttributes re,
			Model model) {
		if (res.hasErrors()) {

			return "new.jsp";
		} else {
			songService.create(song);
			return "redirect:/songs/new";
		}
	}

	@GetMapping("/songs/{id}")
	public String view(@PathVariable("id") Long id, Model model) {
		model.addAttribute("song", songService.findById(id));
		return "view.jsp";
	}

	@PostMapping("/delete/{id}")
	public String destroy(@PathVariable("id") Long id) {
		songService.delete(id);
		return "redirect:/dashboard";
	}

	@GetMapping("/search/topTen")
	public String top10(Model model) {
		model.addAttribute("songs", songService.top10());
		return "top10.jsp";

	}

	@GetMapping(value = "/search")
	public String search(@RequestParam(value = "artist") String artist, HttpSession session,RedirectAttributes re) {
		System.out.println(artist);
		if(artist.isBlank()) {
			  re.addFlashAttribute("blank", "Search value must not be empty!");
			  return "redirect:/dashboard";
		}
		else {
			
			session.setAttribute("artist", artist);
			return "redirect:/search/" + artist;
		}

	}

	
	  @GetMapping("/search/{artist}")
	  public String search(@PathVariable("artist") String artist,Model model) { 
		  model.addAttribute("artist", artist);
		  System.out.println(artist);
		  model.addAttribute("songs",songService.findByName(artist));
		  return "search.jsp";
	  
	  }
	 

		/*
		 * @GetMapping("/search/{artist}") public String search(@RequestParam("artist")
		 * String artist, Model model) { model.addAttribute("artist", artist);
		 * System.out.println(artist); model.addAttribute("songs",
		 * songService.findByName(artist)); return "search.jsp";
		 * 
		 * }
		 */

}
