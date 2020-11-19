package gsmclass;
class School extends Object {
	String name;
	School(String name) {
		this.name = name;
	}
	public String toString() {
		return "우리 학교는 "+this.name;
	}
}
public class ObjectDemo {

	public static void main(String[] args) {
		School s = new School("GSM");
		System.out.println(s.toString());
		// 우리 학교는 GSM
	}

}
