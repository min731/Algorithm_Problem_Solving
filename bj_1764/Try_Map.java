package bj_1764;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Try_Map {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String,Integer> not_be_heard_seen = new HashMap<>();

        for (int i = 0; i < N; i++) {
            not_be_heard_seen.put(br.readLine(),1);
        }

        for (int i = 0; i < M; i++) {
            String input = br.readLine();
            if(not_be_heard_seen.keySet().contains(input))
            not_be_heard_seen.put(input,2);
        }

        List<String> ANS = new ArrayList<>();

        for(Map.Entry<String, Integer> entry : not_be_heard_seen.entrySet()){
            if(entry.getValue()==2){
                ANS.add(entry.getKey());
            }
        }
        bw.write(ANS.size() + "\n");

        Collections.sort(ANS);

        for (int i = 0; i < ANS.size(); i++) {
            bw.write(ANS.get(i) + "\n");
        }

        bw.flush();

    }

}
