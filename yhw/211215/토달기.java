import java.util.*;
public class Main {
	static String answer = "";
	static int len = 0;
	static HashSet<String> letters;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String letter = sc.next();//첫 단어
		letters = new HashSet<String>();
		for (int i = 0; i < n; i++) {
			String input = sc.next();
			letters.add(input);
			len = Math.max(len, input.length());
		}
		bfs(letter);
		System.out.println(answer);
	}
	private static void bfs(String letter) {
		Queue<String> q = new LinkedList<String>();
		q.add(letter);
		HashSet<String> visited = new HashSet<String>();
		visited.add(letter);
		answer = letter;
		
		while(!q.isEmpty()) {
			String cur = q.poll();
			
			if(!letters.contains(cur) || cur.length() > len) 
				continue;//없는단어 or 사전에 없는 단어
			
			for(int i = 0; i<26; i++) {
				char alp = 'a'; alp += i;
				for (int j = 0; j <= cur.length(); j++) {//맨 앞부터 맨 끝까지
					String nLetter = "";
					nLetter += cur.substring(0,j);
					nLetter += alp;
					nLetter += cur.substring(j,cur.length());
					if(letters.contains(nLetter) && !visited.contains(nLetter)) {
						q.add(nLetter);
						visited.add(nLetter);
						if(answer.length() <= nLetter.length())
							answer = nLetter;
					}
				}
			}
		}
	}
}