package bj_8979;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main3 {
    public static void main(String[] args) throws IOException {

        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        HashMap<Integer, Integer> map1 = new HashMap<>();

        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());
            String medals = "";
            String medal = st.nextToken();
            for (int j = 0; j < 3; j++) {
                medal = st.nextToken();
                medals += medal;
            }
            map1.put(i, Integer.parseInt(medals));
        }

        // 메달별 정렬
        ArrayList<Integer> medals_info = new ArrayList<>();
        for (int value : map1.values()) {
            medals_info.add(value);
        }
        Collections.sort(medals_info, Collections.reverseOrder());

        // 등수

        int[] ranking = new int[N];

        int rank = 2;
        ranking[0] = 1;
        for (int i = 0; i < medals_info.size() - 1; i++) {
            if (!medals_info.get(i).equals(medals_info.get(i + 1))) {
                ranking[i + 1] = rank++;
            } else {
                ranking[i + 1] = ranking[i];
                rank++;
            }
        }

        System.out.println(ranking[medals_info.indexOf(map1.get(K))]);

    }
}
