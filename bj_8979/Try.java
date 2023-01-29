package bj_8979;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Try {
    public static void main(String[] args) throws IOException {
        
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<Integer>> countries = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            ArrayList<Integer> medals = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                medals.add(Integer.parseInt(st.nextToken()));
            }
            countries.add(medals);
            // System.out.println(Arrays.deepToString(medals.toArray()));
        }

        // 금메달 정렬

        for (int i=0;i<N;)







    }
}
