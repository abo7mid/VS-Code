package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
//import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.Date;
import java.util.Random;

import javax.servlet.http.HttpSession;

@Controller
public class NinjaGold {
	private int gold;
	static String place;
	static String state;
	static String curgold;
	static String message ;
	static boolean sub = false;
	
	@RequestMapping(value="/",method=RequestMethod.GET)
	public String index() {
		
		return "index.jsp";
	}
	
	public void setGold(int gold) {
		this.gold = this.gold + gold;
	}
	public void subGold(int gold) {
		this.gold = this.gold - gold;
	}
	
	public int getGold() {
		return this.gold;
	}
	@RequestMapping(value="/farm", method=RequestMethod.POST)
	public String farmProcess(HttpSession session,@RequestParam(value="farm") String farm)
	
	{
		Random rand = new Random();
		if(farm != null)
		{
			Integer randomNum = rand.nextInt((20- 10) + 1) + 10;
			setGold(randomNum);    
			session.setAttribute("randomNum",getGold());
			place = "farm";
			state = "earned";
			curgold  =  randomNum.toString();
			sub = false;
			session.setAttribute("sub",sub);

			message = String.format("You entered %s and %s %s. (%s)" ,place,state,curgold, new Date() );
			session.setAttribute("message",message);
   	
  	
		}

		return "redirect:/";
	}
	
	
	@RequestMapping(value="/cave", method=RequestMethod.POST)
	public String caveProcess(HttpSession session,@RequestParam(value="cave") String cave)
	
	{
		Random rand = new Random();
		if(cave != null)
		{
			Integer randomNum = rand.nextInt((10- 5) + 1) + 5;
			setGold(randomNum);    
			session.setAttribute("randomNum",getGold());
			place = "cave";
			state = "earned";
			curgold  =  randomNum.toString();
			sub = false;
			session.setAttribute("sub",sub);

			message = String.format("You entered %s and %s %s. (%s)" ,place,state,curgold, new Date() );
			session.setAttribute("message",message);
            			
		}
		return "redirect:/";
	}
	@RequestMapping(value="/house", method=RequestMethod.POST)
	public String houseProcess(HttpSession session,@RequestParam(value="house") String house)
	
	{
		Random rand = new Random();
		if(house != null)
		{
			Integer randomNum = rand.nextInt((5- 2) + 1) + 2;
			setGold(randomNum);    
			session.setAttribute("randomNum",getGold());
			place = "house";
			state = "earned";
			curgold  =  randomNum.toString();
			sub = false;
			session.setAttribute("sub",sub);
			
			message = String.format("You entered %s and %s %s. (%s)" ,place,state,curgold, new Date() );
			session.setAttribute("message",message);
			
		}
		return "redirect:/";
	}
	@RequestMapping(value="/casino", method=RequestMethod.POST)
	public String casionProcess(HttpSession session,@RequestParam(value="casino") String casion)
	
	{
		Random rand = new Random();
		if(casion != null)
		{
			Integer randomNum = rand.nextInt((50- 0) + 1) + 0;
			if(randomNum % 2 == 0) { //if even add 
				
				setGold(randomNum);    
				session.setAttribute("randomNum",getGold());
				place = "casino";
				state = "earned";
				curgold  =  randomNum.toString();
				sub = false;
				session.setAttribute("sub",sub);

				message = String.format("You entered %s and %s %s. (%s)" ,place,state,curgold, new Date() );
				session.setAttribute("message",message);
			}
			else {// else subtract
				subGold(randomNum);    
				session.setAttribute("randomNum",getGold());
				place = "casion";
				state = "lost";
				curgold  =  randomNum.toString();
				message = String.format("You entered %s and %s %s. (%s)" ,place,state,curgold, new Date() );
				session.setAttribute("message",message);
				sub = true;
				session.setAttribute("sub",sub);
			}
			
		}
		return "redirect:/";
	}

}
