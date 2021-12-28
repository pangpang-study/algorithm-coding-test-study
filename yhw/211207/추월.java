import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        HashMap<String, Integer> tunnel = new HashMap<String, Integer>();
        for (int i = 0; i < n; i++) {
        	String car = sc.next();
        	tunnel.put(car,i);
		}
        ArrayList<Integer> order = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
			order.add(tunnel.get(sc.next()));
		}
        int answer = 0;
        for (int i = 0; i < n; i++) {
        	for(int j = i+1; j < n; j++) {
        		if(order.get(i) > order.get(j)) {
        			answer++;
        			break;
        		}
        	}
		}
        System.out.println(answer);
    }
}