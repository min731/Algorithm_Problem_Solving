package bj_1302;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Correct_answer {

    // 입력값 받기
    static HashMap<String, Integer> getData() throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Integer> map1 = new HashMap<>();

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {

            String book = br.readLine();

            if (!map1.containsKey(book)) {
                map1.put(book, 1);
                continue;
            }

            map1.put(book, map1.get(book) + 1);

        }
        return map1;
    }

    // 베스트 셀러 출력하기
    static String getAns(HashMap<String, Integer> map1) {

        String best = "";
        int max = 0;
        ArrayList<String> bests = new ArrayList<>();

        // 가장 큰 value값 찾기
        for (String key : map1.keySet()) {
            if (map1.get(key) >= max) {
                max = map1.get(key);
            }
        }

        // 베스트 셀러 이름 수집
        for (Map.Entry<String, Integer> entry1 : map1.entrySet()) {
            String key = entry1.getKey();
            Integer value = entry1.getValue();
            if (value == max) {
                bests.add(key);
            }
        }

        // 베스트셀러 이름 정렬
        Collections.sort(bests);
        best = bests.get(0);
        System.out.println(best);

        return best;

    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        HashMap<String, Integer> map1 = new HashMap<>();
        String best = "";

        // 입력값 받기
        map1 = getData();

        // 베스트셀러 출력
        getAns(map1);

    }

}