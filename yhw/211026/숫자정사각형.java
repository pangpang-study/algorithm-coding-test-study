import java.util.*;
public class Main {
	static int max = Integer.MIN_VALUE;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int map[][] = new int[n][m];
		for (int i = 0; i < n; i++) {
			String s = sc.next();
			for (int j = 0; j < m; j++) {
				map[i][j] = s.charAt(j) - '0';
			}
		}
		
		int min = Math.min(n, m);
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				for (int j2 = 0; j2 < min; j2++) {
					if(i+j2 >= n || j+j2 >= m) continue;
					if(check(map[i][j],map[i][j+j2],
							map[i+j2][j],map[i+j2][j+j2])){//네 꼭지점이 같으면
						max = Math.max((j2+1)*(j2+1), max);
					}
				}
			}
		}
		if(max > 0)
			System.out.println(max);
		else
			System.out.println(1);
	}
	private static boolean check(int i, int j, int k, int l) {
		if(i == j && j == k && k == l) return true;
		else return false;
	}
}