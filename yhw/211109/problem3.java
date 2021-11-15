import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int map[] = new int[n];
		for (int i = 0; i < map.length; i++) {
			map[i] = sc.nextInt();
		}
		Arrays.sort(map);
		long money = sc.nextLong();
		long st = 0; long end = map[n-1];
		long answer = 0; long mid = 0;
		while(st <= end) {
			mid = (st + end) / 2;
			long sum = 0;
			for(int numb:map) {//얘가 최대일지...
				if(numb >= mid)sum += mid;
				else sum += numb;
			}
			if(sum <= money) { 
				answer = Math.max(answer, mid);
				st = mid + 1;
			}
			else {
				end = mid - 1;
			}
			
		}
		System.out.println(answer);
	}
}