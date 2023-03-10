package bj_11582;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Try {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuffer sb;

        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        int k = Integer.parseInt(br.readLine());

        String ans;

        for (int i = 1; i <= k; i++) {

            sb = new StringBuffer();

            for (int j = 0; j < a.length; j += Math.pow(2, i)) {
                System.out.println("j: " + j);

                int tmp2[] = Arrays.copyOfRange(a, j, j + (int) Math.pow(2, i));
                Arrays.sort(tmp2);
                System.out.println(Arrays.toString(tmp2));
                sb.append(Arrays.toString(tmp2) + " ");

            }

            if (i == k) {
                ans = sb.toString();
                ans = ans.replace("[", "");
                ans = ans.replace("]", "");
                ans = ans.replace(",", "");
                bw.write(ans);
                bw.flush();
                break;
            }
        }

    }

}
