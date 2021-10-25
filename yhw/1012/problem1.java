import java.util.*;
class node{
	char idx;
	node left;
	node right;
	node(char idx){
		this.idx = idx;
	}
}
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		node tree = new node('A');
		
		for (int i = 0; i < n; i++) {
			char parent = sc.next().charAt(0);
			char left = sc.next().charAt(0);
			char right = sc.next().charAt(0);
			search(parent,tree,left,right);
		}
		preorder(tree);
		System.out.println();
		inorder(tree);
		System.out.println();
		postorder(tree);
	}
	public static void search(char target, node root, char left, char right) {
		if(root == null) return;
		if(root.idx == target) {
			node l = new node(left);
			node r = new node(right);
			root.left = l;
			root.right = r;
			return;
		}
		else if(root.idx == '.') 
			return;
		search(target,root.left,left,right);
		search(target,root.right,left,right);
	}
	public static void preorder(node cur) {//전위
		if(cur.idx == '.') 
			return;
		else {
			System.out.print(cur.idx);
		}
		preorder(cur.left);
		preorder(cur.right);
	}
	public static void postorder(node cur) {//후위
		if(cur == null) return;
		postorder(cur.left);
		postorder(cur.right);
		if(cur.idx == '.') 
			return;
		else {
			System.out.print(cur.idx);
		}
	}
	public static void inorder(node cur) {//중위
		if(cur == null) return;
		inorder(cur.left);
		if(cur.idx == '.') 
			return;
		else {
			System.out.print(cur.idx);
		}
		inorder(cur.right);
	}
}