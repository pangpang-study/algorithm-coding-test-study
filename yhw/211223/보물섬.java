import java.util.*;
public class Main {
	static int answer = 0;
	static char map[][];
	static int r,c;
	static int dr[] = {1,-1,0,0};
	static int dc[] = {0,0,1,-1};
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		r = sc.nextInt(); c = sc.nextInt();
		map = new char[r][c];
		for (int i = 0; i < r; i++) {
			String str = sc.next();
			for (int j = 0; j < c; j++) {
				map[i][j] = str.charAt(j);
			}
		}
		
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if(map[i][j] == 'L') {//육지일 경우
					int num = bfs(i,j);//시작점
					answer = Math.max(num, answer);
				}
			}
		}
		System.out.println(answer);
	}
	private static int bfs(int y, int x) {
		boolean visited[][] = new boolean[r][c];
		Queue<int []> q = new LinkedList<int[]>();
		q.add(new int[] {y,x,0});
		visited[y][x] = true;
		int max = 0;
		while(!q.isEmpty()) {
			int[]cur = q.poll();
			if(cur[2] > max) 
				max = cur[2];
			
			for (int i = 0; i < 4; i++) {
				int nr = cur[0] + dr[i];
				int nc = cur[1] + dc[i];
				if(nr >= r || nc >= c || nr < 0 || nc < 0) continue;
				if(map[nr][nc] == 'W' || visited[nr][nc]) continue;
				visited[nr][nc] = true;
				q.add(new int[] {nr,nc,cur[2]+1});
			}
		}
		return max;
	}
}