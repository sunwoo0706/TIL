package gsmclass;
class Span<K, V> {
	private K key;
	private V value;
	Span(K key, V value) {
		this.key = key;
		this.value = value;
	}
	public K getKey() {
		return key;
	}
	public V getValue() {
		return value;
	}
}
public class GenericDemo2 {

	public static void main(String[] args) {
		Span<String, Integer> s = new Span<String, Integer>("Á¤¹ÎÇõ", 18);
		
		System.out.println("ÀÌ¸§ ::"+s.getKey()+" ³ªÀÌ ::"+s.getValue());
		
		Span<String, Double> s2 = new Span<>("Á¤¹ÎÇõ", 185.5);
		
		System.out.println("ÀÌ¸§ ::"+s2.getKey()+" ³ªÀÌ ::"+s2.getValue());
	}

}
