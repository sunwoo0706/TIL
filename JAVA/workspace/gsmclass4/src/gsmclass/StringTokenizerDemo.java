package gsmclass;

import java.util.StringTokenizer;

public class StringTokenizerDemo {

	public static void main(String[] args) {
		String s = "Good morning";
		StringTokenizer st = new StringTokenizer(s, " ");
		System.out.println(st.countTokens());
		int n = st.countTokens();
		for (int i = 0; i < n; i++) {
			System.out.println(st.nextToken());
		}
	}
	
}
