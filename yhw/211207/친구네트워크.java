import java.util.*;
public class Main {
	static int parent[];
	static int count[];
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		parent = new int[200002];
		count = new int[200002];
		
		StringBuilder sb = new StringBuilder();
		
		//친구 네트워크 입력받기
		for (int i = 0; i < n; i++) {
			int f = sc.nextInt();
			
			for (int j = 1; j <= f*2; j++) {
				parent[j] = j;
			}
			
			int nodeNum = 0;
			HashMap<String, Integer> map = new HashMap<String, Integer>();
			count = new int[200002];
			
			for(int j = 0; j < f; j++) {
				String fr1 = sc.next();
				String fr2 = sc.next();
				
				if(!map.containsKey(fr1))map.put(fr1, ++nodeNum);
				if(!map.containsKey(fr2))map.put(fr2, ++nodeNum);
				
				int node1=map.get(fr1);
				int node2=map.get(fr2);
				
				if(union(node1,node2))
					sb.append(Math.max(count[node1],count[node2]) + "\n");
			}
		}
		
		System.out.print(sb);
	}
	public static boolean union(int a, int b) {
		int ra = find(a);
		int rb = find(b);
		
		if(ra == rb) {
			int max = Math.max(count[ra], count[rb]);
			count[ra] = max;
			count[rb] = max;
			count[a] = max;
			count[b] = max;
			return true;
		}
		else {
			if(ra > rb)
				parent[ra] = rb;
			else
				parent[rb] = ra;
			
			boolean isOk = false;
			
			if(count[a] != 0 && count[b] != 0) {
				//친구 네트워크가 둘다 존재 할 경우
				int sum = Math.max(count[ra], count[a]) + Math.max(count[rb], count[b]);
				count[ra] = sum;
				count[rb] = sum;
				count[a] = sum;
				count[b] = sum;
			}
			else if(count[a] != 0 || count[b] != 0) {
				//둘중에 하나는 새로들어온 친구
				int sum = Math.max(count[ra], count[a]) + Math.max(count[rb], count[b]) + 1;
				count[ra] = sum;
				count[rb] = sum;
				count[a] = sum;
				count[b] = sum;
				isOk = true;
			}
			
			//둘다 0일경우에만 2로 초기화해주기 위해서
			if(count[a] == 0 && isOk == false) {
				count[a]=2; count[ra]=2;
			}
			if(count[b] == 0 && isOk == false) { 
				count[b]=2; count[rb]=2;
			}
			
			return true;
		}
	}
	public static int find(int a) {
		if(a == parent[a])return a;
		else return parent[a] = find(parent[a]);
	}
}