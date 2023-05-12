package bj_1003;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Try {

    static int fibonacci(int num){
        if (num == 0){
            return 0;
        }
        else if (num == 1){
            return 1;
        }
        else {

            return fibonacci(num-1) + fibonacci(num-2);
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());

        int [] testCases = new int [T];

        for (int i=0; i<T; i++){
            testCases[i] = Integer.parseInt(br.readLine());
        }

        for (int i=0; i<T; i++){
            bw.write(fibonacci(testCases[i])+"");
            bw.flush();
        }




        
    }
}