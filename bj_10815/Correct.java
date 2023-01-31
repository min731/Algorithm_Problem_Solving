package bj_10815;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Correct {

    static void binarySearch(int[] mycard, int x, BufferedWriter bw) throws IOException {
        int low = 0;
        int high = mycard.length - 1;
        int mid;
        while (low <= high) {

            mid = (low + high) / 2;

            if (mycard[mid] == x) {
                bw.write("1 ");
                return;
            }

            else if (x < mycard[mid]) {
                high = mid - 1;
            }

            else {
                low = mid + 1;
            }

        }

        bw.write("0 ");
    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int[] mycard = new int[N];
        for (int i = 0; i < N; i++) {
            mycard[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int[] check = new int[M];
        for (int i = 0; i < M; i++) {
            check[i] = Integer.parseInt(st.nextToken());
        }

        // 이진 탐색
        Arrays.sort(mycard);
        for (int i = 0; i < M; i++) {
            binarySearch(mycard, check[i], bw);
        }

        bw.flush();

    }

}
