package bj_2178;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

class Pair {

    int x;
    int y;

    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

}

public class Main_Pair {

    static void dfs(int[][][][] graph, int x, int y, boolean[][] visitied, int cnt) {

        visitied[x][y] = true;

        if (x == graph.length - 1 && y == graph[0].length - 1) {
            System.out.println(cnt + 1);
            return;
        }

        Stack <int []> stack = new Stack<>();
        // stack.pu

        int[] moves_x = new int[] { 1, 0, 0, -1 };
        int[] moves_y = new int[] { 0, 1, -1, 0 };

        for (int i=0; i<moves_x.length;i++){
            if (x + moves_x[i] >= 0 && x + moves_x[i] < graph.length && y + moves_y[i] >= 0&& y + moves_y[i] < graph[0].length){
                int x_check = graph[x+moves_x[i]][y+moves_y[i]][i][0];
                int y_check = graph[x+moves_x[i]][y+moves_y[i]][i][1];
                if(!visitied[x_check][y_check]){
                    System.out.println(x_check+","+y_check);
                    dfs(graph, x, y, visitied,cnt);
                }
            }

        }
    }

    // for (int i = 0; i < moves_x.length; i++) {
    // if (x + moves_x[i] >= 0 && x + moves_x[i] < graph.length && y + moves_y[i] >=
    // 0
    // && y + moves_y[i] < graph[0].length) {
    // if (visitied[x + moves_x[i]][y + moves_y[i]] == false) {
    // if (board[x + moves_x[i]][y + moves_y[i]] == 1) {
    // cnt++;
    // dfs(board, x + moves_x[i], y + moves_y[i], visitied, cnt);
    // }
    // }

    // }
    // }

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

        // 방문한 위치 true or false
        boolean[][] visitied = new boolean[board.length][board[0].length];

        // 움직인 칸
        int cnt = 0;

        // 그래프
        int[][] graph = new int[row_num][column_num];
        int[] moves_x = new int[] { 1, 0, 0, -1 };
        int[] moves_y = new int[] { 0, 1, -1, 0 };

        for (int x = 0; x < row_num; x++) {
            for (int y = 0; y < column_num; y++) {
                System.out.println("-----------" + x + "," + y + "-----------");
                
                for (int k = 0; k < moves_x.length; k++) {
                    if (x + moves_x[k] >= 0 && x + moves_x[k] < board.length && y + moves_y[k] >= 0
                            && y + moves_y[k] < board[0].length) {
                        if (board[x + moves_x[k]][y + moves_y[k]] == 1) {
                            Pair pair1 = new Pair(x + moves_x[k], y + moves_y[k]);
                            graph[x][y][k] = pair1;
                        }
                    }
                    System.out.println(Arrays.toString(graph[x][y][k]));
                }
            }
        }

        // root 위치
        int x = 0;
        int y = 0;

        // 미로 탐색
        dfs(graph, x, y, visitied, cnt);
    }

}