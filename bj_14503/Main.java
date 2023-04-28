package bj_14503;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    static int clean(int r,int c,int dir,int [][]map){
        int ans = 0 ;

        // 방향 
        // 0  1  2  3
        // 북 동 남 서

        int [] dx = new int []{-1,0,1,0};
        int [] dy = new int []{0,1,0,-1};

        int x = -1;
        int y = -1;

        while(true){

            // 현재 위치 청소
            // 청소 완료이면 2
            if (map[r][c] == 0){
                map[r][c] = 2;
                ans+=1;
            }

             // 주변 4칸 청소 완료 
            boolean around_4 = true;

            for (int i =3; i>=0;i--){
                x = r+dx[i];
                y = c+dy[i];

                if (map[x][y]==1){
                    continue;
                }

                if (map[x][y] == 0){
                    around_4 = false;
                    break;
                }
            }

            if (around_4 == true){
                
                r += dx[(dir+2)%4];
                c += dy[(dir+2)%4];
                
                // 후진하려는 위치가 벽이면, return
                if (map[r][c] == 1){
                    return ans;
                }
            }
            else{
                dir = (dir+3)%4;
                x = r + dx[dir];
                y = c + dy[dir];
                if (map[x][y]==0){
                    r = x;
                    c = y;
                }

            }
        }

    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;


        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int [][] map = new int [n][m];

        st = new StringTokenizer(br.readLine());

        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int dir = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = clean(r,c,dir,map);

        // bw는 문자열로 변환해서 출력
        bw.write(ans+"");
        bw.flush();
        bw.close();
    }
}
