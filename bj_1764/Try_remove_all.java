package bj_1764;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Try_remove_all {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<String> not_be_heard = new ArrayList<>();
        List<String> not_be_heard_origin = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String input = br.readLine();

            not_be_heard.add(input);
            not_be_heard_origin.add(input);
        }

        List<String> not_be_seen = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            not_be_seen.add(br.readLine());
        }

        not_be_heard.removeAll(not_be_seen);
        not_be_heard_origin.removeAll(not_be_heard);

        Collections.sort(not_be_heard_origin);

        int n = not_be_heard_origin.size();

        bw.write(n + "");
        bw.newLine();

        for (int i = 0; i < n; i++) {
            bw.write(not_be_heard_origin.get(i));
            bw.newLine();
        }

        bw.flush();

    }

}
