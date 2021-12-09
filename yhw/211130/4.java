import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        
        for (int i = 0; i < tc; i++) {
        	int answer = 0;
			int stx = sc.nextInt();
			int sty = sc.nextInt();
			int endx = sc.nextInt();
			int endy = sc.nextInt();
			
			int n = sc.nextInt();
			for (int j = 0; j < n; j++) {
				int x = sc.nextInt(); int y = sc.nextInt();
				int r = sc.nextInt();
				
				int d1 = (x-stx)*(x-stx) + (y-sty)*(y-sty);
				int d2 = (x-endx)*(x-endx) + (y-endy)*(y-endy);
				
				if((r * r) <= d1 || (r * r) <= d2) {
					if(d1 < r*r) answer++;
					if(d2 < r*r) answer++;
				}
			}
			System.out.println(answer);
		}
    }
}