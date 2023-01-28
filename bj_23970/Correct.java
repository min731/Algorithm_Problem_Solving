package bj_23970;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Correct {

    static int bubble_sort(int[] A, int[] B, int n) {

        // A,B 처음부터 같으면 1
        if (Arrays.equals(A, B)) {
            return 1;
        }

        // last, last2 : 정렬이 끝난 인덱스는 for문 돌지 않아도 됌
        int last = n - 1;
        int last2 = 0;
        for (int i = 0; i < n - 1; i++) {
            if (last == 0) {
                break;
            }
            int check = 0;
            for (int j = 0; j < last; j++) {
                if (A[j] > A[j + 1]) {
                    swap(A, j, j + 1);
                    check++;
                    last2 = j;

                    if (A[j] == B[j]) {
                        if (Arrays.equals(A, B)) {
                            return 1;
                        }
                    }
                }
            }
            last = last2;
            // 바뀌는 것이 없으면 break;
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