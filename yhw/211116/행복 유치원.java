import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		int arr[] = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		int diff[] = new int[n-1];
		for (int i = 1; i < n; i++) {
			diff[i-1] = arr[i] - arr[i-1];
		}
		Arrays.sort(diff);
		int answer = 0;
		for (int i = 0; i < n-k; i++) {
			answer += diff[i];
		}
		System.out.println(answer);
	}
}