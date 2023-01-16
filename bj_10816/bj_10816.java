package bj_10816;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class bj_10816 {

    static int [] binary_search(int [] cardArray, int [] findArray){

        int [] output = new int [findArray.length];

        for (int i=0;i<findArray.length;i++){     // 찾아야하는 것 [10,9,-5,2,3,4,5,-10]
            System.out.println("찾아야 하는 수: " + findArray[i]);
            for (int j=0;j<cardArray.length;j++){  // 찾을 곳 [-10, -10, 2, 3, 3,   6 ,  7, 10, 10, 10 ]
                System.out.println(j);             //           0    1   2  3  4    5    6  7   8   9  
                int pl = 0;              //  pl = 0
                int pc = cardArray.length/2;   //  pc = 5
                int pr = cardArray.length-1;   //  pr = 9 

                while(findArray[i]!=cardArray[j]){
                    System.out.println("pl: " +pl + " pc: " + pc + " pr: " + pr);
                    if(findArray[i]<cardArray[j]){
                        pr = pc-1;
                        pc -= (pr-pl)/2-1; // 5-(4-0)/2-1 = 2
                    }
                    else{
                        pl = pc+1;
                        pc += (pr-pl)/2+1;
                    }
                    if(pl <= pc || pc <= pr){
                        break;
                    }
                }

                if (findArray[i]==cardArray[j]){
                
                    output[i] +=1;

                }
            }
            System.out.println(Arrays.toString(output));
        }

        return output;


    }
    
    public static void main(String[] args) {

        Scanner stdIn = new Scanner(System.in);

        // System.out.print("카드 갯수 N을 입력:");
        // int N = stdIn.nextInt();
        int N = 10;
        // int [] cardArray = new int[10];
        int [] cardArray = {6,3,2,10,10,10,-10,-10,7,3};

        Arrays.sort(cardArray);
        System.out.println(Arrays.toString(cardArray));

    //   for (int i=0;i<N;i++){

    //         System.out.print("배열의 요소를 하나씩 입력하시오.");
    //         cardArray[i] = stdIn.nextInt();

    //     }

        // System.out.println(cardArrayays.toString(cardArray));

        // System.out.print("M을 입력:");
        // int M = stdIn.nextInt();

        int M = 8;
        int [] findArray = {10,9,-5,2,3,4,5,-10};
        System.out.println(Arrays.toString(findArray));

        // for (int i=0;i<M;i++){

        //     findArray[i] = 

        // }

        
        System.out.println(Arrays.toString(binary_search(cardArray, findArray)));

        
    }
    
}