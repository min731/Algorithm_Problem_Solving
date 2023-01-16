package bj_10816;
import java.util.Arrays;
import java.util.Scanner;

public class Main {    
    public static void main(String[] args) {

        Scanner stdIn = new Scanner(System.in);

        int N = stdIn.nextInt();
        int [] cardArray = new int[N];
        Arrays.sort(cardArray);

      for (int i=0;i<cardArray.length;i++){

            cardArray[i] = stdIn.nextInt();

        }

        int M = stdIn.nextInt();
        int [] findArray = new int[M];
        for (int i=0;i<findArray.length;i++){

            findArray[i] = stdIn.nextInt();

        }
        
        for (int i : binary_search(cardArray, findArray)){

            System.out.print(i+" ");
        }
     
        
    }
        private static int [] binary_search(int [] cardArray, int [] findArray){

        int [] output = new int [findArray.length];

        for (int i=0;i<findArray.length;i++){    

            for (int j=0;j<cardArray.length;j++){ 
                int pl = 0;              
                int pc = cardArray.length/2;   
                int pr = cardArray.length-1;   

                while(findArray[i]!=cardArray[j]){
                    if(findArray[i]<cardArray[j]){
                        pr = pc-1;
                        pc -= (pr-pl)/2-1; 
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
        }

        return output;
    }
}