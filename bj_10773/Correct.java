package bj_10773;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Correct {

    static Stack stack1 = new Stack<>();
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int K = Integer.parseInt(br.readLine());
        
        int input;
        for(int i=0;i<K;i++){
            input = Integer.parseInt(br.readLine());
            if(input==0){
                stack1.pop();
                continue;
            }
            stack1.push(input);
        }

        int sum = 0;
        while(!stack1.isEmpty()){
            sum+=(int)stack1.pop();
        }

        bw.write(sum+"");
        bw.flush();

    }    
}
