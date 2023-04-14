package bj_1182;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main3 {

    // static 변수 초기화
    // ans (S에 해당하는 갯수)
    static int ans = 0;

    static void print(int[] arr, boolean[] visited, int S) {

        int check_S = 0;

        for(int i = 0; i < arr.length; i++) {

            // 조합을 구한뒤 check_S에 더해서 S인지 확인
            if(visited[i] == true){
                check_S += arr[i];
            }
        }

        // 합이 S이면 ans에 +1
        if (check_S == S){
            ans += 1;
        }
        
        return ;
    }

    // combination 함수 정의
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
        
        // 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int  N = Integer.parseInt(st.nextToken());
        int [] arr = new int [N];
        int  S = Integer.parseInt(st.nextToken());

        st  = new StringTokenizer(br.readLine());

        for(int i = 0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 부분수열 최소 1개부터 최대 5개까지 (1 <= r <= 5)

        boolean [] visited = new boolean [arr.length];
        int start = 0;

        for (int r = 1; r<arr.length+1; r++){
            comb1(arr, visited, start, r, S);
        }
        
        // 최종답 출력
        System.out.print(ans);

    }

}
