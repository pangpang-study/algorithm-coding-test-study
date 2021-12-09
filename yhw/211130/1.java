import java.util.*;
public class Main {
	static int dr[] = {0,0,-1,1};
	static int dc[] = {1,-1,0,0};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int m = sc.nextInt();
        int dicer = sc.nextInt(); int dicec = sc.nextInt();
        
        int k = sc.nextInt(); int map[][] = new int[n][m];
        int command[] = new int[k];
        
        int dice[] = new int[6];//다이스
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++) {
            	map[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < k; i++) 
        	command[i] = sc.nextInt();
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
        	int nr = dicer + dr[command[i]-1];
        	int nc = dicec + dc[command[i]-1];
        	if(nr >= n || nr < 0 || nc >= m || nc < 0) continue;
        	dicer = nr; dicec = nc;//위치 변경
        	int newDice[] = new int[6];
			switch(command[i]-1) {
			case 0://우
				newDice[0] = dice[4];
				newDice[1] = dice[1];
				newDice[2] = dice[5];
				newDice[4] = dice[2];
				newDice[3] = dice[3];
				newDice[5] = dice[0];
				break;
			case 1://좌
				newDice[0] = dice[5];
				newDice[1] = dice[1];
				newDice[2] = dice[4];
				newDice[3] = dice[3];
				newDice[4] = dice[0];
				newDice[5] = dice[2];
				break;
			case 2://상
				newDice[0] = dice[1];
				newDice[1] = dice[2];
				newDice[2] = dice[3];
				newDice[3] = dice[0];
				newDice[4] = dice[4];
				newDice[5] = dice[5];
				break;
			case 3://하
				newDice[0] = dice[3];
				newDice[1] = dice[0];
				newDice[2] = dice[1];
				newDice[3] = dice[2];
				newDice[4] = dice[4];
				newDice[5] = dice[5];
				break;
			}
			//맨 밑면
			dice = newDice;
			if(map[dicer][dicec] == 0) map[dicer][dicec] = dice[2];
			else {
				dice[2] = map[dicer][dicec];
				map[dicer][dicec] = 0;
			}
			sb.append(dice[0] + "\n");//주사위 윗면
		}
        System.out.println(sb);
    }
}