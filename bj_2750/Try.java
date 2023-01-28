package bj_2750;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Try {

    // 삽입 정렬
    static void insertSort(int[] arr, int N) {

        for (int i = 1; i < N; i++) {
            if (arr[i - 1] > arr[i]) {
                for (int j = 0; j <= i - 1; j++) {
                    if (arr[j] > arr[i]) {
                        swap(arr, i, j);
                    }
                }
            }
        }
    }

    static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        insertSort(arr, arr.length);

        for (int i = 0; i < N; i++) {
            System.out.println(arr[i]);
        }

    }
}
