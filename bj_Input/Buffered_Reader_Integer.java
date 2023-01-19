package bj_Input;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Buffered_Reader_Integer {

    public static void main(String[] args) throws NumberFormatException, IOException {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

         int int1 = 0;

         int1 = Integer.parseInt( br.readLine());

         System.out.println(int1);
    }
    
}
