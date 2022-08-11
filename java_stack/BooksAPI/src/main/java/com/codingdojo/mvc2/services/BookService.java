package com.codingdojo.mvc2.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.mvc2.models.Book;
import com.codingdojo.mvc2.repository.BookRepository;

@Service
public class BookService {
	public final BookRepository bookRepository;

	public BookService(BookRepository bookRepository) {
		this.bookRepository = bookRepository;
	}
	public void  deleteBook(Long id) {
		 bookRepository.deleteById(id);
		
	}

	public Book updateBook(Book b) {
		return bookRepository.save(b);
				
	}
	
	public List<Book> getBooks() {
		return bookRepository.findAll();
	}
	
	public Optional<Book> findBookApi(Long id) {
		return bookRepository.findById(id);
	}
	public Book findBook(Long id) {
        Optional<Book> optionalBook = bookRepository.findById(id);
        if(optionalBook.isPresent()) {
            return optionalBook.get();
        } else {
            return null;
        } 
	}

}
