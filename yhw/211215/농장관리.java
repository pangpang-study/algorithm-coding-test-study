import java.util.*;
class pos implements Comparable<pos>{
	int r,c,cost;
	pos(int r, int c, int cost){
		this.r = r;
		this.c = c;
		this.cost = cost;
	}
	@Override
	public int compareTo(pos o) {
		return o.cost - this.cost;
	}
}
public class Main {
	static int dr[] = {1,-1,0,0,1,-1,1,-1};
	static int dc[] = {0,0,1,-1,1,-1,-1,1};
	static int map[][];
	static int n,m;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		
		map = new int[n][m];
		ArrayList<pos> list = new ArrayList<pos>();
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				map[i][j] = sc.nextInt();
				list.add(new pos(i,j,map[i][j]));
			}
		}
		
		Collections.sort(list);
		int cnt = 0;
		for (int i = 0; i < list.size(); i++) {
			pos cur = list.get(i);
			if(map[cur.r][cur.c] > 0) {
				map[cur.r][cur.c] = 0;
				count(cur); cnt++;
			}
		}
		System.out.println(cnt);
	}
	private static void count(pos cur) {
		Queue<pos> list = new LinkedList<pos>();
		list.add(cur);
		while(!list.isEmpty()) {
			pos now = list.poll();
			for (int i = 0; i < 8; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];
				
				if(nr >= n || nc >= m || nr < 0 || nc < 0) continue;
				if(map[nr][nc] > 0 && map[nr][nc] <= now.cost) {
					//방문한적 없음 & 산봉우리 조건만족
					list.add(new pos(nr,nc,map[nr][nc]));
					map[nr][nc] = 0;
				}
			}
		}
		
	}
}