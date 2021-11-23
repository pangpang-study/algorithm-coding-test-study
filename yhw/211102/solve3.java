import java.util.*;
public class Main {
	static int n,m;
	static int map[][];
	static int result[][];
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
        map = new int[n][m]; result = new int[n][m];
		for (int i = 0; i < n; i++) {
			String com = sc.next();
			for (int j = 0; j < m; j++) {
				map[i][j] = com.charAt(j) - '0';
			}
		}
		for (int i = 0; i < n; i++) {
			String com = sc.next();
			for (int j = 0; j < m; j++) {
				result[i][j] = com.charAt(j) - '0';
			}
		}
        
		if(n < 3 || m < 3) {
            for (int i = 0; i < n; i++) {
			    for (int j = 0; j < m; j++) {
				    if(map[i][j] != result[i][j]) {
					    System.out.println(-1);
					    return;
				    }
			    }
		    }
            System.out.println(0); return;
        }
        
		int cnt = 0;
		
		for (int i = 0; i < n-2; i++) {
			for (int j = 0; j < m-2; j++) {
				//맨 왼쪽 위만 비교해서 같으면 넘어가고 다르면 flip
				if(map[i][j] != result[i][j]) {
					flip(i,j); cnt++;
				}
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if(map[i][j] != result[i][j]) {
					System.out.println(-1);
					return;
				}
			}
		}
		System.out.println(cnt);
	}
	public static void flip(int r, int c) {
		for (int i = r; i < r+3; i++) {
			for (int j = c; j < c+3; j++) {
				map[i][j] = map[i][j]==0?1:0;
			}
		}
	}
}