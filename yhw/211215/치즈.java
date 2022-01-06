import java.util.*;
public class Main {
	static int n, m;
	static int map[][];
	static boolean visited[][];
	static int dr[] = {1,-1,0,0,};
	static int dc[] = {0,0,1,-1};
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt(); m = sc.nextInt();
		map = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				map[i][j] = sc.nextInt();
			}
		}
		
		int count = n*m;//다 체크했을때 치즈가 없음
		int result = 0;
		while(true) {
			visited = new boolean[n][m];
			int cnt = bfs(0,0);
			if(cnt == count) 
				break;
			else {
				ArrayList<int[]> cheese = new ArrayList<int[]>();
				for(int y = 0; y<n; y++) {
					for(int x = 0; x<m; x++) {
						if(!visited[y][x]) {//외부에 있는 기포가 아닐때
							//1 치즈
							if(map[y][x] == 1) {
								cheese.add(new int[] {y,x});//치즈의 좌표
							}
							//2 내부 기포
							else {
								map[y][x] = -1;
							}
						}
					}
				}
				ArrayList<int[]> delete = new ArrayList<int[]>();
				for(int x = 0; x<cheese.size(); x++) {//치즈 길이만큼
					int [] cur = cheese.get(x);
					if(check(cur[0],cur[1])) {
						delete.add(new int[] {cur[0],cur[1]});
					}
				}
				for(int x = 0; x<delete.size(); x++) {//공기와 접촉한 치즈를 지우자
					int [] cur = delete.get(x);
					map[cur[0]][cur[1]] = 0;
				}
				result++;
			}
		}
		System.out.println(result);
	}
	private static boolean check(int r, int c) {//얘가 한시간뒤에 지워질 치즈놈?
		int count = 0;
		for (int i = 0; i < 4; i++) {
			int nr = r+dr[i];
			int nc = c+dc[i];
			if(nr >= n || nc >= m || nr < 0 || nc < 0) continue;
			if(map[nr][nc] == 0) count++;
		}
		
		return count >= 2;
	}
	private static int bfs(int r, int c) {
		Queue<int[]> q = new LinkedList<int[]>();
		int cnt = 1;
		q.add(new int[] {r,c}); 
		visited[r][c] = true;
		
		while(!q.isEmpty()) {
			int []cur = q.poll();
			for (int i = 0; i < 4; i++) {
				int nr = cur[0] + dr[i];
				int nc = cur[1] + dc[i];
				if(nr >= n || nc >= m || nr < 0 || nc < 0) continue;
				if(visited[nr][nc] || map[nr][nc] == 1) continue;//방문 한적? 치즈?
				visited[nr][nc] = true;
				q.add(new int[] {nr,nc});
				map[nr][nc] = 0; cnt++;
 			}
		}
		return cnt;
	}
}