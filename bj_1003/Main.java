package bj_1003;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    // 동적 프로그래밍을 위해 0과 1이 등장하는 ArrayList 저장
    static ArrayList <Integer> zero = new ArrayList<Integer>(Arrays.asList(1,0,1));
    static ArrayList <Integer> one = new ArrayList<Integer>(Arrays.asList(0,1,1));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static void fibonacci(int num) throws IOException{
        
        int len = zero.size();
        
        // num = 3
        // len = 3
        if (num >= len) {

            // 이전에 저장된 0,1 등장 갯수를 더함
            for (int i=len; i<num+1;i++){
                zero.add(zero.get(i-1)+zero.get(i-2));
                one.add(one.get(i-1)+one.get(i-2));
            }
        }

        bw.write(zero.get(num) + " " + one.get(num)+"\n");
        bw.flush();

    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        int [] testCases = new int [T];

        for (int i=0; i<T; i++){
            testCases[i] = Integer.parseInt(br.readLine());
        }

        for (int i=0; i<T; i++){
            fibonacci(testCases[i]);
        }

    }
}
