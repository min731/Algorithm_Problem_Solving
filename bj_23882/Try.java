package bj_23882;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Try {

    static int selection_sort(int[] arr, int N,int K) {

        int cnt =0;

        for (int i = N - 1; i > 0; i--) {
            int max_idx = 0;
            System.out.println("<" + i + " 부터 탐색>");
            for (int j = i; j >= 0; j--) {
                if (arr[i] <= arr[j]) {
                    max_idx = j;
                }
            }

            if(arr[i]==arr[max_idx]){
                continue;
            }

            System.out.println(N - i + " 번째 정렬 ");
            System.out.println("바꿀 인덱스: " + i + ", 최댓값 인덱스: " + max_idx);
            System.out.println("정렬 전: " + Arrays.toString(arr));
            cnt = swap(arr, i, max_idx,cnt);
            System.out.println("정렬 후: " + Arrays.toString(arr));

            if (cnt==K){
                System.out.println("출력: " + Arrays.toString(arr));
            }

        }

        return cnt;
    }

    static int swap(int[] arr, int a, int b,int cnt) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;

        cnt++;

        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(Arrays.toString(arr));
        int cnt = selection_sort(arr,N,K);
        System.out.println(Arrays.toString(arr));

        if(cnt<K){
            System.out.println(-1);
        }

    }

}
