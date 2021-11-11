import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException{
		//Scanner sc = new Scanner(System.in);
		BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));		
		String str = sc.readLine();
		StringTokenizer tok = new StringTokenizer(str," ");
		String st = tok.nextToken();
		String end = tok.nextToken();
		String quit = tok.nextToken();
		tok = new StringTokenizer(st,":");
		int st_m = Integer.parseInt(tok.nextToken());
		int st_s = Integer.parseInt(tok.nextToken());
		tok = new StringTokenizer(end,":");
		int end_m = Integer.parseInt(tok.nextToken());
		int end_s = Integer.parseInt(tok.nextToken());
		tok = new StringTokenizer(quit,":");
		int q_m = Integer.parseInt(tok.nextToken());
		int q_s = Integer.parseInt(tok.nextToken());
		
		HashSet<String> check = new HashSet<String>();
		HashSet<String> already = new HashSet<String>();
		int minLimit = end_m * 60 + end_s;
		int maxLimit = q_m * 60 + q_s;
		int count = 0;
		String command = null;
		while((command = sc.readLine()) != null) {
			tok = new StringTokenizer(command," ");
			String time = tok.nextToken();
			String nick = tok.nextToken();
			tok = new StringTokenizer(time,":");
			
			int min = Integer.parseInt(tok.nextToken());
			int sec = Integer.parseInt(tok.nextToken());
			
			//넣기
			if(st_m > min) check.add(nick);
			else if(st_m == min){
				if(st_s >= sec) {
					check.add(nick);
				}
			}
			
			//체크?
			if(minLimit <= min*60+sec && maxLimit >= min*60+sec) {
				if(check.contains(nick) && !already.contains(nick)) {
					already.add(nick);
					count++;
				}
			}
		}
		System.out.println(count);
	}
}