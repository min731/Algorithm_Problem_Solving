package bj_23882;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main2 {

    static int selection_sort(int[] arr, int N, int K) {

        int cnt = 0;

        for (int i = N - 1; i > 0; i--) {
            int max_idx = -1;
            for (int j = i-1; j >= 0; j--) {
                if (arr[i] < arr[j]) {
                    max_idx = j;
                }
            }

            if(max_idx!=-1){
                cnt = swap(arr, i, max_idx, cnt);
            }

            if (cnt == K) {
                for (int el : arr) {
                    System.out.print(el + " ");
                }
            }

        }

        return cnt;
    }

    static int swap(int[] arr, int a, int b, int cnt) {
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

        int cnt = selection_sort(arr, N, K);

        if (cnt < K) {
            System.out.println(-1);
        }

    }

}