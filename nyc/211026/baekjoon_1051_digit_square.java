import java.io.*;
import java.util.*;

public class Main {
    public static int solution(int[][] board, int n, int m) {
        for (int len = Math.min(n, m)-1; len>0; len--) {
            for (int i=0; i<n-len; i++) {
                for (int j=0; j<m-len; j++) {
                    if ((board[i][j] == board[i+len][j]) && (board[i+len][j] == board[i][j+len])
                            && (board[i][j+len] == board[i+len][j+len]))
                        return (int)Math.pow(len+1, 2);
                }
            }
        }
        return 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] board = new int[N][M];
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                board[i][j] = br.read()-'0';
            }
            br.readLine();
        }
        System.out.println(solution(board, N, M));
    }
}