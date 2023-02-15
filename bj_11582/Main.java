package bj_11582;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

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

        // 간격
        int div = n / k;

        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = 0; i < n; i += div) {

            // subList : 파이썬의 인덱싱
            ArrayList<Integer> list2 = new ArrayList<>(list1.subList(i, i + div));
            Collections.sort(list2);

            // addAll : ArrayList에 자료구조 모든 데이터를 다 넣음
            ans.addAll(list2);
        }

        for (int i = 0; i < ans.size(); i++) {
            bw.write(ans.get(i) + " ");
        }

        bw.flush();

    }

}
