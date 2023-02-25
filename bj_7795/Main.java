package bj_7795;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int upperBound(int key, int [] B){

        int low = 0;
        int high = B.length-1;

        while(low<high){
            int mid = (high-low)/2;
            System.out.println(" low: "+low +" mid: "+mid +" high: " + high );
            if(key>B[mid]){
                low = mid;
            }
            else{
                high = mid-1;
            }

        }

        return high;

    }

    static int lowerBound(int key, int [] B){
        int low = 0;
        int high = B.length-1;

        while(low<high){
            int mid = (high-low)/2;
            if(key>B[mid]){
                low = mid+1;
            }
            else{
                high = mid;
            }
        }
        return low;

    }


    
    public static void main(String[] args) throws IOException {
        
        System.out.println("테스트 케이스 갯수 입력:");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());

        for(int i=0;i<t;i++){
            System.out.println("A_len B_len 입력:");
            st = new StringTokenizer(br.readLine());
            int A_len = Integer.parseInt(st.nextToken());
            int B_len = Integer.parseInt(st.nextToken());

            int [] A = new int [A_len];
            int [] B = new int [B_len];
            
            // System.out.println(A.length);
            // System.out.println(B.length);

            System.out.println("A의 요소 입력:");
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<A.length;j++){
                A[j] = Integer.parseInt(st.nextToken());
            }

            System.out.println("B의 요소 입력:");
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<B.length;j++){
                B[j] = Integer.parseInt(st.nextToken());
            }
            
            Arrays.sort(B);

            System.out.println(Arrays.toString(A) + Arrays.toString(B));
            

            int cnt = 0;

            for(int m=0;m<A.length;m++){                
                
                cnt = upperBound(A[m], B)-lowerBound(A[m], B);
                cnt += cnt;
                bw.write(cnt);
                System.out.println(m);
                }

            bw.flush();

            }
        }


            // System.out.println("A 입력:");
            // for (int m=0;m<A_len;m++){
            //     A[m] = Integer.parseInt(st.nextToken());
            // }
            // System.out.println("B 입력:");
            // for(int n=0;n<B_len;n--){
            //     B[n] = Integer.parseInt(st.nextToken(null));
            
        
    
}
