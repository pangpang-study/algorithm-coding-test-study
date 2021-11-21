import java.io.*;
import java.util.*;

public class Main {
    public static boolean[] CheckNum(int x, int y) {
        boolean[] check = new boolean[10];
        check[0] = true;
        for (int i=0; i<9; i++) {
            check[board[x][i]] = true;
            check[board[i][y]] = true;
        }
        for (int i = (x/3)*3; i<(x/3)*3 + 3; i++) {
            for (int j = (y/3)*3; j<(y/3)*3 + 3; j++) {
                check[board[i][j]] = true;
            }
        }
        return check;
    }

    public static void Sudoku(int depth) {
        if (empty.size() == depth) {
            for (int i=0; i<9; i++) {
                for (int j=0; j<9; j++) {
                    System.out.print(board[i][j]);
                }
                System.out.println();
            }
            System.exit(0);
        }

        int x = empty.get(depth)[0];
        int y = empty.get(depth)[1];
        int num = 0;
        for (boolean f : CheckNum(x, y)) {
            if (!f) {
                board[x][y] = num;
                Sudoku(depth+1);
                board[x][y] = 0;
            }
            num ++;
        }
    }

    static int[][] board = new int[9][9];
    static ArrayList<Integer[]> empty = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i=0; i<9; i++) {
            String tmp = br.readLine();
            for (int j=0; j<9; j++) {
                board[i][j] = tmp.charAt(j) - '0';
            }
        }

        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (board[i][j] == 0) {
                    empty.add(new Integer[]{i, j});
                }
            }
        }
        Sudoku(0);
    }
}