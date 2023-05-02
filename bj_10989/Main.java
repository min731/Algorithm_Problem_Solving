package bj_10989;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    static int [] countingSort(int [] arr, int N, int max){
        
        // 누적도수
        int [] f = new int[max+1];
        // 작업용 목표 배열
        int [] b = new int[N+1];
    
        // 도수분포표
        for (int i=0; i<N; i++) f[arr[i]]++;
        
        // 누적도수분포표
        for (int i=1;i<=max;i++){
            f[i] += f[i-1];
        }
        // 목표 배열
        for (int i=N-1;i>=0;i--){
            // * -- 연산자 : 참조한 객체의 값을 -1함
            b[--f[arr[i]]] = arr[i];
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

        // 최댓값 구하기
        int max = arr[0];
        for (int i=1; i<N;i++)
        if (arr[i] > max) max =arr[i];

        arr = countingSort(arr,N,max);

        for (int i=0;i<N;i++){
            bw.write(arr[i]+"\n");
        }
        bw.flush();

    }
}
