package bj_11582;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Try3 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> list1 = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            list1.add(Integer.parseInt(st.nextToken()));
        }

        int k = Integer.parseInt(br.readLine());

        int div = n/k;

        ArrayList<Integer> ans = new ArrayList<>();
        // n i div
        // 8 2
        // i 0 4
        //

        // 12 2
        // i 0 4 8

        // 24 3
        // i 0 8 16

        for (int i = 0; i < n; i += div) {
            ArrayList<Integer> list2 = new ArrayList<>(list1.subList(i, i + div));
            Collections.sort(list2);
            ans.addAll(list2);
            System.out.println(Arrays.deepToString(list2.toArray()));
        }

        for (int i = 0; i < ans.size(); i++) {
            bw.write(ans.get(i) + " ");
        }

        bw.flush();

    }

}
