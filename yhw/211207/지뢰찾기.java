import java.util.*;
public class Main {
	static char map[][];
	static int n;
	static int dr[] = {1,-1,0,0,1,-1,1,-1};
	static int dc[] = {0,0,1,-1,1,-1,-1,1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        map = new char[n][n];
        
        for (int i = 0; i < n; i++) {
        	String com = sc.next();
			for (int j = 0; j < n; j++) {
				map[i][j] = com.charAt(j);
			}
		}
        System.out.println(sol());
    }
	private static int sol() {
		int answer = 0;
		for (int i = 1; i < n-1; i++) {
			for (int j = 1; j < n-1; j++) {
				answer += check(i,j);
				answer++;
			}
		}
		return answer;
	}
	private static int check(int r, int c) {
		for (int i = 0; i < 8; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if(nr >= n || nc >= n || nr < 0 || nc < 0) continue;
			if(map[nr][nc] == '0') return -1;
		}
		
		for (int i = 0; i < 8; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if(nr >= n || nc >= n || nr < 0 || nc < 0) continue;
			if(map[nr][nc] > '0' && map[nr][nc] <= '9') {
				map[nr][nc]--;
			}
		}
		return 0;
	}
}