package gsmclass;
class Square {
	int width;
	int height;
	Square(int width, int height) {
		this.width = width;
		this.height = height;
	}
	@Override
	public boolean equals(Object o) {
		if (o instanceof Square) {
			if (this.width * this.height == ((Square)o).width* ((Square)o).height) {
				return true;
			}
			else {
				return false;
			}
		} else {
			return false;
		}
	}
}
public class ObjectDemo2 {

	public static void main(String[] args) {
		Square s1 = new Square(3,4);
		Square s2 = new Square(3,4);
		System.out.println(s1.equals(s2));

	}

}
