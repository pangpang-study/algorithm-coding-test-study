import java.util.*;
class shortPath implements Comparable<shortPath>{
	int r,c,cost;
	public shortPath(int r, int c, int cost) {
		this.r = r;
		this.c = c;
		this.cost = cost; 
	}
	@Override
	public int compareTo(shortPath o) {
		return this.cost - o.cost;
	}
}
public class Main {
	static int n,m;
	static int map[][];
	static int pass[][];
	static HashMap<Integer, String> target;
	static HashSet<String> visit;
	static int dr[] = {1,-1,0,0};
	static int dc[] = {0,0,1,-1};
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		int fuel = sc.nextInt();
		
		map = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				map[i][j] = sc.nextInt();
			}
		}
		int r = sc.nextInt()-1; int c = sc.nextInt()-1;//택시 시작위치
		
		pass = new int[n][n];
		target = new HashMap<Integer, String>();
		visit = new HashSet<String>();
		
		for (int i = 0; i < m; i++) {
			pass[sc.nextInt()-1][sc.nextInt()-1] = i+1;
			String position = "";
			position += sc.nextInt() - 1;
			position += sc.nextInt() - 1; 
			target.put(i+1, position);
		}//승객의 위치, 도착 위치
		
		for (int i = 0; i < m; i++) {//모든 승객의 수만큼 반복
			int near[] = bfs(r,c);//가장 가까이있는 승객을 찾자
			if(near[0] == -1 || near[2] > fuel){//연료가 없음
				System.out.println(-1); return;
			}
			
			fuel -= near[2];
			int dist[] = go(near[3],near[0],near[1]);//승객번호,r,c
			
			if(dist[0] == -1 || dist[2] > fuel){//연료가 없음
				System.out.println(-1); return;
			}			
			fuel -= dist[2];
			fuel += dist[2]*2;
			r = dist[0]; c = dist[1];//택시위치 변경
		}
		System.out.println(fuel);
	}
	private static int[] bfs(int r, int c) {
		Queue<int[]> q = new LinkedList<int[]>();
		boolean visited[][] = new boolean[n][n];
		
		if(pass[r][c] != 0) {
			int tar = pass[r][c]; 
			pass[r][c] = 0;
			return new int[] {r,c,0,tar};
		}
		
		q.add(new int[] {r,c,0});
		visited[r][c] = true;
		ArrayList<shortPath> pos = new ArrayList<>();
		
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			
			for (int i = 0; i < 4; i++) {
				int nr = cur[0] + dr[i];
				int nc = cur[1] + dc[i];
				if(nr >= n || nc >= n || nr < 0 || nc < 0) continue;
				if(visited[nr][nc] || map[nr][nc] == 1) continue;//벽이거나 방문했음
				if(pass[nr][nc] != 0) {//승객이 있을경우
					pos.add(new shortPath(nr,nc,cur[2]+1));
				}else {
					visited[nr][nc] = true;
					q.add(new int[] {nr,nc,cur[2]+1});
				}
			}
		}
		if(pos.size() == 0) return new int[] {-1};//승객을 못찾음
		
		Collections.sort(pos);
		int resultR = pos.get(0).r,resultC = pos.get(0).c;
		int resultCost = pos.get(0).cost;
		
		for (int i = 1; i < pos.size(); i++) {
			
			if(resultCost < pos.get(i).cost) break;
			
			if(pos.get(i).r == resultR) {//행이 같으면
				if(pos.get(i).c < resultC) {//열이 더 작은애
					resultR = pos.get(i).r;
					resultC = pos.get(i).c;
				}
			}else if(pos.get(i).r < resultR) {//행이 더 작은애
				resultR = pos.get(i).r;
				resultC = pos.get(i).c;
			}
		}
		
		int tar = pass[resultR][resultC];
		pass[resultR][resultC] = 0;
		return new int[] {resultR,resultC,resultCost,tar};
	}
	private static int[] go(int tar,int r, int c) {
		Queue<int[]> q = new LinkedList<int[]>();
		boolean visited[][] = new boolean[n][n];
		
		
		q.add(new int[] {r,c,0});
		visited[r][c] = true;
		String check = target.get(tar);
		String tmp = ""; tmp += r; tmp += c;
		
		if(check.equals(tmp) && !visit.contains(tar)) {//도착지점일 경우
			tmp = ""; tmp += tar;
			visit.add(tmp);
			return new int[] {r,c,0};				
		}
		
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			
			for (int i = 0; i < 4; i++) {
				int nr = cur[0] + dr[i];
				int nc = cur[1] + dc[i];
				if(nr >= n || nc >= n || nr < 0 || nc < 0) continue;
				if(visited[nr][nc] || map[nr][nc] == 1) continue;//벽이거나 방문했음
				String temp = ""; temp += nr; temp += nc;
				if(check.equals(temp) && !visit.contains(tar)) {//도착지점일 경우
					temp = ""; temp += tar;
					visit.add(temp);
					return new int[] {nr,nc,cur[2] + 1};				
				}else {
					visited[nr][nc] = true;
					q.add(new int[] {nr,nc,cur[2]+1});
				}
			}
		}
		return new int[] {-1};
	}
}