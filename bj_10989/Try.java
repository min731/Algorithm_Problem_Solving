package bj_10989;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Try {

    static int [] countingSort(int [] arr, int N, int max){
     
        // 누적도수
        int [] f = new int[max+1];
        // 작업용 목표 배열
        int [] b = new int[N];
    
        // 도수분포표
        for (int i=0; i<N; i++) f[arr[i]]++;
        // System.out.println(Arrays.toString(f));

        System.out.println("-------------누적도수분포표-------------");
        // 누적도수분포표
        for (int i=1;i<=max;i++){
            f[i] += f[i-1];
        }
        System.out.println(Arrays.toString(f));

        System.out.println("-------------목표배열-------------");
        // 목표 배열
        for (int i=N-1;i>=0;i--){
            System.out.println("i 는 " + i);
            // System.out.println("원래 f[arr[i]] 는 " + f[arr[i]]);

            // * -- 연산자 : 참조한 객체의 값을 -1함
            // max = 7
            b[(N-1)-(--f[arr[i]])] = arr[i];
            // int temp = f[arr[i]];
            // System.out.println("arr[i] 는 " + arr[i]);
            // System.out.println("f[arr[i]] 는 " + (temp));
            System.out.println(Arrays.toString(b));
            // System.out.println("--------------");
        }
        //최종 배열
        for (int i=0;i<N;i++) arr[i] = b[i];

        return arr;

    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N;

        N = Integer.parseInt(br.readLine());
        int [] arr = new int [N];

        for (int i=0;i<N;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        System.out.println("-----------원본 배열------------");
        System.out.println(Arrays.toString(arr));
        System.out.println("----------도수분포표------------");

        // 최댓값 구하기
        int max = arr[0];

        for (int i=1; i<N;i++)
        if (arr[i] > max) max =arr[i];

        arr = countingSort(arr,N,max);

        System.out.println("----------정답------------");
        bw.write(Arrays.toString(arr));
        bw.flush();


    }
}
