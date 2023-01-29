package bj_8979;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
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
            for (int j = 0; j < 4; j++) {
                String medal = st.nextToken();
                medals += medal;
            }
            map1.put(i, Integer.parseInt(medals));
            System.out.println(medals);
        }

        // 메달 정렬
        Set<Integer> medals_info_set = new HashSet<>();

        for (int value : map1.values()) {
            medals_info_set.add(value);
        }

        ArrayList<Integer> medals_info = new ArrayList<>(medals_info_set);

        Collections.sort(medals_info, Collections.reverseOrder());
        System.out.println(Arrays.deepToString(medals_info.toArray()));

        System.out.println(medals_info.indexOf(map1.get(K)) + 1);

    }
}
