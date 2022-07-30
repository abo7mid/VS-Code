package com.example.demo;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller

public class DisplayDateTime {
	SimpleDateFormat time = new SimpleDateFormat("hh:mm aa");

	SimpleDateFormat date = new SimpleDateFormat("E 'the' d 'of' MMM ',' y");
//	SimpleDateFormat date6 = new SimpleDateFormat("dd/yy/mm");
//	SimpleDateFormat date7 = new SimpleDateFormat("ddd/yyy/mmm");
//	SimpleDateFormat date8 = new SimpleDateFormat("dddd/yyyy/mmmm");
//
//	SimpleDateFormat date0 = new SimpleDateFormat("D/Y/M");
//	SimpleDateFormat date1 = new SimpleDateFormat("DD/YY/MM");
//	SimpleDateFormat date2 = new SimpleDateFormat("DDD/YYY/MMM");
//	SimpleDateFormat date3 = new SimpleDateFormat("DDDD/YYYY/MMMM");
//	SimpleDateFormat date5 = new SimpleDateFormat("E d L");
//	SimpleDateFormat date9 = new SimpleDateFormat("e d L");

	
	//"DDD/YY/m" 29/22/7
	//"DD/YY/mm" 29/22/07
	//"DD/Y/mmm" 29/2022/Jul
	//"DD/y/mmm" 29/2022/July
	//Saturday, the 22 of January, 2028  "E 'the' d 'of' MMM ',' y"
	/*
	 * SimpleDateFormat date4 = new
	 * SimpleDateFormat("D,DD,DDD,DDDD/M,MM,MMM,MMM/Y,YY,YYY,YYYY");//
	 * SimpleDateFormat a = new SimpleDateFormat("MM/dd/yyyy aa");
	 *///	java.util.Date date = new java.util.Date();
	
	@RequestMapping("/")
	public String index() {
		
		return "index.jsp";
	}
	@RequestMapping("/date")
	public String date(Model model) {
		model.addAttribute("date",date.format(new Date()).toString());
//		model.addAttribute("date1",date1.format(new Date()).toString());
//		model.addAttribute("date2",date2.format(new Date()).toString());
//		model.addAttribute("date3",date3.format(new Date()).toString());
//		model.addAttribute("date4",date4.format(new Date()).toString());
//		model.addAttribute("date5",date5.format(new Date()).toString());
//		model.addAttribute("date6",date6.format(new Date()).toString());
//		model.addAttribute("date7",date7.format(new Date()).toString());
//		model.addAttribute("date8",date8.format(new Date()).toString());
////		model.addAttribute("date9",date9.format(new Date()).toString());



		return "date.jsp";
	}

	@RequestMapping("/time")
	public String time(Model model) {
		model.addAttribute("time",time.format(new Date()).toString());
//		model.addAttribute("time1",a.format(date)) ;
		
		return "time.jsp";
	}

}




