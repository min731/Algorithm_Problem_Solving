package bj_8979;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main2 {
    public static void main(String[] args) throws IOException {

        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        System.out.println("K :" + K);
        HashMap<Integer, Integer> map1 = new HashMap<>();

        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());
            String medals = "";
            int country = Integer.parseInt(st.nextToken());
            for (int j = 0; j < 3; j++) {
                String medal = st.nextToken();
                medals += medal;
            }
            map1.put(country, Integer.parseInt(medals));
            System.out.println(medals);
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
                System.out.print("같음!");
                ranking[i + 1] = ranking[i];
                rank++;
            }
        }

        System.out.println("찾아야 하는 등수: " + K + ", K의 메달: " + map1.get(K));
        System.out.println(Arrays.deepToString(medals_info.toArray()));
        System.out.println(Arrays.toString(ranking));
        System.out.println(ranking[medals_info.indexOf(map1.get(K))]);

    }
}
