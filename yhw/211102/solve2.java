import java.util.*;
public class Main {
	static int r,c;
	static char map[][];
	static PriorityQueue<String> pq = new PriorityQueue<String>();
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		r = sc.nextInt();
		c = sc.nextInt();
		map = new char[r][c];
		for (int i = 0; i < r; i++) {
			String com = sc.next();
			for (int j = 0; j < c; j++) {
				map[i][j] = com.charAt(j);
			}
		}
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if(map[i][j] != '#') {
					check(i, j);
				}
			}
		}
		System.out.println(pq.peek());
	}
	private static void check(int i, int j) {
		if(i == 0) {//맨 위
			if(j == 0) {//아래, 오른쪽 다가보자
				goRight(i,j);
				goDown(i,j);
			}
			else if(map[i][j-1] == '#') {//아래, 오른쪽 다가보자
				goRight(i,j);
				goDown(i,j);
			}
			else {//아래만
				goDown(i,j);
			}
		}
		else if(j == 0) {
			if(i == 0) {//아래, 오른쪽 다가보자
				goRight(i,j);
				goDown(i,j);
			}
			else if(map[i-1][j] == '#') {//아래, 오른쪽 다가보자
				goRight(i,j);
				goDown(i,j);
			}
			else {//오른쪽만
				goRight(i,j);
			}
		}
		else {//맨위, 맨왼쪽이 둘다 아닐때
			if(map[i-1][j] == '#')
				goDown(i, j);
			if(map[i][j-1] == '#')
				goRight(i, j);
		}
	}
	private static void goDown(int cr, int cc) {
		String result = "";
		for (int i = cr; i < r;  i++) {
			if(map[i][cc] == '#') break;
			result += map[i][cc];
		}
		if(result.length() >= 2) pq.add(result);
	}
	private static void goRight(int cr, int cc) {
		String result = "";
		for (int i = cc; i < c;  i++) {
			if(map[cr][i] == '#') break;
			result += map[cr][i];
		}
		if(result.length() >= 2) pq.add(result);
	}    
}