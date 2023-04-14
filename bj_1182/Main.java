package bj_1182;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int ans = 0;

    static void print(int[] arr, boolean[] visited, int S) {

        int [] tmp_arr = new int [arr.length]; 

        for(int i = 0; i < arr.length; i++) {
            if(visited[i] == true){
                // System.out.print(arr[i] + " ");
                tmp_arr[i] = arr[i];
            }
        }
        // System.out.println();
        // System.out.println(Arrays.toString(tmp_arr));

        if (Arrays.stream(tmp_arr).sum() == S){
            // System.out.println("합이 " + S);
            ans += 1;
        }
        
        return ;
    }

    static void comb1(int[] arr, boolean[] visited, int start, int r, int S) {
        if(r == 0) {

            print(arr, visited,S);

            return;

        } else {

            for(int i = start; i < arr.length; i++) {
                visited[i] = true;
                comb1(arr, visited, i + 1, r - 1,S);
                visited[i] = false;


            }
        }
    }


    public static void main(String[] args) throws IOException {
    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int  N = Integer.parseInt(st.nextToken());
        int [] arr = new int [N];
        int  S = Integer.parseInt(st.nextToken());

        st  = new StringTokenizer(br.readLine());

        for(int i = 0; i<5; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 부분수열 최소 1개부터 최대 5개까지 (1 <= r <= 5)

        boolean [] visited = new boolean [arr.length];
        int start = 0;

        for (int r = 1; r<arr.length+1; r++){
            comb1(arr, visited, start, r, S);
        }
        
        // System.out.println("갯수는 : " + ans);
        System.out.print(ans);

    }

}
