package bj_3085;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Try {

    static int checkMax (String [][] tmp_board){
        int eatNumH = 0;
        int eatNumV = 0;
        int max_tmp_eatNum =0;

        int len = tmp_board.length;

        for (int i=0;i<len;i++){
            int tmp_eatNum = 1;
            for(int j=0;j<len-1;j++){
                if (tmp_board[i][j].equals(tmp_board[i][j+1])){
                    tmp_eatNum +=1;
                }
                else{
                    if(max_tmp_eatNum <tmp_eatNum){
                        max_tmp_eatNum = tmp_eatNum;
                    }
                    tmp_eatNum = 0;
                }

            }
            System.out.println("eatNumH 와 tmp_eatNum " + eatNumH + ", " + max_tmp_eatNum);
            if (eatNumH < max_tmp_eatNum){
                eatNumH = max_tmp_eatNum;
            }
        }

        max_tmp_eatNum =0;

        for (int i=0;i<len;i++){
            int tmp_eatNum = 1;
            for(int j=0;j<len-1;j++){
                if (tmp_board[j][i].equals(tmp_board[j+1][i])){
                    tmp_eatNum +=1;
                }
                else{
                    if(max_tmp_eatNum <tmp_eatNum){
                        max_tmp_eatNum = tmp_eatNum;
                    }
                    tmp_eatNum = 0;
                }
            }
            System.out.println("eatNumV 와 tmp_eatNum " + eatNumV + ", " + max_tmp_eatNum);
            if (eatNumV < max_tmp_eatNum){
                eatNumV = max_tmp_eatNum;
            }
        }


        return Math.max(eatNumH,eatNumV);
    }


    static int swap(String [][] board, int i, int j, boolean is_H){

        System.out.println("------- 원본 board--------");
        for(int k=0; k<board.length; k++){
            System.out.println(Arrays.toString(board[k]));
        }
        System.out.println("--------------------------");



        int eatNum = 0;
        String [][] tmp_board = board;
        String tmp_color = tmp_board[i][j];

        if (is_H){
            tmp_board[i][j] = tmp_board[i][j+1];
            tmp_board[i][j+1] = tmp_color;

            System.out.println("--------가로로 다를 때 swap--------");
            for(int k=0; k<tmp_board.length; k++){
                System.out.println(Arrays.toString(board[k]));
            }

            eatNum = checkMax(tmp_board);
            System.out.println("최대 갯수 : " + eatNum);
            System.out.println("----------------------------------");

            tmp_board[i][j+1] = tmp_board[i][j];
            tmp_board[i][j] = tmp_color;
        }
        else{
            tmp_board[i][j] = tmp_board[i+1][j];
            tmp_board[i+1][j] = tmp_color;

            System.out.println("--------세로로 다를 때 swap--------");
            for(int k=0; k<tmp_board.length; k++){
                System.out.println(Arrays.toString(board[k]));
            }

            eatNum = checkMax(tmp_board);
            System.out.println("최대 갯수 : " + eatNum);
            System.out.println("----------------------------------");
            
            tmp_board[i][j] = tmp_board[i+1][j];
            tmp_board[i+1][j] = tmp_color;
        }

        return eatNum;
    }

    static int eatMax(String [][] board){
        int max = 0;
        int tmp_max = 0;

        int len = board.length;
        boolean is_H = false;

        for (int i=0;i<len;i++){
            for(int j=0;j<len;j++){
                is_H = false;

                // 가로로 다를 때
                if (j+1<=len-1){
                    if (!board[i][j].equals(board[i][j+1])){
                        is_H = true;
                        System.out.println("--------가로로 다를 때--------");
                        System.out.println("i와 j 는 " + i + ", " + j);
                        System.out.println("board[i][j] 와 board[i][j+1] " + board[i][j] + ", " + board[i][j+1]);
                        tmp_max = swap(board, i, j, is_H);
                        if (max < tmp_max){
                            max = tmp_max;
                        }
                    }
                }

                // 세로로 다를 때
                if (i+1<=len-1){
                    if (!board[i][j].equals(board[i+1][j])){
                        is_H = false;
                        System.out.println("--------세로로 다를 때--------");
                        System.out.println("i와 j 는 " + i + ", " + j);
                        System.out.println("board[i][j] 와 board[i+1][j] " + board[i][j] + ", " + board[i+1][j]);
                        tmp_max = swap(board, i, j, is_H);
                        if (max < tmp_max){
                            max = tmp_max;
                        }
                    }
                }



            }
        }


        return max;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        String [][] board = new String [N][N];

        for (int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            String line = st.nextToken();
            for(int j=0;j<N;j++){
                board[i][j] = String.valueOf(line.charAt(j));
            }
        }

        int ans = eatMax(board);

        bw.write(ans+"");
        bw.flush();

        // for(int i=0; i<N; i++){
        //     System.out.println(Arrays.toString(board[i]));
        // }



    }
}
