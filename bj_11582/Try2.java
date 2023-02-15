package bj_11582;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Try2 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuffer sb = new StringBuffer();

        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        int k = Integer.parseInt(br.readLine());

        int [][] ans = new int[n / (int) Math.pow(2, k)][n / (int) Math.pow(2, k)/2];

        for (int i = 1; i <= k; i++) {

            int[][] tmp = new int[n / (int) Math.pow(2, i)][n / (int) Math.pow(2, i)/2];
            int idx = 0;

            for (int j = 0; j < a.length; j += Math.pow(2, i)) {

                int tmp2[] = Arrays.copyOfRange(a, j, j + (int) Math.pow(2, i));
                Arrays.sort(tmp2);
                tmp[idx++] = tmp2;

            }

            if (i == k) {
                ans = tmp;
            }
        }

        for(int i=0;i<ans.length;i++){
            for(int j=0; j<ans[0].length;j++){
                sb.append(ans[i][j]+" ");
            }
        }

        bw.write(sb.toString());
        bw.flush();

    }

}
