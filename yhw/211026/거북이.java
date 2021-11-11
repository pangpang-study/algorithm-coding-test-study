import java.util.*;
public class Main {
	static int dr[] = {-1,0,1,0};
	static int dc[] = {0,-1,0,1};
	static int minX,minY,maxX,maxY;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			String s = sc.next();
			
			minX = 0;minY = 0;
			maxX = 0;maxY = 0;
			
			int dir = 0;//방향
			int pos[] = {0,0};//위치
			for (int j = 0; j < s.length(); j++) {
				switch (s.charAt(j)){
					case 'F': {
						pos[0] += dr[dir];
						pos[1] += dc[dir];
						break;
					}
					case 'B': {
						pos[0] -= dr[dir];
						pos[1] -= dc[dir];
						break;
					}
					case 'L': {
						dir += 1;
						if(dir >= 4) dir -= 4;
						if(dir < 0) dir += 4;
						break;
					}
					case 'R': {
						dir -= 1;
						if(dir >= 4) dir -= 4;
						if(dir < 0) dir += 4;
						break;
					}
				}
				check(minX,minY,maxX,maxY,pos);
			}
			int result = cal(minX,minY,maxX,maxY);
			System.out.println(result);
		}
	}
	private static int cal(int minX, int minY, int maxX, int maxY) {
		return (maxY-minY)*(maxX-minX);
	}
	private static void check(int a, int b, int A, int B, int[] pos) {
		if(pos[0] < a) minX = pos[0];
		if(pos[0] > A) maxX = pos[0];
		if(pos[1] < b) minY = pos[1];
		if(pos[1] > B) maxY = pos[1];
	}
}