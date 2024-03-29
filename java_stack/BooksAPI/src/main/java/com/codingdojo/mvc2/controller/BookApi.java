package com.codingdojo.mvc2.controller;

import com.codingdojo.mvc2.models.Book;
import com.codingdojo.mvc2.services.BookService;

import java.util.List;
import java.util.Optional;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BookApi {
 private final BookService bookService;
 public BookApi(BookService bookService){
     this.bookService = bookService;
 }
 // other methods removed for brevity
 

 @RequestMapping(value="/api/books/{id}", method=RequestMethod.PUT)
 public Book update(
 		@PathVariable("id") Long id, 
 		@RequestParam(value="title") String title, 
 		@RequestParam(value="description") String desc, 
 		@RequestParam(value="language") String lang,
 		@RequestParam(value="pages") Integer numOfPages) {
     Book book = new Book(id,title, desc, lang, numOfPages);
     bookService.updateBook(book);
     return book;
 }
 
 @RequestMapping(value="/api/books", method=RequestMethod.GET)
 public List<Book> getBooks() {
     return bookService.getBooks();
 }
 @RequestMapping(value="/api/books/{bookId}", method=RequestMethod.GET)
 public Optional<Book> getBook(@PathVariable("bookId") Long bookId) {
	 return bookService.findBookApi(bookId);
 }
 
 
 
 @RequestMapping(value="/api/books/{id}", method=RequestMethod.DELETE)
 public void destroy(@PathVariable("id") Long id) {
     bookService.deleteBook(id);
 }
}