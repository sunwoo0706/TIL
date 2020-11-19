package gsmclass;

public class Wrapper {

	public static void main(String[] args) {
		// 기본타입 int
		Integer i = new Integer(10); // 박싱
		Integer i2 = Integer.valueOf(5);
		System.out.println(i);
		System.out.println(i2);
		Integer i3 = 20;
		System.out.println(i3);
		
		int i4 = i2.intValue();
		System.out.println(i4);
		int i5 = i3;
		System.out.println(i5);
		double d = 3.15;
		String s = Double.toString(3.14);
				
		Double d2 = Double.parseDouble("3.14");
		System.out.println(d2);
	}

}


























