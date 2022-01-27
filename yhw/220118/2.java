import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		int result = 0;
		int x = 0; int y = 0;
		out : for (int i = 0; i < str.length(); i++) {
			int stIdx = i;
			int endIdx = str.length()-1;
			x = i;
			if((endIdx - stIdx + 1) % 2 == 0) {//짝수
				for (int j2 = stIdx, j3 = endIdx; j2 < endIdx; j2++,j3--) {
					if(str.charAt(j2) != str.charAt(j3)) {//양끝이 다름
						break;
					}else {//양끝이 같음
						if(j2 + 1 == j3) break out;
					}
				}
			}
			else {
				for (int j2 = stIdx, j3 = endIdx; j2 <= endIdx; j2++,j3--) {
					if(str.charAt(j2) != str.charAt(j3)) {//양끝이 다름
						break;
					}else {//양끝이 같음
						if(j2 == j3) break out;
					}
				}
			}
		}
		
		if(x == 0)
			System.out.println(str.length());
		else
			System.out.println(x + str.length());//팰린드롬의 좌표
	}
}