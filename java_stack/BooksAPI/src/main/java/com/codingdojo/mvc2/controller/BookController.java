package com.codingdojo.mvc2.controller;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.codingdojo.mvc2.models.Book;
import com.codingdojo.mvc2.services.BookService;

@Controller
public class BookController {
	
	@Autowired
	BookService bookService;
//	public BookController(BookService bookService) {
//		this.bookService = bookService;
//	}

//	@GetMapping("/404")
//	public String NotFound() {
//		return "404.jsp";
//	}

	@GetMapping("/")
	public String index() {
		return "redirect:/books";
	}
	@GetMapping("/books")
	public String books() {
		return "index.jsp";
	}
	
	
	@GetMapping("/books/{bookId}")
	public String bookById(@PathVariable("bookId") Long bookId,Model model,RedirectAttributes redirect) {
		Book book = bookService.findBook(bookId);
		if(book!=null) {
			model.addAttribute("book",book);
			
		}
		else {
			redirect.addFlashAttribute("bookNotFound",String.format("Book with id %s is not found", bookId));
			return "redirect:/books";
		}
		return "show.jsp";
	}
}
