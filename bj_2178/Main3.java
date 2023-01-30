package bj_2178;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main3 {

    static void dfs(int[][] board, int x, int y, boolean[][] visitied, int cnt) {

        visitied[x][y] = true;

        if (x == board.length - 1 && y == board[0].length - 1) {
            System.out.println(cnt + 1);
            return;
        }

        int[] moves_x = new int[] { 1, 0, 0, -1 };
        int[] moves_y = new int[] { 0, 1, -1, 0 };

        for (int i = 0; i < moves_x.length; i++) {
            if (x + moves_x[i] >= 0 && x + moves_x[i] < board.length && y + moves_y[i] >= 0
                    && y + moves_y[i] < board[0].length) {
                if (visitied[x + moves_x[i]][y + moves_y[i]] == false) {
                    if (board[x + moves_x[i]][y + moves_y[i]] == 1) {
                        cnt++;
                        dfs(board, x + moves_x[i], y + moves_y[i], visitied, cnt);
                    }
                }

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

        // root 위치
        // int x = 0;
        // int y = 0;

        // 방문한 위치 true or false
        boolean[][] visitied = new boolean[board.length][board[0].length];

        // 움직인 칸
        int cnt = 0;

        // 그래프
        int[][][][] graph = new int[row_num][column_num][4][2];
        int[] moves_x = new int[] { 1, 0, 0, -1 };
        int[] moves_y = new int[] { 0, 1, -1, 0 };

        for (int x = 0; x < row_num; x++) {
            for (int y = 0; y < column_num; y++) {
                System.out.println("x"+","+"y"+"에서 갈 수 있는 좌표");
                for (int k = 0; k < moves_x.length; k++) {
                    if (x + moves_x[k] >= 0 && x + moves_x[k] < board.length && y + moves_y[k] >= 0
                            && y + moves_y[k] < board[0].length) {
                        if (board[x + moves_x[k]][y + moves_y[k]] == 1) {
                            graph[x][y][k][0] = x + moves_x[k];
                            graph[x][y][k][1] = y + moves_y[k];
                        }
                    }
                    System.out.println(Arrays.toString(graph[x][y][k]));
                }
            }
        }

        // 미로 탐색
        // dfs(board, x, y, visitied,cnt);
    }

}