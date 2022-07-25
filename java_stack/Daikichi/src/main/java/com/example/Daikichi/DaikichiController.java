package com.example.Daikichi;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DaikichiController {

		
		
		
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

//		@RequestMapping(value="/greeting/{username}",method=RequestMethod.GET)
//		public String greeting(@PathVariable("username") String username) {
//			return "Hello "+ username;
//		}


	}


