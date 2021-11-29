import java.util.*;
public class Main {
	static int answer = 0;
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int egg[][] = new int[n][2];
		for (int i = 0; i < n; i++) {
			egg[i][0] = sc.nextInt();//내구도
			egg[i][1] = sc.nextInt();//무게
		}
		BREAK(0,n,egg);
		System.out.println(answer);
	}
	private static void BREAK(int cur, int limit, int [][]egg) {
		if(cur == limit) {
			int cnt = 0;
			for (int i = 0; i < limit; i++) {
				if(egg[i][0] <= 0) cnt++;
			}
			answer = Math.max(cnt, answer);
			return;
		}
		
		if(egg[cur][0] <= 0) {
			BREAK(cur+1,limit,egg);
	        return;
		}
		
		boolean flag = true;
		for (int i = 0; i < limit; i++) {//깨보기
			if(cur == i || egg[i][0] <= 0) continue;
			egg[cur][0] -= egg[i][1];//기준계란
			egg[i][0] -= egg[cur][1];//오른쪽 계란
			flag = false;
			BREAK(cur+1,limit,egg);
			egg[cur][0] += egg[i][1];//기준계란
			egg[i][0] += egg[cur][1];//오른쪽 계란
		}
		if(flag) {
			BREAK(cur+1,limit,egg);
		}
	}
}