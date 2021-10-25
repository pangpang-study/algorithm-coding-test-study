import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int map[][] = new int[n][m];
		int rain[] = new int[m];
		
		for (int j = 0; j < m; j++) {
			rain[j] = sc.nextInt();
		}
		
		for (int j = 0; j < m; j++) {
			for (int i = 0; i < n; i++) {
				if(rain[j] + i >= n)
					map[i][j] = 1;
			}
		}

		int count[] = new int[n];
		for (int i = 0; i < n; i++) {
			ArrayList<Integer> cnt = new ArrayList<Integer>();
			boolean addOk = false;
			for (int j = 0; j < m; j++) {
				if(map[i][j] == 1 && cnt.size() == 0) {//1을 처음 만남
					addOk = true;
				}
				else if(map[i][j] == 1 && cnt.size() != 0) {//벽을 만남
					count[i] += cnt.size();
					cnt.clear();
				}
				else if(map[i][j] == 0 && addOk) {//더해줘!
					cnt.add(map[i][j]);
				}
				else
					continue;
			}
		}
		int sum = 0;
		for (int num : count) {
			sum += num;
		}
		
		System.out.println(sum);
	}
}