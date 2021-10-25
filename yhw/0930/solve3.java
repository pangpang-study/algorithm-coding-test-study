import java.util.*;
class node{
	int r,c;
	node(int r, int c){
		this.r = r;
		this.c = c;
	}
}
public class Main {
	static int dr[] = {0,-1,-1,-1,0,1,1,1};
	static int dc[] = {-1,-1,0,1,1,1,0,-1};
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		
		int map[][] = new int[n][n];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				map[i][j] = sc.nextInt();
			} 
		}
		
		Queue<node> cloud = new LinkedList<node>();//구름
		cloud.add(new node(n-1,0));
		cloud.add(new node(n-1,1));
		cloud.add(new node(n-2,0));
		cloud.add(new node(n-2,1));//맨 처음 구름
		
		
		for (int i = 0; i < m; i++) {//마법시전
			int d = sc.nextInt() - 1;//방향
			int s = sc.nextInt();//거리
			boolean visited[][] = new boolean[n][n];
			
			int size = cloud.size();
			for (int j = 0; j < size; j++) {//현재 있는 구름 크기만큼
				node cur = cloud.poll();
				int nr = cur.r + (dr[d] * s%n);
				int nc = cur.c + (dc[d] * s%n);
				//범위 초과시
				if(nr >= n) nr -= n; 
				if(nc >= n) nc -= n;
				if(nr < 0) nr += n; 
				if(nc < 0) nc += n;
				
				cloud.add(new node(nr,nc));//새구름
				map[nr][nc] += 1;
			}
			//4. 대각선 체크
			while(!cloud.isEmpty()){
				node cl = cloud.poll();
				int cloud_cnt = 0;
				for (int j = 0; j < 8; j++) {
					if(j%2 == 1) {
						int nr = cl.r + dr[j];
						int nc = cl.c + dc[j];
						if(nr >= n || nc >= n || nc < 0 || nr < 0) continue;
						if(map[nr][nc] > 0)
							cloud_cnt++;							
					}
				}
				map[cl.r][cl.c] += cloud_cnt;
				visited[cl.r][cl.c] = true;
			}
			
			//5. 구름 넣기
			for (int j = 0; j < n; j++) {
				for (int j2 = 0; j2 < n; j2++) {
					if(!visited[j][j2] && map[j][j2] >= 2) {
						map[j][j2] -= 2;
						cloud.add(new node(j,j2));
					}
				}
			}
		}
		int result = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				result += map[i][j];
			}
		}
		
		
		System.out.println(result);
	}
}