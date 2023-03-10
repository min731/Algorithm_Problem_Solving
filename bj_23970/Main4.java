package bj_23970;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main4 {

    static int bubble_sort(int[] A, int[] B, int n) {

        if (Arrays.equals(A, B)) {
            return 1;
        }

        int same = n - 1;
        for (int i = 0; i < same; i++) {
            int last = n-1;
            int check = 0;
            for (int j = i; j < same - i; j++) {
                if (A[j] > A[j + 1]) {
                    swap(A, j, j + 1);
                    check++;
                    last = j + 1;

                    if(A[j]==B[j]){
                        if(Arrays.toString(A).equals(Arrays.toString(B))){
                            return 1;
                        }
                    }
                    // 정렬 할 때 마다 비교
                    System.out.println(Arrays.toString(A) +" vs "+(Arrays.toString(B)));
                    if(Arrays.toString(A).equals(Arrays.toString(B))){
                        return 1;
                    }

                }
            }
            same = last;
            if (check == 0) {
            break;
            }

        }

        return 0;
    }

    static void swap(int[] A, int front, int rear) {
        int temp = A[front];
        A[front] = A[rear];
        A[rear] = temp;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int[] A = new int[n];
        for (int i = 0; i < A.length; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int[] B = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < A.length; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        bw.write(bubble_sort(A, B, n) + "");

        bw.flush();

    }

}