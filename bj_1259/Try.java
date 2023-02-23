package bj_1259;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Try {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input;

        while(true){
            
            input = br.readLine();
            if(input.equals("0")){
                break;
            }

            for(int i = 0;i<=input.length()/2;i++){
                if(input.charAt(i)!=input.charAt(input.length()-i-1)){
                    bw.write("no\n");
                    break;
                }
                if(i==input.length()/2){
                    bw.write("yes\n");
                }
                
            }

        }

        bw.flush();
        bw.close();

    }
    
}
