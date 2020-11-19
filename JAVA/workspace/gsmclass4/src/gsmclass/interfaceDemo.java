package gsmclass;
interface Phone {
	int VERSION=12;
	void turnOn();
	void turnOff();
}
class Iphone implements Phone {

	@Override
	public void turnOn() {
		System.out.println("Iphone On");
	}

	@Override
	public void turnOff() {
		System.out.println("Iphone Off");
	}
	
}
class Galaxy implements Phone {

	@Override
	public void turnOn() {
		System.out.println("Galaxy On");
	}

	@Override
	public void turnOff() {
		System.out.println("Galaxy Off");
	}
	
}
public class interfaceDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}
