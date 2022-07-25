package com.example.demo;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Daikichi{

		
		
		
		@RequestMapping("/daikichi")
		public String Hello() {
			return "Welcome!";
		}
		
		
		@RequestMapping(value="/daikichi/today",method=RequestMethod.GET)
		public String today() {
			return "Today you will find luck in all your endeavors!";
		}

		
		@RequestMapping(value="/daikichi/tomorrow",method=RequestMethod.GET)
		public String tomorrow() {
			return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
		}

		@RequestMapping(value="/greeting/{username}",method=RequestMethod.GET)
		public String greeting(@PathVariable("username") String username) {
			return "Hello "+ username;
		}


		@RequestMapping(value="/daikichi/travel/{city}",method=RequestMethod.GET)
		public String city(@PathVariable("city") String city) {
			return "Congratulations! You will soon travel to "+ city +"!";
		}

		
		@RequestMapping(value="/daikichi/lotto/{num}",method=RequestMethod.GET)
		public String even(@PathVariable("num") String num) {
			int par = Integer.parseInt(num);
			if(par % 2 == 0) {
				return "You will take a grand journey in the near future, but be weary of tempting offers";
			}
			return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends.";
		}

	}
