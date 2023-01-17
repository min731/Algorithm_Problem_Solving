package bj_10816;
import java.util.Arrays;
import java.util.Scanner;

public class Try {    
    public static void main(String[] args) {

        Scanner stdIn = new Scanner(System.in);

        // int N = stdIn.nextInt();
        // int [] cardArray = new int[N];

        int [] cardArray = new int[] {3,7,-2,5,5};

        Arrays.sort(cardArray);
        System.out.println(Arrays.toString(cardArray));

        // [-10, -10, 2, 3, 3, 3, 3, 5, 6, 7, 7, 10, 10, 10, 10]

    //   for (int i=0;i<cardArray.length;i++){

    //         cardArray[i] = stdIn.nextInt();

    //     }

        // int M = stdIn.nextInt();
        // int [] findArray = new int[M];
        // for (int i=0;i<findArray.length;i++){

        //     findArray[i] = stdIn.nextInt();

        // }
        
        int [] findArray = new int [] {7,9,-5,5,3,0,6};

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
                System.out.println("findArray[i]: " + findArray[i] + " cardArray[pc]: " + cardArray[pc]);
                System.out.println("pl: "+pl + " pc: " + pc + " pr: " + pr);
                if(findArray[i]>cardArray[pc]){
                    pl = pc+1;
                    pc += (pr-pl)/2+1;
                }
                else{ // cardArray[j] > findArray[i]
                    pr = pc-1;

                    pc = pc-(pr-pl)/2-1;

                    //   5-(4-0)/2-1 
                }
                System.out.println("pl: "+pl + " pc: " + pc + " pr: " + pr);

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
            System.out.println(Arrays.toString(output));
            
        }

        return output;
    }
}