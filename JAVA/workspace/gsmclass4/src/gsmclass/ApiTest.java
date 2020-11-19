package gsmclass;

import java.text.MessageFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.StringTokenizer;

class Car
{
    private String model;
    public Car(String model)
    {
        this.model = model;
    }
    
    @Override
    public String toString() { // getter
        
        return this.model;
        
    }

    @Override
  public boolean equals(Object obj) {

      Car car = (Car)obj;
      return (this.model == car.model );

  }
    
}


public class ApiTest {

    public static void main(String[] args) {

        SimpleDateFormat s = new SimpleDateFormat("MM-dd-yyyy");
        Date d = new Date();
        Car myCar = new Car("그랜저");
        Car yourCar = new Car("그랜저");
        String str = MessageFormat.format("날짜: {0}, 자동차 모델  = [{1}], 운전자 (홍길동)"
                , s.format(d), myCar);
        StringTokenizer st = new StringTokenizer(str, "[|]|,|(|) |="); 
        if(myCar.equals(yourCar)) 
        {
            System.out.println("자동차 모델이 둘 다 "+myCar+"로 동일하다");
        } 
        else 
        {
            System.out.println("내"+myCar+", 너"+yourCar+"로 모델이 다르다.");
        }
        
        while(st.hasMoreTokens())
        {
            System.out.println(st.nextToken());
        }
        
        
        
    }

}
