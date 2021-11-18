import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();//최대 수색범위
		int r = sc.nextInt();
		int item[] = new int[n+1];
		int map[][] = new int[n+1][n+1];
		
		for (int i = 1; i <= n; i++) item[i] = sc.nextInt();
		
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= n; j++) {
				map[i][j] = (int)1e9;//나머지놈 무한대
				if(i == j) map[i][j] = 0;//자기 자신은 0
			}
		}
		
		for (int i = 0; i < r; i++) {//수색 범위
			int from = sc.nextInt();
			int to = sc.nextInt();
			int cost = sc.nextInt();
			map[from][to] = cost;
			map[to][from] = cost;
		}
		
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				for (int j2 = 1; j2 <= n; j2++) {
					map[j][j2] = Math.min(map[j][j2], map[j][i] + map[i][j2]);
				}
			}
		}
		
		int answer = 0;
		for (int i = 1; i <= n; i++) {
			int comp = 0;
			for (int j = 1; j <= n; j++) {
				if(map[i][j] <= m) comp += item[j];
			}
			answer = Math.max(answer, comp);
		}
		System.out.println(answer);
	}
}