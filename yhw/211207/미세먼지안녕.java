import java.util.*;
class pos{
	int r,c,cost;
	pos(int r,int c,int cost){
		this.r = r;
		this.c = c;
		this.cost = cost;
	}
}
public class Main {
	static int R,C;
	static int map[][];
	static int dr[] = {0,-1,0,1};
	static int dc[] = {1,0,-1,0};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        int T = sc.nextInt();
        
        map = new int[R][C];
        ArrayList<pos> dust = new ArrayList<pos>();//먼지
        int cleaner = -1;
        for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				map[i][j] = sc.nextInt();
				if(map[i][j] == -1 && cleaner == -1)
					cleaner = i;
			}
		}
        for (int tc = 0; tc < T; tc++) {
	        for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					if(map[i][j] != 0 && map[i][j] != -1) 
						dust.add(new pos(i,j,map[i][j]));//미세먼지의 위치
				}
			}	        
	        //확산
	        for (int i = 0; i < dust.size(); i++) {
	        	pos cur = dust.get(i);
	        	int amountOfDust = cur.cost/5;
	        	int cnt = 0;
				for (int j = 0; j < 4; j++) {
					int nr = dr[j] + cur.r;
					int nc = dc[j] + cur.c;
					if(nr >= R || nr < 0 || nc >= C || nc < 0) continue;
					if(map[nr][nc] == -1) continue;
					
					map[nr][nc] += amountOfDust; cnt++;
				}
				map[cur.r][cur.c] -= amountOfDust * cnt;
			}
	        
	        //공기청정 위 on
	        up(cleaner,0);
	        //공기청정 아래 on
	        down(cleaner+1,0);
        }
        int answer = 0;
        for (int i = 0; i < R; i++) {
        	for (int j = 0; j < C; j++) {
        		if(map[i][j] == 0 || map[i][j] == -1) continue; 
        		answer += map[i][j]; 
        	}
        }
        System.out.println(answer);
	}
    public static void up(int tr,int tc) {//반 시계방향
    	//아래
    	for (int i = tr-1; i > 0; i--) 
			map[i][0] = map[i-1][0];
    	//왼쪽
    	for (int i = 0; i < C -1; i++) 
    		map[0][i] = map[0][i+1];
    	//위
    	for (int i = 0; i < tr; i++) 
    		map[i][C-1] = map[i+1][C-1];
    	//오른쪽
    	for (int i = C-1; i > 1; i--) 
			map[tr][i] = map[tr][i-1];
    	map[tr][1] = 0;
	}
    public static void down(int tr,int tc) {//시계방향
    	//위
    	for (int i = tr + 1; i < R - 1; i++) 
    		map[i][0] = map[i+1][0];
    	//왼쪽
    	for (int i = 0; i < C -1; i++) 
    		map[R-1][i] = map[R-1][i+1];
    	//아래
    	for (int i = R-1; i > tr; i--) 
    		map[i][C-1] = map[i-1][C-1];
    	//오른쪽
    	for (int i = C-1; i > 1; i--) 
			map[tr][i] = map[tr][i-1];
    	map[tr][1] = 0;
    }
}