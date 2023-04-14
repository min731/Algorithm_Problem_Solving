package bj_1182;

public class combination {
    
    static void print(int[] arr, boolean[] visited) {
        for(int i = 0; i < arr.length; i++) {
            if(visited[i] == true)
                System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    static void comb1(int[] arr, boolean[] visited, int start, int r) {
        if(r == 0) {

            print(arr, visited);

            return;

        } else {
                // vistied = [f,f,f,f]
                // i = 0 , r = 2
            for(int i = start; i < arr.length; i++) {
                visited[i] = true;
                comb1(arr, visited, i + 1, r - 1);
                // i = 0 부터
                // vistied = [t,f,f,f]
                // i = 1 , r = 1
                // vistied = [t,t,f,f]
                // i = 2 , r = 0                

                visited[i] = false;
                // i = 1부터
                // vistied = [f,t,f,f]
                // i = 2 , r = 2
                // vistied = [f,t,t,f]
                // i = 3 , r = 1
                // i = 4 , r = 0           


            }
        }
    }
    public static void main(String[] args) {
        
        int [] arr = new int []{1,2,3,4};

        boolean [] visited = new boolean [arr.length];

        int start = 0;

        // 2개 뽑기
        int r = 2;

        comb1(arr, visited, start, r);
    }
    
}
