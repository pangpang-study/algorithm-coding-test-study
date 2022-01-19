import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int con[] = new int[2 * n];
		for (int i = 0; i < 2 * n; i++) {
			con[i] = sc.nextInt();
		}
		int time = 0;
		ArrayList<Integer> robot = new ArrayList<Integer>();
		ArrayList<Integer> Nrobot = new ArrayList<Integer>();
		
		while (true) {
			time++;
			//1 회전
			int temp = con[(2 * n) - 1];
			for (int i = 2*n - 1; i > 0; i--) con[i] = con[i - 1];
			con[0] = temp;
						
			boolean visited[] = new boolean[2 * n];
			//회전에따른 로봇 이동시키기
			for (int i = robot.size() - 1; i >= 0; i--) {
				int cur = robot.get(i);
				if(cur + 1 == n - 1) continue;//내리는 위치에 도달
				Nrobot.add(cur + 1);
				visited[cur+1] = true;
			}
			
			robot.clear();
			
			//2
			for (int i = Nrobot.size() - 1; i >= 0 ; i--) {
				int cur = Nrobot.get(i);				
				if(con[(cur + 1) % (2 * n)] > 0 && !visited[(cur + 1) % (2 * n)]) {
					//내구도가 0보다 큼 & 로봇이 없음
					con[(cur + 1) % (2 * n)] -= 1;//내구도 - 1
					visited[cur] = false;
					
					if(cur + 1 == n - 1) continue;//내리는 위치에 도달
					
					visited[(cur + 1) % (2 * n)] = true;
					robot.add((cur + 1) % (2 * n));//로봇의 위치
				}
				else {
					robot.add(cur);
				}
			}
			
			//3
			if(con[0] > 0) {
				con[0] -= 1;
				robot.add(0);
			}
			
			//4
			int cnt = 0;
			for (int i = 0; i < 2 * n; i++) {
				if(con[i] == 0) {
					cnt++;
				}
			}
			if(cnt >= k) break;
			Nrobot.clear();
		}
		System.out.println(time);
	}
}