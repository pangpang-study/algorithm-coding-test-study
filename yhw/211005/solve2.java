import java.util.*;
class node implements Comparable<node>{
	int idx,cost;
	node(int idx, int cost){
		this.idx = idx;
		this.cost = cost;
	}
	public int compareTo(node o) {
		return this.cost - o.cost;
	}
}
public class Main {
	static int t,num;
	static boolean visited[] = new boolean[100001];
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		t = sc.nextInt();
		num = sc.nextInt();
		
		int min = click(n);
		
		if(min != Integer.MAX_VALUE)
			System.out.println(min);
		else
			System.out.println("ANG");
		
	}
	public static int click(int cnt) {
		
		PriorityQueue<node> q = new PriorityQueue<>();
		q.add(new node(cnt,0));
		visited[cnt] = true;
		
		while(!q.isEmpty()) {
			node cur = q.poll();
			if(cur.cost > t) return Integer.MAX_VALUE;
			if(cur.idx == num) {
				return cur.cost;
			}
			for (int i = 0; i < 2; i++) {
				if(i == 0) {//a버튼 클릭
					if(visited[cur.idx + 1]) continue;
					if(cur.idx + 1 > 99999) continue;;
					visited[cur.idx + 1] = true;
					q.add(new node(cur.idx+1,cur.cost+1));
				}else {//b버튼 클릭
					String num = "";
					if(cur.idx * 2 > 99999) continue;;
					num += cur.idx * 2;
					String result = "";
					
					int check = num.charAt(0) - '0';
					if(check - 1 == 0) {
						for (int j = 1; j < num.length(); j++) {
							result += num.charAt(j);
						}
					}
					else {
						if(check - 1 > 0) {
							check = check - 1;
							for (int j = 0; j < num.length(); j++) {
								if(j == 0)
									result += check;
								else result += num.charAt(j);
							}
						}
					}
					int number = -1;
					if(result.equals(""))
						number = 0;
					else
						number = Integer.parseInt(result);
					
					if(visited[number]) continue;
					visited[number] = true;
					q.add(new node(number,cur.cost+1));
				}
			}
		}
		
		return Integer.MAX_VALUE;
	}
}