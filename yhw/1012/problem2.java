import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int d = sc.nextInt();
		int n = sc.nextInt();
		
		int pizza[] = new int[d];
		int idx = 0;
		for (int i = 0; i < d; i++) {
			pizza[i] = sc.nextInt();
			if(i == 0) idx = pizza[i];
			else {
				if(idx > pizza[i]) {idx = pizza[i]; continue;}
				else pizza[i] = idx;
			}
		}
		
		int start = 0;
		int end = d;
		for (int i = 0; i < n; i++) {
			if(end < 0) {System.out.println(0); return; }
			boolean isok = false;
			int num = sc.nextInt();
			
			while(start < end) {
				int mid = (start + end) / 2;
				if(pizza[mid] < num) {
					end = mid;
				}
				else {
					start = mid + 1;
				}
				isok = true;
			}
			start = 0;
			end-=1;
		}
		System.out.println(end + 1);
	}
}