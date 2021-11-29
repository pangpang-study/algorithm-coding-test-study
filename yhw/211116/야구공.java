import java.util.*;
public class Main {
	static int answer = 0;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int input[][] = new int[n][9];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < 9; j++) {
				input[i][j] = sc.nextInt();
			}
		}
		mix(0,0,new int[8],input);
		System.out.println(answer);
	}

	private static void mix(int idx, int flag, int[] order,int [][]input) {
		if(idx == 8) {
			int baseball[] = new int[9];
			int num = 0;
			for (int i = 0; i < 9; i++) { 
				if(i==3) continue;
				baseball[i] = order[num++] + 1;
			}
			int first = 0;
			int hit = baseball[first];//맨 첫번째 타자
			int score = 0;
			for (int i = 0; i < input.length; i++) {//n이닝
				int outcount = 0;
				//Queue<Integer> q = new LinkedList<>();
				int b1,b2,b3; b1 = b2 = b3 = 0; 
				while(outcount != 3) {
					switch(input[i][hit]) {
					case 0:
						outcount++;
						break;
					case 1:
//						if(q.isEmpty()) q.add(1);
//						else {
//							for (int j = 0,size = q.size(); j < size; j++) {
//								int now = q.poll();
//								if(now == 3) score++;
//								else q.add(now+1);
//							}q.add(1);
//						}
						if(b3 == 1) { b3 = 0; score++;}
						if(b2 == 1) { b3 = 1; b2 = 0;}
						if(b1 == 1) { b2 = 1; b1 = 0;}
						b1 = 1;
						break;
					case 2:
//						if(q.isEmpty()) q.add(2);
//						else {
//							for (int j = 0,size = q.size(); j < size; j++) {
//								int now = q.poll();
//								if(now >= 2) score++;
//								else q.add(now+2);
//							}q.add(2);
//						}
						if(b3 == 1) { b3 = 0; score++;}
						if(b2 == 1) { b2 = 0; score++;}
						if(b1 == 1) { b3 = 1; b1 = 0;}
						b2 = 1;
						break;
					case 3:
//						if(q.isEmpty()) q.add(3);
//						else {
//							while(!q.isEmpty()) {
//								q.poll();
//								score++;
//							}q.add(3);
//						}
						if(b3 == 1) { b3 = 0; score++;}
						if(b2 == 1) { b2 = 0; score++;}
						if(b1 == 1) { b1 = 0; score++;}
						b3 = 1;
						break;
					case 4:
//						while(!q.isEmpty()) {
//							q.poll();
//							score++;
//						}score++;
						if(b3 == 1) { b3 = 0; score++;}
						if(b2 == 1) { b2 = 0; score++;}
						if(b1 == 1) { b1 = 0; score++;}
						score++;
						break;
					}
					if(first == 8) {
						first = 0; hit = baseball[first]; 
					}
					else hit = baseball[++first];
				}
			}
			answer = Math.max(answer, score);
			return;
		}
		for (int i = 0; i < 8; i++) {
			if((flag&1<<i) != 0) continue;
			order[idx] = i;
			mix(idx+1,flag|1<<i,order,input);
		}
		
	}
}