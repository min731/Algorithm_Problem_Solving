package bj_2178;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Try {

    static void dfs(int[][] board, int x, int y, boolean[][] visitied, int cnt) {

        // root 위치(0,0)는 바로 = true
        visitied[x][y] = true;

        for (int i = 0; i < visitied.length; i++) {
            System.out.println(Arrays.toString(visitied[i]));
        }

        if (x == board.length - 1 && y == board[0].length - 1) {
            System.out.println("도착");
            System.out.println(cnt);
            return;
        }

        // System.out.println("dfs 후 x,y: " + x + "," + y);
        System.out.println("-----------------");
        // 1,1 기준
        // 0,1 1,0 ,1,2 2,1

        int[] moves_x = new int[] { 1, 0, 0, -1 };
        int[] moves_y = new int[] { 0, 1, -1, 0 };

        boolean back = false;
        for (int i = 0; i < moves_x.length; i++) {
            if (x + moves_x[i] >= 0 && x + moves_x[i] < board.length && y + moves_y[i] >= 0
                    && y + moves_y[i] < board[0].length) {
                if (visitied[x + moves_x[i]][y + moves_y[i]] == false) {
                    if (board[x + moves_x[i]][y + moves_y[i]] == 1) {
                        System.out.println((x + moves_x[i]) + "," + (y + moves_y[i]) + " 로 이동");
                        cnt++;
                        dfs(board, x + moves_x[i], y + moves_y[i], visitied, cnt);
                        back = true;
                    }
                }

            }
            if (back == true) {
                cnt--;
            }
        }

    }

    public static void main(String[] args) throws IOException {

        // board 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int row_num = Integer.parseInt(st.nextToken());
        int column_num = Integer.parseInt(st.nextToken());

        int[][] board = new int[row_num][column_num];

        for (int i = 0; i < row_num; i++) {
            int[] column = new int[column_num];
            String map = br.readLine();
            for (int j = 0; j < column_num; j++) {
                column[j] = Integer.parseInt(Character.toString(map.charAt(j)));
            }
            board[i] = column;
        }

        // board 확인
        for (int i = 0; i < row_num; i++) {
            System.out.println(Arrays.toString(board[i]));
        }

        // root 위치
        int x = 0;
        int y = 0;

        // 방문한 위치 true or false
        boolean[][] visitied = new boolean[board.length][board[0].length];

        // 움직인 칸
        int cnt = 1;

        // 미로 탐색
        dfs(board, x, y, visitied, cnt);
    }

}
