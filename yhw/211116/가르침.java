import java.util.*;
public class Main {
	static int k,n;
	static char []selectAlp;
	static HashSet<Character> hs, hashCheck[];
	static int max = 0;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		hs = new HashSet<Character>();//antic 담아놓음
		hs.add('a');hs.add('n');hs.add('t');hs.add('i');hs.add('c');//얘낸 무조건 있어야함
		
		n = sc.nextInt();
		k = sc.nextInt();
		
		if(k < 5) System.out.println(0);//어차피 5보다 작은 단어를 가르칠 수 있으면 아무것도 못배움
		else {//배울 수 있음
			HashSet<Character> hash = new HashSet<Character>();
			hashCheck = new HashSet[n];
			for (int i = 0; i < n; i++) {
				String word = sc.next();
				hashCheck[i] = new HashSet<Character>();
				for(int j = 0; j < word.length(); j++) {
					if(!hs.contains(word.charAt(j))) {
						hash.add(word.charAt(j));
						hashCheck[i].add(word.charAt(j));
					}
				}
			}
			int size = k - 5;//조합 뽑을 수 있는 수
			selectAlp = new char[hash.size()]; 
			int index = 0;
			for(char c : hash) selectAlp[index++] = c;
			if(hash.size() > size)
				comb(0,0,size,new int[size],hash.size());
			else
				max = n;
			System.out.println(max);
		}
	}

	private static void comb(int idx, int cnt, int size, int[] input, int limit) {
		 if(cnt == size) {
			 
			int answer = 0;
			
			for (int i = 0; i < n; i++) {
				int answerCount = 0;
				for (int j = 0; j < input.length; j++) {
					if(hashCheck[i].contains(selectAlp[input[j]])) {
						answerCount++;
					}
				}
				if(answerCount == hashCheck[i].size())//단어 가르칠수 있음!
					answer++;
			}
			max = Math.max(answer, max);
			return;
		 }
		 for (int i = idx; i < limit; i++) {
			input[cnt] = i;
			comb(i+1,cnt+1,size,input,limit);
		}
		
	}
}