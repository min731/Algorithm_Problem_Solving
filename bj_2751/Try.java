package bj_2751;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Try {

    static void quickSort(int [] arr,int left,int right){
        int low = left;
        int high = right;
        int m = sortelem3(arr, low, (low+high)/2, high);
        int x = arr[m];

        swap(arr, m,right-1);
        low++;
        high-=2;

        while(low<=high){
            if(arr[low]<x){
                low++;
            }
            if(arr[high]>x){
                high--;
            }
            if(low<=high){
                swap(arr, low++, high--);
            }
        }

        if(left<high){
            quickSort(arr, left, high);
        }
        if(low<right){
            quickSort(arr, low, right);
        }

    }


    static int sortelem3(int [] arr, int a, int b, int c){
        if(arr[b]<arr[a]){
            swap(arr, b, a);
        }
        if(arr[b]>arr[c]){
            swap(arr, b, c);
        }
        if(arr[b]<arr[a]){
            swap(arr, b, a);
        }

        return b;
    }

    static void swap(int [] arr, int front, int rear){
        int tmp = arr[front];
        arr[front] = arr[rear];
        arr[rear] = tmp;
    }
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int [] arr = new int [N];

        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        quickSort(arr, 0, arr.length-1);

        for(int i=0;i<N;i++){
            if(i==N-1){
                bw.write(arr[i]+"");
                break;
            }
            bw.write(arr[i]+"\n");
        }
        bw.flush();





    }
}
