import java.util.*;
public class Main {
    public static void Solution(String str){
        int tmp;
        for (String s : str.split("")) {
            if (s.equals("(") || s.equals("[")) stack.push(s);
            else if (stack.isEmpty()) return;

            else if (s.equals(")")) {
                tmp = 0;
                while (!stack.isEmpty() && stack.peek().chars().allMatch(Character::isDigit)) {
                    tmp += Integer.parseInt(stack.pop());
                }
                if (!stack.isEmpty() && stack.peek().equals("(")) {
                    stack.pop();
                    if (tmp == 0) stack.push("2");
                    else stack.push(Integer.toString(tmp * 2));
                }
                else return;
            }
            else if (s.equals("]")) {
                tmp = 0;
                while (!stack.isEmpty() && stack.peek().chars().allMatch(Character::isDigit)) {
                    tmp += Integer.parseInt(stack.pop());
                }
                if (!stack.isEmpty() && stack.peek().equals("[")) {
                    stack.pop();
                    if (tmp == 0) stack.push("3");
                    else stack.push(Integer.toString(tmp * 3));
                }
                else return;
            }
        }
    }
    static Stack<String> stack = new Stack<>();
    public static void main(String[] args){
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        Solution(str);
        for (String s : stack) {
            if (s.chars().allMatch(Character :: isDigit)) {
                answer += Integer.parseInt(s);
            }
            else {
                answer = 0;
                break;
            }
        }
        System.out.println(answer);
    }
}