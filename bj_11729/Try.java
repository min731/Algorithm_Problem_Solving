package bj_11729;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class getAns{

    String ans;
    int cnt;

    public getAns() {
        this.ans = "";
        this.cnt = 0;
        
    }
}

public class Try {

    static getAns move(int n, int x, int y,getAns getAns) throws IOException{
        
        if(n>0){
            getAns = move(n-1,x,6-x-y,getAns);
            getAns.ans += (x+" "+y+"\n");
            getAns.cnt++;
            // 3,1,3
                // 2,1,2
                    // 1,1,3
                    // 2,1,2
                    // 1,3,2
                // 3,1,3
                    // 3,1,3
                // 2,2,3
                    //1,2,1
                    //2,2,3
                    //1,1,3
        }
        
        if(n>0){
            move(n-1,6-x-y,y,getAns);
        }
        return getAns;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        getAns getAns = new getAns();

        int n = Integer.parseInt(br.readLine());

        getAns = move(n,1,3,getAns);

        bw.write(getAns.cnt+"\n");
        bw.write(getAns.ans);
        bw.flush();
    }

}