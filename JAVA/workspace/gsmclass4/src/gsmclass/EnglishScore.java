package gsmclass;

class MathScore implements Comparable<MathScore> {
	String name;
	int score;
	MathScore(String name, int score) {
		this.name = name;
		this.score = score;
	}
	@Override
	public int compareTo(MathScore o) {
		return score > o.score ? 1 : (score<o.score ? -1 : 0);
	}
	public String toString() {
		return name + ", " + score;
	}
}
public class EnglishScore implements Comparable<EnglishScore> {
	String name;
	int score;
	public EnglishScore(String name, int score) {
		this.name = name;
		this.score = score;
	}
	public String toString() {
		return name + ", " + score;
	}
	@Override
	public int compareTo(EnglishScore o) {
		return score > o.score ? 1 : (score<o.score ? -1 : 0);
	}
	static <T extends Comparable> T findBest(T[] a) {
		T best = a[0];
		
		for (int i = 1; i < a.length; i++) {
			if(best.compareTo(a[i])==-1)
				best=a[i];
		}
		return best;
	}
	static <T> T findScore(T[] a, String name) {
		for (int i = 0; i < a.length; i++) {
			if(a[i].toString().substring(0,3).equals(name))
				return a[i];
		}
		return null;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String name = "null";
			EnglishScore[] ea = {new EnglishScore("김삿갓",77), new EnglishScore("장영실",88),new EnglishScore("홍길동",99)};
			MathScore[] ma = {new MathScore("김삿갓",77), new MathScore("장영실",88),new MathScore("홍길동",99)};
			System.out.println("영어 최고 점수는: "+findBest(ea));
			System.out.println("수학 최고 점수는: "+findBest(ma));
			try {
				name = args[0];
				System.out.println("영어 점수: "+ findScore(ea, name));
				System.out.println("수학 점수: "+ findScore(ma, name));
			} catch (Exception e) {
				System.out.println("**명령 인자 없음**");
				System.out.println(e);
			}
			
	}

}
