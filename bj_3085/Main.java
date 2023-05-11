package bj_3085;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    static char [][] board;
    static int N;
    static int max=0;

    static void check(){
        
        // 가로 체크
        for(int i=0; i<N; i++){
            int cnt = 1;
            for (int j=0; j<N-1; j++){
                if (board[i][j] == board[i][j+1]){
                    cnt ++;
                }
                else{
                    cnt = 1;
                }
                max = Math.max(max,cnt);

            }
        }

        // 세로 체크
        for (int i=0; i<N; i++){
            int cnt = 1;
            for (int j=0; j<N-1; j++){

                if (board[j][i] == board[j+1][i]){
                    cnt++;
                }
                else{
                    cnt = 1;
                }
                max = Math.max(max,cnt);
            }

        }
    }



    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        board = new char [N][N];

        for (int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            String line = st.nextToken();
            for(int j=0;j<N;j++){
                board[i][j] = line.charAt(j);
            }
        }

        // 가로 먼저 체크
        for (int i=0; i<N; i++){
            for (int j=0; j<N-1; j++){

                // 가로 인접 문자 교환
                char tmp = board[i][j];
                board[i][j] = board[i][j+1];
                board[i][j+1] = tmp;

                // 최대 갯수 확인

                check();

                // 교환한 문자 복구
                board[i][j+1] = board[i][j];
                board[i][j] = tmp;

            }
        }

        // 세로 체크
        for (int i=0; i<N; i++){
            for (int j=0; j<N-1; j++){

                // 가로 인접 문자 교환
                char tmp = board[j][i];
                board[j][i] = board[j+1][i];
                board[j+1][i] = tmp;

                // 최대 갯수 확인

                check();

                // 교환한 문자 복구
                board[j+1][i] = board[j][i];
                board[j][i] = tmp;

            }
        }

        bw.write(max+"");
        bw.flush();
    }
}
