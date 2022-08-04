package com.example.demo;

//import java.util.ArrayList;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
//import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class FormController {
	
	
	
	
	
    @RequestMapping("/")
	public String index() {
		System.out.println("redirected");
		return "redirect:/omikuji";
		
	}
    
    
    
    @RequestMapping(value="/omikuji", method=RequestMethod.GET)
    public String Omikuji(Model model) {
    	System.out.println("get");
    	return "Omikuji.jsp";
    }

    @RequestMapping(value="/omikuji",method=RequestMethod.POST)//a route that process the post request and at the end we should redirect
    public String OmikujiPost(HttpSession session, @RequestParam(value="number") String number,
				    @RequestParam(value="name") String name,
					@RequestParam(value="city") String city,
					@RequestParam(value="hobby") String hobby,
					@RequestParam(value="living") String living,
			/*
			 * user @PathVariable() for get method
			 * @PathVariable(value="hobby") String gethobby,
			 * 
			 * @PathVariable(value="living") String getliving,
			 */
					@RequestParam(value="say") String say) {
    	// CODE TO PROCESS FORM ie. check email and password
 
    	
    	session.setAttribute("number",number);
    	session.setAttribute("city",city);
    	session.setAttribute("name",name);
    	session.setAttribute("hobby",hobby);
    	session.setAttribute("living",living);
    	session.setAttribute("say",say);
    	
    	
    	
    	System.out.println("POST");
        return "redirect:/omikuji/show";
//    	return "show.jsp";
    }
    
    
    
    @RequestMapping(value="/omikuji/show", method=RequestMethod.GET)
    public String show(Model model) {
    	System.out.println("get");
    	return "show.jsp";
    }
}
