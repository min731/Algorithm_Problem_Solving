package bj_10816;
import java.util.Arrays;
import java.util.Scanner;

public class Try2 {    
    public static void main(String[] args) {

        Scanner stdIn = new Scanner(System.in);

        int N = stdIn.nextInt();
        int [] cardArray = new int[N];

       for (int i=0;i<N;i++){

             cardArray[i] = stdIn.nextInt();

         }
        
        Arrays.sort(cardArray);

         int M = stdIn.nextInt();
         int [] findArray = new int[M];
         for (int i=0;i<M;i++){

             findArray[i] = stdIn.nextInt();

         }

        for (int i : binary_search(cardArray, findArray)){

            System.out.print(i+" ");
        }
     
        
    }
        private static int [] binary_search(int [] cardArray, int [] findArray){

        int [] output = new int [findArray.length];

        for (int i=0;i<findArray.length;i++){  // {10, 9 ,-5 , 2 , 3 , 4 , 5 , -10}

                                               // {-10, -10 , 2 , 3 , 3 ,   6   , 7 , 10 , 10, 10}
            int pl = 0;                        //   0     1   2   3   4     5     6   7    8    9
            int pc = cardArray.length/2;   
            int pr = cardArray.length-1;   

            while(findArray[i]!=cardArray[pc]){

                if(findArray[i]>cardArray[pc]){
                    pl = pc+1;
                    pc += (pr-pl)/2+1;
                }
                else{ 
                    pr = pc-1;
                    pc = pc-(pr-pl)/2-1;
                }

                if(pl > pc || pc > pr){
                    break;
                }

            }

            if ( 0<=pc && pc < cardArray.length && findArray[i]==cardArray[pc]){
                output[i] +=1;
                for (int m=pc-1; 0<=m;m--){
                    if (cardArray[m]==findArray[i]){
                        output[i] +=1;
                    }
                }
                for (int m=pc+1; m<=pr;m++){
                    if (cardArray[m]==findArray[i]){
                        output[i] +=1;
                    }
                }
            }
            
        }

        return output;
    }
}