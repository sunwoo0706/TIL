package gsmclass;
class Sta<T>{
	int p;
	Object []arr;
	Sta(){
		p = 0;
		arr = new Object[10];
	}
	public void push(T data) {
		if (p == 10) {
			return;
		}
		arr[p] = data;
		p++;
	}
	public T pop() {
		if(p == 0)
			return null;
		--p;
		return ((T) arr[p]);
	}
}
public class GenericDemo3 {

	public static void main(String[] args) {
		Sta<Integer> s = new Sta<Integer>();
		s.push(10);
		s.push(20);
		s.push(30);
		for (int i = 0; i < 3; i++) {
			System.out.println(s.pop());
		}
	}

}
