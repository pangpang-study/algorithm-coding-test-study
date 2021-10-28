import java.io.*;
import java.util.*;

public class Main {
    public static int timeToMillisecond(String time) {
        return Integer.parseInt(time.substring(0, 2))*60 + Integer.parseInt(time.substring(3, 5));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int S, E, Q, count=0;
        String chat;
        HashSet<String> set = new HashSet<>();

        S = timeToMillisecond(st.nextToken());
        E = timeToMillisecond(st.nextToken());
        Q = timeToMillisecond(st.nextToken());

        while((chat = br.readLine()) != null) {
            st = new StringTokenizer(chat, " ");
            int time = timeToMillisecond(st.nextToken());
            String name = st.nextToken();
            if (time <= S) {
                set.add(name);
            }
            else if (E <= time && time <= Q && set.contains(name)) {
                count += 1;
                set.remove(name);
            }
        }
        System.out.println(count);
    }
}