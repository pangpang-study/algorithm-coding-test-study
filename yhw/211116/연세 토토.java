import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();//성준이가 가진 마일리지
		int p[] = new int[n];//참여 인원
		ArrayList<Integer> mileage = new ArrayList<>();
		int limit[] = new int[n];//과목당 최대 수강인원
		for (int i = 0; i < n; i++) {
			p[i] = sc.nextInt();
			limit[i] = sc.nextInt();//최대 수강인원
			
			int mile[] = new int[p[i]];
			for (int j = 0; j < p[i]; j++) {
				mile[j] = sc.nextInt();
			}
			Arrays.sort(mile);
			int insert = 1;
			if(p[i] - limit[i] < 0) {//수강인원이 모자람, 마일리지가 0 이상이면 가능
				insert = 1;
			}
			else {//수강인원을 넘어섬
				insert = mile[p[i] - limit[i]];
			}
			mileage.add(insert);
		}
		Collections.sort(mileage);
		int sum = 0;
		int answer = 0;
		for(int numb : mileage) {
			sum += numb;
			if(sum <= m) answer++;
			else break;
		}
		System.out.println(answer);
	}
}