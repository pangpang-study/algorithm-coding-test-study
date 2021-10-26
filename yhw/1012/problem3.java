import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	static boolean finished[];
	static boolean visited[];
	static int people[];
	static int result;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String tc = br.readLine();
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < Integer.parseInt(tc); i++) {
			result = 0;
			int n = Integer.parseInt(br.readLine());
			people = new int[n];
			String s = br.readLine();
			StringTokenizer tok = new StringTokenizer(s);
			for (int j = 0; j < n; j++) {
				people[j] = Integer.parseInt(tok.nextToken()) - 1;
			}
			finished = new boolean[n];
			visited = new boolean[n];
			
			for (int j = 0; j < n; j++) {
				if(!finished[j])
					dfs(j);
			}
			sb.append(n - result + "\n");
		}
		System.out.print(sb);
	}
	private static void dfs(int j) {
		if(visited[j]) {//사이클발견
			finished[j] = true;
			result++;
		}
		visited[j] = true;
		int next = people[j];
		if(!finished[next]) 
			dfs(next);
		finished[j] = true;
	}
}