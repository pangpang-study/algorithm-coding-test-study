import java.util.*;
public class Main {
	static int input[];//(+ - x /)
	static int num[];
	static int n,max,min;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		num = new int[n];
		int cal[] = new int[4]; 
		
		for (int i = 0; i < n; i++) {
			num[i] = sc.nextInt();
		}
		for (int i = 0; i < 4; i++) {
			cal[i] = sc.nextInt();
		}
		
		int idx = 0;
		max = -1 * Integer.MAX_VALUE; min = Integer.MAX_VALUE;
		
		input = new int[n-1];
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < cal[i]; j++) {
				input[idx++] = i;
			}
		}
		int result[] = new int[n-1];
		comb(0,0,result);
		System.out.println(max + "\n" + min);
	}
	public static void comb(int idx, int flag, int result[]) {
		if(idx == n-1) {
			int sum = num[0];
			for (int i = 0; i < n-1; i++) {
				switch(result[i]) {
				case 0: sum = sum + num[i+1]; break;
				case 1: sum = sum - num[i+1]; break;
				case 2: sum = sum * num[i+1]; break;
				case 3:
					if(sum < 0) {
						sum = Math.abs(sum) / num[i+1];
						sum *= -1;
					}
					else sum = sum / num[i+1]; 
					break;
				}
			}
			if(max < sum) max = sum;
			if(min > sum) min = sum;
			return;
		}
		
		for (int i = 0; i < n-1; i++) {
			if((flag&1<<i) != 0) continue;
			result[idx] = input[i];
			comb(idx+1,flag|1<<i,result);
		}
	}
}