import java.io.*;
import java.util.*;


public class Main {
    public static void floyd(int n) {
        for (int k=1; k<=n; k++) {
            for (int i=1; i<=n; i++) {
                for(int j=1; j<=n; j++) {
                    graph[i][j] = Math.min(graph[i][k] + graph[k][j], graph[i][j]);
                }
            }
        }
    }

    public static int sum(int n, int m, int idx) {
        int answer = 0;
        for (int i=1; i<=n; i++) {
            if (graph[idx][i] <= m) {
                answer += items[i];
            }
        }
        return answer;
    }

    public static int solution(int n, int m) {
        int biggest = 0;
        floyd(n);
        for (int i=1; i<=n; i++) {
            biggest = Math.max(biggest, sum(n, m, i));
        }
        return biggest;
    }

    static int[] items;
    static int[][] graph;
    static int INF = 100000;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        items = new int[N+1];
        graph = new int[N+1][N+1];

        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=N; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        for (int i=0; i<=N; i++) {
            for (int j=0; j<=N; j++) {
                graph[i][j] = INF;
            }
            graph[i][i] = 0;
        }

        for(int i=0; i<R; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int len = Integer.parseInt(st.nextToken());
            graph[a][b] = len;
            graph[b][a] = len;
        }

        System.out.println(solution(N, M));
    }
}