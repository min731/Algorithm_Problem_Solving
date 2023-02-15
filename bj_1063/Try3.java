package bj_1063;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class Pos {

    int x;
    int y;
}

public class Try3 {

    static Map<String, Integer> parser_map = new HashMap<>();
    static Map<String, int[]> move_cmds = new HashMap<>();

    static Pos parser(String pos) {

        String alphabet = pos.substring(0, 1);
        String num = pos.substring(1, 2);

        Pos obj = new Pos();

        obj.x = parser_map.get(alphabet);
        obj.y = parser_map.get(num);

        return obj;
    }

    static Pos move_act(String move_cmd,Pos obj){

        int [] move_act = move_cmds.get(move_cmd);

        if(obj.x+move_act[0] >=0 && obj.y+move_act[1] >=0 && )

        obj.x += move_act[0];
        obj.y += move_act[1];

        return obj; 
    }

    public static void main(String[] args) throws IOException {

        // 입력 받기

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        StringBuffer sb = new StringBuffer();

        // 1) 킹,돌 위치
        st = new StringTokenizer(br.readLine());
        String[] info = new String[2];

        for (int i = 0; i < info.length; i++) {
            info[i] = st.nextToken();
        }

        // 2) 명령 갯수
        int num_cmd = Integer.parseInt(st.nextToken());
        String[] cmds = new String[num_cmd];

        // 3) 명령어 받기
        for (int i = 0; i < cmds.length; i++) {
            cmds[i] = br.readLine();
        }

        // board 만들기

        int[][] board = new int[8][8];

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                board[i][j] = 0;
            }
            System.out.println(Arrays.toString(board[i]));
        }

        // parser_map(변환 맵) 만들기

        Map<String, Integer> parser_map = new HashMap<>();

        String num_alpha = "87654321ABCDEFGH";
        for (int i = 0; i < num_alpha.length(); i++) {
            parser_map.put(num_alpha.substring(i, i + 1), i % 8);
        }

        // 킹(1),돌(2) 처음위치로

        Pos king = new Pos();
        Pos stone = new Pos();

        king = parser(info[0]);
        stone = parser(info[1]);

        board[king.x][king.y] = 1;
        board[stone.x][stone.y] = 2;

        // 이동 명령

        Map<String, int[]> move_cmds = new HashMap<>();
        int[] R = new int[] { 1, 0 };
        int[] L = new int[] { -1, 0 };
        int[] B = new int[] { 0, 1 };
        int[] T = new int[] { 0, -1 };
        int[] RT = new int[] { 1, -1 };
        int[] LT = new int[] { -1, -1 };
        int[] RB = new int[] { 1, 1 };
        int[] LB = new int[] { -1, 1 };

        move_cmds.put("R", R);
        move_cmds.put("L", L);
        move_cmds.put("B", B);
        move_cmds.put("T", T);
        move_cmds.put("R", RT);
        move_cmds.put("L", LT);
        move_cmds.put("B", RB);
        move_cmds.put("T", LB);

        for (String move : cmds) {

        }

    }

}
