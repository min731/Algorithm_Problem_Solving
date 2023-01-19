package bj_Input;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


        // 1 2 3 4 5 
        // [1, 2, 3, 4, 5]
public class String_Tokenizer {
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int [] arr = new int [n];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++){
            int x = Integer.parseInt(st.nextToken());
            arr[i] = x;

        }

        System.out.println(Arrays.toString(arr));

    }
    
}
