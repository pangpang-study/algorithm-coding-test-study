import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int dPrice = sc.nextInt();//도우 가격
		int tPrice = sc.nextInt();//토핑 가격
		
		int cal = sc.nextInt();//도우의 열량
		int calory[] = new int[n];//토핑의 열량
		for (int i = 0; i < n; i++) {
			calory[i] = sc.nextInt();//토핑의 열량
		}
		Arrays.sort(calory);
		int k = 0;//가격
		int answer = cal / dPrice;
		
		for(int i = n-1; i >= 0; i--) {
			int newPrice = dPrice + tPrice*(k+1);//토핑을 추가한 가격
			if((cal+calory[i]) / newPrice >= answer) {//원래 1원당 가격보다 크면
				k+=1; 
				answer = (cal+calory[i]) / newPrice;
				cal += calory[i];
			}
			else break;
		}
		System.out.println(answer);
	}
}