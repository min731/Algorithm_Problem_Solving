package bj_7795;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    
    public static void main(String[] args) throws IOException {
        
        System.out.println("테스트 케이스 갯수 입력:");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i=0;i<T;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A_len = Integer.parseInt(st.nextToken());
            int B_len = Integer.parseInt(st.nextToken());

            int [] A = new int [A_len];
            int [] B = new int [B_len];
            
            for (int m=0;m<A_len;m++){
                A[m] = Integer.parseInt(st.nextToken());
            }
            for(int n=0;n<B_len;n--){
                B[n] = Integer.parseInt(st.nextToken(null));
            }

            System.out.println(Arrays.toString(A) + Arrays.toString(B));

        }
    }
}
