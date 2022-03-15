import java.util.*;
class position implements Comparable<position>{
	int r,c,dir,cnt;
	boolean mirror;
	public position(int r, int c, int dir, int cnt, boolean mirror) {
		this.r = r; this.c = c; this.dir = dir; this.cnt = cnt; this.mirror = mirror;
	}
	@Override
	public int compareTo(position o) {
		return this.cnt - o.cnt;
	}
	
}
public class Main {
	static int n,answer = (int)1e9;
	static char map[][];
	static int dr[] = {0,0,1,-1};
	static int dc[] = {1,-1,0,0};
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		map = new char[n][n];
		ArrayList<int[]> pos = new ArrayList<int[]>();
		int mirror = 0;
		int stY=0,stX=0;
		for (int i = 0; i < n; i++) {
			String com =  sc.next();
			for (int j = 0; j < n; j++) {
				map[i][j] = com.charAt(j);
				if(map[i][j] == '#') pos.add(new int[] {i,j});
				if(map[i][j] == '!') mirror++;
			}
		}
		nav(pos.get(0)[0],pos.get(0)[1],pos.get(1)[0],pos.get(1)[1],mirror);
		System.out.println(answer);
	}
	private static void nav(int stR, int stC, int endR,int endC, int mirrorCnt) {
		PriorityQueue<position> q = new PriorityQueue<>();
		for (int j = 0; j < 4; j++) q.add(new position(stR,stC,j,0,false));
		boolean visited[][][] = new boolean[n][n][4];
		for (int j = 0; j < 4; j++) visited[stR][stC][j] = true;
		while(!q.isEmpty()) {
			position cur = q.poll();
			if(cur.r == endR && cur.c == endC) {
				answer = cur.cnt;
				return;
			}
			if(cur.mirror) {//거울이 설치된 좌표
				int dir[] = new int[2];
				switch(cur.dir){
					case 0:
						dir[0] = 2; dir[1] = 3;
						break;
					case 1:
						dir[0] = 2; dir[1] = 3;
						break;
					case 2:
						dir[0] = 0; dir[1] = 1;
						break;
					case 3:
						dir[0] = 0; dir[1] = 1;
						break;
				}
				for (int i = 0; i < 2; i++) {
					int nr = dr[dir[i]] + cur.r;
					int nc = dc[dir[i]] + cur.c;
					if(nr >= n || nc >= n || nr < 0 || nc < 0) continue;
					if(map[nr][nc] == '*' || visited[nr][nc][dir[i]]) continue;
					if(map[nr][nc] == '.') {
						//거울이 없는 위치임
						visited[nr][nc][dir[i]] = true;
						q.add(new position(nr, nc, dir[i], cur.cnt, false));
					}else if(map[nr][nc] == '!'){
						//거울이 있는 위치임
						visited[nr][nc][dir[i]] = true;
						q.add(new position(nr, nc, dir[i], cur.cnt,false));
						q.add(new position(nr, nc, dir[i], cur.cnt + 1,true));
					}
					else {
						visited[nr][nc][dir[i]] = true;
						q.add(new position(nr, nc, dir[i], cur.cnt,false));
					}
				}
			}//거울이 설치되지 않은 좌표
				int nr = dr[cur.dir] + cur.r;
				int nc = dc[cur.dir] + cur.c;
				if(nr >= n || nc >= n || nr < 0 || nc < 0) continue;
				if(map[nr][nc] == '*' || visited[nr][nc][cur.dir]) continue;
				if(map[nr][nc] == '.') {
					//거울이 없는 위치임
					visited[nr][nc][cur.dir] = true;
					q.add(new position(nr, nc, cur.dir, cur.cnt, false));
				}else if(map[nr][nc] == '!'){
					//거울이 있는 위치임
					visited[nr][nc][cur.dir] = true;
					q.add(new position(nr, nc, cur.dir, cur.cnt,false));
					q.add(new position(nr, nc, cur.dir, cur.cnt + 1,true));
				}
				else {
					visited[nr][nc][cur.dir] = true;
					q.add(new position(nr, nc, cur.dir, cur.cnt,false));
				}
			}
		}
	}