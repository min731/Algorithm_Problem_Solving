package bj_11729;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    static String move(int n, int x, int y, String ans) throws IOException {

        if (n > 0) {
            ans = move(n - 1, x, 6 - x - y, ans);
            ans += (x + " " + y + "\n");
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
            ans = move(n - 1, 6 - x - y, y, ans);
        }
        return ans;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String ans = "";
        int cnt = 0;

        int n = Integer.parseInt(br.readLine());

        ans = move(n, 1, 3, ans);

        char blank = ' ';
        for (int i = 0; i < ans.length(); i++) {
            char line = ans.charAt(i);
            if (line == blank) {
                cnt++;
            }
        }

        bw.write(cnt + "\n");
        bw.write(ans);
        bw.flush();
    }

}