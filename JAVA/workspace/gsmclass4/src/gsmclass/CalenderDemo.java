package gsmclass;

import java.util.Calendar;
import java.util.Date;

public class CalenderDemo {

	public static void main(String[] args) {
		Date now = new Date();
		System.out.println(now);
		
		Calendar c = Calendar.getInstance();
		System.out.println(c);
		
		System.out.println(c.get(Calendar.YEAR));
		System.out.println(c.get(Calendar.MONTH) + 1);
		
		System.out.println(c.get(Calendar.DAY_OF_MONTH));
		System.out.println(c.get(Calendar.DAY_OF_WEEK));
		System.out.println(c.get(Calendar.WEEK_OF_YEAR));
		System.out.println(c.get(Calendar.WEEK_OF_MONTH));
		
		System.out.println(c.get(Calendar.HOUR));
		System.out.println(c.get(Calendar.HOUR_OF_DAY));
		System.out.println(c.get(Calendar.MINUTE));
	}

}
