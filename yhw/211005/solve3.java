import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int dp[] = new int[n+1];
		int vip = sc.nextInt();
		ArrayList<Integer> seat = new ArrayList<Integer>();
		for (int i = 0; i < vip; i++) {
			seat.add(sc.nextInt());
		}
		dp[0] = 1;
		dp[1] = 1;
		for (int i = 2; i <= n; i++) {
			dp[i] = dp[i-1] + dp[i-2];
		}
		int ans = 1;
		int curVipSeat = 0;
		//dp[3] * dp[2] * dp[2] - 예시의 4,7이 vip석인경우의 순열임
		for (int i = 0; i < vip; i++) {
			ans *= dp[seat.get(i)-curVipSeat-1];
			curVipSeat = seat.get(i);
		}
		ans *= dp[n-curVipSeat];
		System.out.println(ans);
	}
}