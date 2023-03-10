package bj_1302;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Try {

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
        System.out.println(map1);
        return map1;
    }

    static String getAns(HashMap<String, Integer> map1) {

        String best = "";
        int max = 0;
        ArrayList<String> bests = new ArrayList<>();

        for (String key : map1.keySet()) {
            if (map1.get(key) >= max) {
                max = map1.get(key);
            }
        }

        for (Map.Entry<String, Integer> entry1 : map1.entrySet()) {
            String key = entry1.getKey();
            Integer value = entry1.getValue();
            if (value == max) {
                bests.add(key);
            }
        }

        Collections.sort(bests);
        System.out.println(bests);
        best = bests.get(0);

        System.out.println(best);

        return best;

    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        HashMap<String, Integer> map1 = new HashMap<>();
        String best = "";

        map1 = getData();
        getAns(map1);

    }

}
