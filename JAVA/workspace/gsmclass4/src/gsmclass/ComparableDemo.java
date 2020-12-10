package gsmclass;
class Nav implements Comparable {
	int n;
	Nav(int n) {
		this.n = n;
	}
	@Override
	public int compareTo(Object o) {
		if (n < ((Nav)o).n)
			return-1;
		else
			return 1;
	}
	
}
public class ComparableDemo {

	public static void main(String[] args) {
		Nav n = new Nav(3);
		Nav n2 = new Nav(4);
		if (n.compareTo(n2) == 1) {
			System.out.println("내가가진 n이 더큼");
		}
		else {
			System.out.println("니가가진 n이 더큼");
		}
	}

}
