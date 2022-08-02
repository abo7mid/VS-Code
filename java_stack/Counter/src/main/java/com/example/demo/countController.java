package com.example.demo;

import javax.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class countController {

	
	@RequestMapping("/")
	public String index(Model model, HttpSession session) {
        model.addAttribute("welcome", "Welcome User!");
		if (session.getAttribute("count") == null) {
			 session.setAttribute("count", 0);


		}
		else {
		     int currentCount = (int)session.getAttribute("count") + 1;
			 session.setAttribute("count", currentCount);


		}
		return "index.jsp";
	}
	@RequestMapping("/counter")
	public String count(Model model,HttpSession session) {
		int currentCount = (int)session.getAttribute("count");
	     model.addAttribute("countToShow", currentCount);
		 

		return "counter.jsp";
	}
	
	
}