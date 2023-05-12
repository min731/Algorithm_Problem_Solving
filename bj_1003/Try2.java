package bj_1003;

import java.util.ArrayList;
import java.util.Arrays;

public class Try2 {

    static ArrayList <Integer> zero = new ArrayList<Integer>(Arrays.asList(1,0,1));
    static ArrayList <Integer> one = new ArrayList<Integer>(Arrays.asList(0,1,1));

    static void fibonacci(int num){
        
        int len = zero.size();
        
        // num = 3
        // len = 3
        if (num >= len) {

            //              
            for (int i=len; i<num+1;i++){
                zero.add(zero.get(i-1)+zero.get(i-2));
                one.add(one.get(i-1)+one.get(i-2));
            }
        }

        System.out.println(zero.get(num) + ", " + one.get(num));

    }

    public static void main(String[] args) {
        fibonacci(2);
        fibonacci(3);
        fibonacci(4);
        fibonacci(5);
    }
    
}
