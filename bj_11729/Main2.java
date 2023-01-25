package bj_11729;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main2 {

    static StringBuilder move(int n, int x, int y, String ans, StringBuilder sb) throws IOException {

        if (n > 0) {
            sb = move(n - 1, x, 6 - x - y, ans, sb);
            sb.append(x + " " + y + "\n");
            // 3,1,3
            // 2,1,2
            // 1,1,3
            // 2,1,2
            // 1,3,2
            // 3,1,3
            // 3,1,3
            // 2,2,3
            // 1,2,1
            // 2,2,3
            // 1,1,3
        }

        if (n > 0) {
            sb = move(n - 1, 6 - x - y, y, ans, sb);
        }
        return sb;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String ans = "";
        int cnt = 0;

        int n = Integer.parseInt(br.readLine());

        sb = move(n, 1, 3, ans, sb);

        char blank = ' ';
        for (int i = 0; i < sb.length(); i++) {
            char line = sb.charAt(i);
            if (line == blank) {
                cnt++;
            }
        }
        System.out.println(cnt);
        System.out.println(sb.toString());
    }

}