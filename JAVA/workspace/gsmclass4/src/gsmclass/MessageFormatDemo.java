package gsmclass;

import java.text.MessageFormat;

public class MessageFormatDemo {

	public static void main(String[] args) {
		String s = "groot";
		int age = 32;
		String fs = MessageFormat.format("이름::{0} 나이:{1}", s, age);
		System.out.println(fs);
		Object []o = {"applemango", 10};
		MessageFormat fs2 = new MessageFormat("이름::{0} 나이:{1}");
		System.out.println(fs2.format(o));
	}

}
