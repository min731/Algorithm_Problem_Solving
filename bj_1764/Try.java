package bj_1764;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Try {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        LinkedList<String> be_heard = new LinkedList<>();
        for(int i=0;i<N;i++){
            be_heard.add(br.readLine());
        }

        Collections.sort(be_heard);
        // for(int i=0;i<be_heard.size();i++){
        //     bw.write(be_heard.get(i));
        //     bw.newLine();
        // }

        int cnt = 0;
        for(int i=0;i<M;i++){
            String be_seen = br.readLine();
            if(be_heard.contains(be_seen)){
                bw.write(be_seen);
                bw.newLine();
                cnt++;
            }
        }

        System.out.println(cnt);

        bw.flush();
        
    }
    
}
