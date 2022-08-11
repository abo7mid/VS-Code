package com.codingdojo.mvc.controller;

//import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
//import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
//import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.codingdojo.mvc.models.Book;
import com.codingdojo.mvc.services.BookService;
@Controller
public class BooksApi {
    private final BookService bookService;
    
    public BooksApi(BookService bookService) {
    	this.bookService = bookService;
    }
    @RequestMapping(value="/",method=RequestMethod.GET)
    public String index() {
        return  "redirect:/books/create";
    }
    
    @RequestMapping(value="/books/create",method=RequestMethod.GET)
    public String createBook() {
    	return "books/createBook.jsp";
    }
    
    
    @RequestMapping(value="/books/create",method=RequestMethod.POST)
    public String storeBook(
    		@RequestParam(value="title") String title,
    		@RequestParam(value="lang") String language,
    		@RequestParam(value="desc") String description,
    		@RequestParam(value="pages") Integer numberOfPages,
    		RedirectAttributes redirectAttr)
    {
    	Book book = new Book(title, description, language, numberOfPages);
		bookService.createBook(book);
		redirectAttr.addFlashAttribute("success","Your books has been created successfully!");
		return  "redirect:/books/create";
    }
    
    
    @RequestMapping(value="/books/view",method=RequestMethod.GET)
    public String viewBooks(Model model) {
    	    model.addAttribute("books",bookService.getAllBooks());   
    	return "books/viewBooks.jsp";
    }
    
    @RequestMapping(value="/books/{id}",method=RequestMethod.GET)
    public String viewBook(@PathVariable("id") Long id ,Model model) {
    	model.addAttribute("book",bookService.findBook(id));   
    	return "books/viewBook.jsp";
    }

}