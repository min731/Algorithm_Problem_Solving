package bj_2178;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Correct {

    static int [][] map;
    static boolean [][] visited;
    static int [] dx = {-1,1,0,0};
    static int [] dy = {0,0,-1,1};

    static void bfs(int x, int y) {

        Queue<int[]> queue1 = new LinkedList<>();
        queue1.add(new int[] {x,y});

        while(!queue1.isEmpty()){
            int now[] = queue1.poll();
            int nowX = now[0];
            int nowY = now[1];

            for(int i=0;i<4;i++){
                int nextX = nowX + dx[i];
                int nextY = nowY + dy[i];

                if (nextX<0 || nextY < 0 || nextX >=n || nextY >= m){
                    continue;
                }
                if (visited[nextX][nextY] || map[nextX][nextY]==0){
                    continue;
                }

                queue1.add(new int[] {nextX,nextY});
                map[nextX][nextY] = map[nowX][nowY]+1;
                visited[nextX][nextY] = true;
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

        map = new int[row_num][column_num];

        for (int i = 0; i < row_num; i++) {
            String input = br.readLine();
            for (int j = 0; j < column_num; j++) {
                map[i][j] = Integer.parseInt(Character.toString(input.charAt(j)));
            }
        }

        // 방문한 위치 true or false
        visited = new boolean[map.length][map.length];

        visited[0][0] = true;

        // 움직인 칸
        bfs(0,0);
        System.out.println(map[row_num-1][column_num-1]);
    }
}