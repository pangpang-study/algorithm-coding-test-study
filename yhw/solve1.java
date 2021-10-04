import java.util.*;
class node{
	int r,c;
	int cost;
	node(int r, int c, int cost){
		this.r = r;
		this.c = c;
		this.cost = cost;
	}
}
public class Main {
	static int dr[] = {1,-1,0,0};
	static int dc[] = {0,0,-1,1};
	static int bam[][];
	static int n,sum;
	static int map[][];
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		map = new int[n][n];
		bam = new int[n][n];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				map[i][j] = sc.nextInt();
				bam[i][j] = 1;
			}
		}
		int result = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				dfs(i,j);
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				result = Math.max(result, bam[i][j]);
			}
		}
		System.out.println(result);
	}
	public static int dfs(int r, int c) {
		if(bam[r][c] != 1) 
			return bam[r][c];
		for (int i = 0; i <4 ; i++) {
			int nr = dr[i] + r;
			int nc = dc[i] + c;
			if(nr >= n || nc >= n || nc < 0 || nr < 0) continue;
			if(map[nr][nc] > map[r][c]) {//들어갈 수 있음
				bam[r][c] = Math.max(dfs(nr,nc) + 1,bam[r][c]);
				dfs(nr,nc);
			}
		}
	return bam[r][c];
	}
}