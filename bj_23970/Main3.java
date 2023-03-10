package bj_23970;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main3 {

    static int bubble_sort(int[] A, int[] B, int n) {

        ArrayList<String> sortProcesses = new ArrayList<>();

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
                    sortProcesses.add(Arrays.toString(A));
                    // if (Arrays.equals(A, B)) {
                    // return 1;
                    // }
                }
            }
            same = last;
            if (check == 0) {
            break;
            }

        }

        System.out.println(Arrays.deepToString(sortProcesses.toArray()));
        for (String Process:sortProcesses){
            System.out.println("A:" + Process +" B: "+Arrays.toString(B));
            if(Process.equals(Arrays.toString(B))){
                return 1;
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