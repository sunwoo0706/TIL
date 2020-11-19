package gsmclass;

import java.text.SimpleDateFormat;
import java.util.Date;

public class SimpleDateFormatDemo {

	public static void main(String[] args) {
		SimpleDateFormat s = new SimpleDateFormat("yyyy-MM-dd a hh:mm:ss");
		Date d = new Date();
		System.out.println(d);
		System.out.println(s.format(d));
		
	}

}
