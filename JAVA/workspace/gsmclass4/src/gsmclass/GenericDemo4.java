package gsmclass;
// 제네릭 메서드

public class GenericDemo4 { // Outer클래스 & 외부클래스
	static class Utils { // inner 클래스 & 내부 클래스
		public static <T> void showArray(T[] arr) {
			for (T t: arr) {
				System.out.println(t);
			}
		}
	}
	public static void main(String[] args) {
		Integer [] ia = {1,2,3,4,5};
		Utils.showArray(ia);
		Character [] ca = {'H','e','l','l','o'};
		Utils.showArray(ca);
	}

}
