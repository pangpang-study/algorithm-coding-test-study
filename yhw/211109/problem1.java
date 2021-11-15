import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String l = sc.next();
		String r = sc.next();
		int answer = 0;
		//길이가 다르면 무조건 0
		if(l.length() != r.length()) answer = 0;
		else {
			for (int i = 0; i < l.length(); i++) {
				if(l.charAt(i) == r.charAt(i) && r.charAt(i) == '8')
					answer++;
				else if(l.charAt(i) != r.charAt(i)) break;
			}
		}
		System.out.println(answer);
	}
}