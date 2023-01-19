package bj_2578;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Try {

    static int [][] makeBoard(int board [][],BufferedReader br,BufferedWriter bw) throws IOException{

        StringTokenizer st;

        for(int i=0;i<5;i++){
            System.out.println("빙고판 " + i +"번째 줄 입력");
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<5;j++){
                int el = Integer.parseInt(st.nextToken());
                board[i][j] = el;
                
            }
        }
        
        bw.write("빙고판"+"\n");
        for (int i=0;i<5;i++){
            bw.write(Arrays.toString(board[i])+"\n");
        }
        bw.flush();

        return board;
    }

    static int [] makeCheck(int [] check,BufferedReader br,BufferedWriter bw) throws IOException{

        StringTokenizer st;

        for(int i=1;i<6;i++){
            System.out.println("체크 " + i +"번째 줄 입력");
            st = new StringTokenizer(br.readLine());
            for (int j=1;j<6;j++){
                int el = Integer.parseInt(st.nextToken());
                check[5*(i-1)+j-1] = el;
            }
        }

        bw.write("체크"+"\n");
        bw.write(Arrays.toString(check));
        bw.flush();

        return check;
    }

    static int counting(int [][] board,int [] check) throws IOException{
        int cnt = 0;
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        for (int i=0;i<check.length;i++){
            System.out.println(i + "번째 check: " + check[i]);
            System.out.println(cnt);
            cnt ++;
            int bingo = 0;
            Boolean find = false;
            for(int j=0;j<5;j++){
                for(int k=0;k<5;k++){

                    if (board[j][k] == check[i]){
                        board[j][k] = -1;
                        find = true;

                        bw.write("빙고판"+"\n");
                        for (int m=0;m<5;m++){
                            bw.write(Arrays.toString(board[m])+"\n");
                        }
                        bw.flush();

                        if(find){
                            break;
                        }
                    }
                }
                if(find){
                    break;
                }
            }

            int [] diagonal1 = new int [5];
            int [] diagonal2 = new int [5];
            int [] vertical = new int [5];


            for(int j=0;j<5;j++){
                int idx_ver = 0;

                // 가로줄 빙고 체크
                if(Arrays.stream(board[j]).sum()<-3){
                    bingo ++;
                }
                
                for(int k=0;k<5;k++){
                    if(j==k){
                        diagonal1[j] = board[j][k];
                    }
                    if(j+k==4){
                        diagonal2[j] = board[j][k];
                    }
                    vertical[idx_ver] = board[k][j];
                    idx_ver++;
                }

                // 세로줄 빙고 체크
                if(Arrays.stream(vertical).sum()<-3){
                    bingo ++;
                }
            }

            // 대각선1 빙고 체크
            if(Arrays.stream(diagonal1).sum()<-3){
                bingo++;
            } 

            // 대각선2 빙고 체크
            if(Arrays.stream(diagonal2).sum()<-3){
                bingo++;
            } 

            if (bingo>=3){
                break;
            }
            bw.write(bingo);
            bw.flush();
        }

        return cnt;
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int board [][] = new int [5][5];
        int check [] = new int [25];
        int cnt = 0;

        board = makeBoard(board, br, bw);
        check = makeCheck(check, br, bw);
        cnt = counting(board, check);

        bw.write("답은 : " + String.valueOf(cnt));
        bw.flush();

        

    



    }
}
