import java.io.*;

public class Main {
    public static int turn(int direction, String cmd) {
        if (cmd.equals("L")) {
            direction -= 1;
            if (direction < 0) direction = 3;
        }
        else {
            direction += 1;
            if (direction > 3) direction = 0;
        }
        return direction;
    }

    public static int solution(String cmd) {
        int d = 0, x = 0, y = 0;
        int maxX = 0, minX = 0, maxY = 0, minY = 0;
        for (String c : cmd.split("")) {
            if (c.equals("F")) {
                x += dx[d];
                y += dy[d];
            }
            else if (c.equals("B")) {
                x -= dx[d];
                y -= dy[d];
            }
            else d = turn(d, c);
            maxX = Math.max(maxX, x);
            maxY = Math.max(maxY, y);
            minX = Math.min(minX, x);
            minY = Math.min(minY, y);
        }
        return (maxX - minX) * (maxY - minY);
    }

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t=0; t<T; t++) {
            String cmd = br.readLine();
            System.out.println(solution(cmd));
        }
    }
}