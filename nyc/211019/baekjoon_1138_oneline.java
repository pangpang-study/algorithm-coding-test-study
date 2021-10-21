import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> people = new ArrayList<>();
        LinkedList<Integer> result = new LinkedList<>();

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            people.add(Integer.parseInt(st.nextToken()));
        }

        result.add(N);
        for (int i=N-2; i>=0; i--) {
            int idx = 0;
            for (Integer r : result) {
                if (idx == people.get(i)) break;
                if (r > i+1) idx++;
            }
            result.add(idx, i+1);
        }

        for (Integer r : result) {
            System.out.print(r + " ");
        }
    }
}