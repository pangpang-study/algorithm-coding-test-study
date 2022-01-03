import java.util.*;
public class Main {
	static int l,c;
	static ArrayList<String> result = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        l = sc.nextInt();
        c = sc.nextInt();
        
        ArrayList<Character> ja = new ArrayList<Character>();
        ArrayList<Character> mo = new ArrayList<Character>();
        
        for (int i = 0; i < c; i++) {
			char alp = sc.next().charAt(0);
			if(alp == 'a' || alp == 'e' || alp == 'i' || alp == 'o' || alp == 'u')
				mo.add(alp);
			else
				ja.add(alp);
		}
        
        for (int i = 1; i <= mo.size(); i++) {
        	if(c - i >= 2)//자음의 개수를 2개이상 뽑을 수 있을때
        		comb(0,0,mo,ja,new char[i],i);
		}
        Collections.sort(result);
        for(String num: result)
        	System.out.println(num);
	}
    private static void comb_ja(int idx, int cnt, ArrayList<Character> ja, char[] input, char[] output, int size) {
		if(idx == size) {
			char[] temp = new char[input.length + output.length];
			int count = 0;
			for (int i = 0; i < input.length; i++) {
				temp[count++] = input[i];
			}
			for (int i = 0; i < output.length; i++) {
				temp[count++] = output[i];
			}
			Arrays.sort(temp);
			String in = "";
			for (int i = 0; i < temp.length; i++) in += temp[i];
			result.add(in);
			return;
		}
		
		for (int i = cnt; i < ja.size(); i++) {
			input[idx] = ja.get(i);
			comb_ja(idx+1,i+1,ja,input,output,size);
		}
	}
	private static void comb(int idx, int cnt, ArrayList<Character> mo, ArrayList<Character> ja, char[] input, int size) {
		if(idx == size) {
			for (int i = 2; i <= ja.size(); i++) {
				if(i + size == l)
					comb_ja(0,0,ja,new char[i],input,i);
			}
			return;
		}
		
		for (int i = cnt; i < mo.size(); i++) {
			input[idx] = mo.get(i);
			comb(idx+1,i+1,mo,ja,input,size);
		}
	}
}