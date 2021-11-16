import java.io.*;
import java.util.*;


public class Main {
    public static boolean isBudgetOverflow(int upperbound) {
        int answer = 0;
        for (Integer e : budgets) {
            if (e < upperbound) answer += e;
            else answer += upperbound;
        }
        return answer > total;
    }

    public static int solution() {
        if (Arrays.stream(budgets).sum() <= total) {
            return Arrays.stream(budgets).max().getAsInt();
        }

        int start = 0, end = INF, answer = 0;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (isBudgetOverflow(mid))
                end = mid - 1;
            else {
                answer = mid;
                start = mid + 1;
            }
        }
        return answer;
    }

    static int[] budgets;
    static int total;
    static int INF = 100000;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());

        budgets = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            budgets[i] = Integer.parseInt(st.nextToken());
        }
        total = Integer.parseInt(br.readLine());

        System.out.println(solution());
    }
}