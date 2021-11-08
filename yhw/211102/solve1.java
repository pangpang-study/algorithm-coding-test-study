import java.util.*;
public class Main {
	static int n,m;
	static int map[][];
	static boolean visited[][];
	static int dr[] = {1,-1,0,0};
	static int dc[] = {0,0,-1,1};
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		map = new int[n][m];
		int ch = sc.nextInt();
		for (int i = 0; i < ch; i++) {
			int l_c = sc.nextInt();
			int l_r = sc.nextInt();
			int r_c = sc.nextInt();
			int r_r = sc.nextInt();
			for (int j = l_r; j < r_r; j++) {
				for (int j2 = l_c; j2 < r_c; j2++) {
					map[j][j2] = 1;
				}
			} 
		}
		
		visited = new boolean[n][m];
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
		int count = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if(!visited[i][j] && map[i][j] == 0) {
					count++; 
					pq.add(bfs(i,j));
				}
			}
		}
		System.out.println(count);
		while(!pq.isEmpty())
			System.out.print(pq.poll() + " ");
		
	}
	private static int bfs(int a, int b) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[]{a,b});
		visited[a][b] = true;
		int count = 0;
		while(!q.isEmpty()) {
			int[] cur = q.poll(); count++;
			for (int i = 0; i < 4; i++) {
				int nr = cur[0] + dr[i];
				int nc = cur[1] + dc[i];
				if(nr >= n || nc >= m || nr < 0 || nc < 0) continue;
				if(visited[nr][nc] || map[nr][nc] == 1) continue;
				visited[nr][nc] = true;
				q.add(new int[] {nr,nc});
			}
		}
		return count;
	}    
}