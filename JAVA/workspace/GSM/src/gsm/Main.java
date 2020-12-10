package gsm;

import java.io.IOException;
import java.util.*;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.event.*; // 버튼 이벤트를 시도 하려던 흔적


import javax.swing.JButton;
import javax.swing.JFrame;

public class Main {

	public Main(String[][] farr, int today) {

		Calendar cal = Calendar.getInstance();

		int year1 = cal.get(Calendar.YEAR);
		int mon1 = cal.get(Calendar.MONTH);
		int day1 = cal.get(Calendar.DAY_OF_MONTH);
		int hour = cal.get(Calendar.HOUR_OF_DAY);

		int n = (hour > 19 ? 0 : (hour < 13 ? 1 : 2)); // 시간대에 맞춰 처음 보여지는 화면을 구성

		// 컴포넌트 생성
		JFrame jFrame = new JFrame("GSM");
		JButton btn1 = new JButton("날짜 : " + year1 + "년 " + (mon1 + 1) + "월 " + day1 + "일");
		JButton btn4 = new JButton("made by Goolgae");
		JButton btn5 = new JButton("<HTML><center><h1>" + (n == 0 ? "아침" : (n == 1 ? "점심" : "저녁")) + "</h1>"
				+ farr[today - 1][n] + "</center></HTML>");

		// 컴포넌트를 넣을 컨테이너 구하기
		Container container = jFrame.getContentPane();

		// 컴포넌트를 컨테이너에 추가

		container.add(btn1, BorderLayout.NORTH);
		container.add(btn4, BorderLayout.SOUTH);
		container.add(btn5, BorderLayout.CENTER);

		// 프레임 크기 지정
		jFrame.setSize(400, 400);

		// 프레임 보이기 설정
		jFrame.setVisible(true);

		// 종료 버튼 설정
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) throws IOException {
		int mount = 0; // title을 긁어 왔을때 그 갯수를 측정하는 변수

		// 이번달의 요일 구하는 알고리즘
		// 왜 쓰냐면 주말은 비워야 하기 때문이다. 내가 멍청해서인지는 몰라도 이 알고리즘 밖에는 생각이 나지 않는다.

		Calendar cal = Calendar.getInstance();

		int niceday = cal.get(Calendar.DATE); // 오늘의 날짜를 구분점으로 정하기 위해 지정
		// cal.set(cal.YEAR, year);
		// cal.set(cal.MONTH, month-1); //1월이 0부터 시작하므로 월에서 -1
		cal.set(Calendar.DAY_OF_MONTH, 1); // DAY_OF_MONTH를 1로 설정 (월의 첫날)

		int week = cal.get(Calendar.DAY_OF_WEEK); // 그 주의 요일 반환 (일:1 ~ 토:7)

		// 학교 급식 사이트를 향한 링킹 작업
		Document doc = Jsoup.connect("http://gsm.gen.hs.kr/xboard/board.php?mode=list&tbnum=8").get();
		Elements titles = doc.select(".content"); // 클래스명으로 먹어버리기

		// print all titles in main page
		for (Element e : titles) {
			mount++;
		}

		int day = (mount % 3 == 0 ? mount / 3 : (mount % 3 == 1 ? (mount / 3) + 1 : (mount / 3) + 2)) + 8;
		// System.out.println(day); // 날짜 제대로 나오는지 확인

		String[][] array; // 이차원 배열 생성

		String[] arr2;

		arr2 = new String[mount + 24]; // 일차적으로 정보를 보낼 배열 // 24는 주말에 급식량도 포함한것이다!!

		// 정보 보내기
		int cnt1 = 0; // 반복문에서 배열을 순환시키기 위해!!
		for (Element e : titles) {
			arr2[cnt1] = e.text();
			cnt1++;
		}

		array = new String[day][3]; // 아침 점심 저녁으로 저장하기 위해 day * 3 사이즈로 제작

		// 주말을 거르는 타선
		int[] joolist; // 주말중 토요일을 구한것 넣는 이차원 배열 일요일은 + 1만 해도 되니깐
		int cnt2 = 0; // 반복문에서 배열을 순환시키기 위해!!

		joolist = new int[4];
		for (int restweek = 0; restweek < day; restweek += (restweek == 0 ? 7 - week : 7)) {
			if (restweek != 0) { // 0은 이 달의 첫째날을 가르키기 때문에 무시해줘야 한다.
				joolist[cnt2] = restweek - 1;
				cnt2++;
			}
		}

		// 이제 제일 중요한 배열에 문자를 넣기

		int cnt3 = 0; // 반복문에서 일차원배열과 i값이 수틀려지기 때문에 변수 선언
		for (int i = 0; i < day; i++) {
			for (int j = 0; j < 3; j++) {
				for (int k = 0; k < 4; k++) {
					if ((joolist[k] + 1) == i) {
						array[i][j] = "토요일 주말입니다.";
						array[i + 1][j] = "일요일 주말입니다.";
						i += 2;
					} else {
						array[i][j] = arr2[cnt3];
					}
				}
				cnt3++;
			}
		}
		for (int i = 0; i < day; i++) {
			for (int j = 0; j < 3; j++) {
				if (array[i][j] == null) {
					array[i][j] = "급식 미실시";
				} // \\은 붙이지 않으면 정규표현식 패턴과 관련된 오류가 발생한다고 한다.
				array[i][j] = array[i][j].replaceAll("\\*", "<br>"); // 자바 gui에서 개행을 하려면 html 코드 가 필요하다고 한다! ? 도대체 왜
				array[i][j] = array[i][j].replaceAll("\\(|\\)| |\\.|[0-9]", ""); // 메뉴가 나올때마다 띄어쓰기가 나와 그 점을 보완하였다.
			} // 위 코드는 크롤링 시에 * 가 붙는 걸 없애고 싶어 검색하다가 개행도 할 수 있을까 하는 의미에서 *를 \n으로 변환시켜주는 코드이다.
		} // 난 아무래도 천재인것 같다.

		// 테스트 코드
//		Scanner scan = new Scanner(System.in);
//		System.out.println("날짜를 입력해주세요.");
//		int when = scan.nextInt() - 1;
//		System.out.println("저녁인가요 아님 아침? 점심? 아침 : 1, 점심 : 2, 저녁 : 3");
//		int when2 = scan.nextInt() - 1;
//		
//		System.out.println(array[when][when2]);

		new Main(array, niceday);
	}

}
