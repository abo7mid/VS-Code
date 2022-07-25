package com.example.demo;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/")
public class Human {

		
		
		
//		@RequestMapping("/")
//		public String Hello() {
//			return "Hello Human";
//		}
		
		
//		@RequestMapping(value="/daikichi/",method=RequestMethod.GET)
//		public String today() {
//			return "Today you will find luck in all your endeavors!";
//		}

		

//		@RequestMapping(value="/greeting/{username}",method=RequestMethod.GET)
//		public String greeting(@PathVariable("username") String username) {
//			return "Hello "+ username;
//		}
		
		
//		@RequestMapping("/search")
//		public String index(@RequestParam(value="q") String searchQuery) {
//			return "You searched for: "+ searchQuery;
//		}

		@RequestMapping("")
		public String index(@RequestParam(value="name",required=false) String name,String lastname,String times) {
			if(name == null) {
				if(lastname != null) {
					return "you must provide both first & last name, "+lastname;
				}
				return "Hello Human";
			}
			else if(name != null && lastname != null) {
				return "Hello "+name +" "+ lastname;
				
			}
			else if(times != null && name != null) {
				String greeting = "";
				for(int i = 0;i<Integer.parseInt(times);i++) {
					greeting = greeting + "Hello "+ name+"\t";
				}
				return greeting;
			}
			
			return "Hello "+ name;
		}

	}


