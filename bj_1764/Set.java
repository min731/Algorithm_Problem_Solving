package bj_1764;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Set {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        LinkedList<String> not_be_heard = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            not_be_heard.add(br.readLine());
        }

        LinkedList<String> not_be_heard_seen = new LinkedList<>();

        // for(int i=0;i<be_heard.size();i++){
        // bw.write(be_heard.get(i));
        // bw.newLine();
        // }

        for (int i = 0; i < M; i++) {
            String not_be_seen = br.readLine();
            if (not_be_heard.contains(not_be_seen)) {
                not_be_heard_seen.add(not_be_seen);
            }
        }

        bw.write(not_be_heard_seen.size() + "\n");

        Collections.sort(not_be_heard_seen);

        for (int i = 0; i < not_be_heard_seen.size(); i++) {
            bw.write(not_be_heard_seen.get(i) + "\n");
        }

        bw.flush();

    }

}
