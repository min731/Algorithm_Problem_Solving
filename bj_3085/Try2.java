package bj_3085;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Try2 {

    static int checkMax (String [][] tmp_board){
        int eatNumH = 0;
        int eatNumV = 0;

        int len = tmp_board.length;

        for (int i=0;i<len;i++){
            int tmp_eatNum = 1;
            for(int j=0;j<len-1;j++){
                if (tmp_board[i][j].equals(tmp_board[i][j+1])){
                    tmp_eatNum +=1;
                }
            }
            if (eatNumH < tmp_eatNum){
                eatNumH = tmp_eatNum;
            }
        }

        for (int i=0;i<len;i++){
            int tmp_eatNum = 1;
            for(int j=0;j<len-1;j++){
                if (tmp_board[j][i].equals(tmp_board[j+1][i])){
                    tmp_eatNum++;
                }
            }
            if (eatNumV < tmp_eatNum){
                eatNumV = tmp_eatNum;
            }
        }


        return Math.max(eatNumH,eatNumV);
    }


    static int swap(String [][] board, int i, int j, boolean is_H){
        int eatNum = 0;
        String [][] tmp_board = board;
        String tmp_color = tmp_board[i][j];

        if (is_H){
            tmp_board[i][j] = tmp_board[i][j+1];
            tmp_board[i][j+1] = tmp_color;

            for(int k=0; k<tmp_board.length; k++){
            }

            eatNum = checkMax(tmp_board);
        }
        else{
            tmp_board[i][j] = tmp_board[i+1][j];
            tmp_board[i+1][j] = tmp_color;

            eatNum = checkMax(tmp_board);
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

    }
}
