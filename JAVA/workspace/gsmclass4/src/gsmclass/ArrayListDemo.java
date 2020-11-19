package gsmclass;

import java.util.ArrayList;

public class ArrayListDemo {

	public static void main(String[] args) {
		ArrayList<Integer> arr = new ArrayList<Integer>();
		arr.add(1);
		arr.add(2);
		arr.add(3);
		
		System.out.println(arr.get(1));
		System.out.println(arr.size());
		arr.add(4);
		System.out.println(arr.size());
		arr.remove(1);
		System.out.println(arr.size());
		
		for (int i = 0; i < arr.size(); i++) {
			System.out.println(arr.get(i));
		}
		
		ArrayList<Double> arr2 = new ArrayList<>();
		arr2.add(3.14);
	}

}
