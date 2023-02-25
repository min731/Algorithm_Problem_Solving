package bj_2667;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Pos {
    int x;
    int y;
}

public class Try {

    // 입력받은 지도
    static int[][] map;
    static boolean[][] visited;

    // 이동 방향키 (오른쪽,아래,왼쪽,위 순서로 탐색)
    static int[] dx = new int[] { 0, 1, 0, -1 };
    static int[] dy = new int[] { 1, 0, -1, 0 };

    static void findHouse(Pos pos) {

        visited[pos.x][pos.y] = true;

        for (int i = 0; i < map[0].length; i++) {
            for (int j = 0; j < map[0].length; j++) {

                if (!visited[i][j]) {

                    int next_pos_x;
                    int next_pos_y;

                    for (int k = 0; k < dx.length; k++) {

                        next_pos_x = pos.x + dx[k];
                        next_pos_y = pos.y + dy[k];

                        if (next_pos_x >= 0 && next_pos_y >= 0
                                || next_pos_x <= map[0].length && next_pos_y < map[0].length) {
                            if (map[next_pos_x][next_pos_y] == 1) {
                                pos.x = next_pos_x;
                                pos.y = next_pos_y;
                                System.out.println("x: " + pos.x + " , y: " + pos.y);

                                for (int z = 0; z < visited[0].length; z++) {
                                    System.out.println(Arrays.toString(visited[z]));
                                }
                                findHouse(pos);
                            }

                        }

                    }
                }

            }
        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        map = new int[n][n];

        String input;
        for (int i = 0; i < n; i++) {

            input = br.readLine();
            System.out.println("input: " + input);
            for (int j = 0; j < n; j++) {
                map[i][j] = input.charAt(j) - 48;
            }

            System.out.println(Arrays.toString(map[i]));
        }
        System.out.println("---------------------------------");

        // root 위치
        Pos pos = new Pos();
        pos.x = 0;
        pos.y = 0;

        // 방문 여부
        visited = new boolean[n][n];
        findHouse(pos);

    }

}
