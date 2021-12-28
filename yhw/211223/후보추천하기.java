import java.util.*;
class order implements Comparable<order>{
	int num, idx, cost;
	order(int num, int idx, int cost){
		this.num = num;
		this.idx = idx;
		this.cost = cost;
	}
	@Override
	public int compareTo(order o) {
		if(this.cost == o.cost)
			return this.idx - o.idx;
		else
			return this.cost - o.cost;
	}
}
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int per = sc.nextInt();
		
		HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
		HashMap<Integer, Integer> O = new HashMap<Integer, Integer>();
		
		for (int i = 0; i < per; i++) {
			int person = sc.nextInt();
			if(hash.get(person) != null) {
				hash.put(person, hash.get(person)+1);
			}else {
				O.put(person, i);
				if(hash.size() < n) {
					hash.put(person, 1);
				}else {//사진틀이 꽉참
					ArrayList<order> od = new ArrayList<order>();
					for (int num : hash.keySet()) {
						od.add(new order(num,O.get(num),hash.get(num)));
					}
					Collections.sort(od);
					hash.remove(od.get(0).num);
					hash.put(person,1);
					//System.out.println(od.get(0));
				}
			}
		}
		ArrayList<Integer> arr = new ArrayList<Integer>();
		for (int num : hash.keySet()) arr.add(num);
		Collections.sort(arr);
		
		for (int num : arr)
			System.out.print(num + " ");
	}
}