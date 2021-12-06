import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String,Double> trees = new HashMap<>();
        String tree = "";
        int count = 0;
        
        while(sc.hasNextLine()) {
        	tree = sc.nextLine();
        	if(trees.get(tree) != null) {
        		double newNum = trees.get(tree) + 1.0;
        		trees.put(tree, newNum);
        	}
        	else {
        		trees.put(tree, 1.0);
        	}
        	count++;
        }
        
        ArrayList<String> sortTree = new ArrayList<String>();
        if(trees.size() > 0) {
	        for (String set : trees.keySet()) {
	        	sortTree.add(set);
			}
	        Collections.sort(sortTree);
	        for (String tr : sortTree) {
	        	double result = trees.get(tr) * 100 / count;
	        	System.out.printf("%s %.4f\n",tr,result);
	        }
        }
    }
}