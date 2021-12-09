import java.util.*;
public class Main {
	static int dr[] = {0,-1,0,1};
	static int dc[] = {1,0,-1,0};
	static boolean map[][];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        map = new boolean[101][101];
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			int d = sc.nextInt();//0,1,2,3
			int g = sc.nextInt();
			dragon(x,y,d,g);
		}
        int answer = 0;
        for (int i = 0; i < 100; i++) {
        	for (int j = 0; j < 100; j++) {
    			if(map[i][j] && map[i+1][j] && map[i][j+1] && map[i+1][j+1])
    				answer++;
    		}
		}
        System.out.println(answer);
    }
	private static void dragon(int c, int r, int d, int g) {
		ArrayList<Integer> dir = new ArrayList<Integer>();
		dir.add(d);
		for (int i = 0; i < g; i++) {
			for (int j = dir.size() - 1; j >= 0; j--) {
				dir.add((dir.get(j) + 1) % 4);
			}
		}
		map[r][c] = true;
		for (int i = 0; i < dir.size(); i++) {
			r += dr[dir.get(i)];
			c += dc[dir.get(i)];
			map[r][c] = true;
		}
	}
}