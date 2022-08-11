package com.codingdojo.mvc2.services;

import java.util.List;

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

}
