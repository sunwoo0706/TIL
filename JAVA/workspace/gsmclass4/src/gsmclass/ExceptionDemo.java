package gsmclass;

import java.util.Scanner;

public class ExceptionDemo {

	public static void main(String[] args) {
		int n1 , n2;
		// 이 두개의 정수를 입력받아서 몫을 구하는 알고리즘
		Scanner sc = new Scanner(System.in);
		
		try {
			n1 = sc.nextInt();
			n2 = sc.nextInt();
			System.out.println("둘을 나눈 몫은 ::" + (n1 / n2));
		}catch(ArithmeticException e) {
			System.out.println(e);
			System.out.println("0으로는 나눌수 없습니다.");
		}

	}

}
