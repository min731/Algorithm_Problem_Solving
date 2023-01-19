package bj_Input;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class while_readLine {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = "";
        String tmp = "";
        while((tmp = br.readLine())!= null){
            str += tmp;
            System.out.print(str);
            System.out.println();
        }
    }
    
}
