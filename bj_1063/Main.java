package bj_1063;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class Pos {

    int x;
    int y;
}

public class Main {

    static Map<String, Integer> pos_parser = new HashMap<>();
    static Map<String, int[]> cmd_parser = new HashMap<>();

    static Pos xy_parser(String info, Map pos_parser) {

        String alphabet = info.substring(0, 1);
        String num = info.substring(1, 2);

        Pos obj = new Pos();

        obj.x = (int) pos_parser.get(alphabet);
        obj.y = (int) pos_parser.get(num);

        return obj;
    }

    static String str_parser(Pos obj, Map pos_parser) {

        int alphabet = obj.x;
        int num = obj.y;

        String alphabet_key = "";
        String num_key = "";

        Boolean find_alphabet = false;

        for (Object key : pos_parser.keySet()) {

            if (!find_alphabet) {
                if (pos_parser.get((String) key).equals(alphabet)) {
                    alphabet_key = (String) key;
                    find_alphabet = true;
                }
            }
            if (find_alphabet) {
                if (pos_parser.get((String) key).equals(num)) {
                    num_key = (String) key;
                }
            }
        }

        return alphabet_key + num_key;
    }

    static Pos[] move_act(String cmd, Pos[] king_stone, Map cmd_parser) {

        int[] cmd_xy = (int[]) cmd_parser.get(cmd);
        Pos king = king_stone[0];
        Pos stone = king_stone[1];

        int next_king_x = king.x + cmd_xy[0];
        int next_king_y = king.y + cmd_xy[1];
        int next_stone_x = stone.x + cmd_xy[0];
        int next_stone_y = stone.y + cmd_xy[1];

        if (next_king_x >= 0 && next_king_y >= 0 && next_king_x <= 7 && next_king_y <= 7) {

            if (next_king_x == stone.x && next_king_y == stone.y) {
                if (next_stone_x >= 0 && next_stone_y >= 0 && next_stone_x <= 7 && next_stone_y <= 7) {
                    stone.x = next_stone_x;
                    stone.y = next_stone_y;
                } else {
                    return king_stone;
                }
            }

            king.x += cmd_xy[0];
            king.y += cmd_xy[1];

        }

        king_stone[0] = king;
        king_stone[1] = stone;

        return king_stone;
    }

    public static void main(String[] args) throws IOException {

        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

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
        }

        // pos_parser(변환 맵) 만들기

        Map<String, Integer> pos_parser = new HashMap<>();

        String num_alpha = "87654321ABCDEFGH";
        for (int i = 0; i < num_alpha.length(); i++) {
            pos_parser.put(num_alpha.substring(i, i + 1), (int) i % 8);
        }

        // 킹(1),돌(2) 처음위치로

        Pos king = new Pos();
        Pos stone = new Pos();

        king = xy_parser(info[0], pos_parser);
        stone = xy_parser(info[1], pos_parser);

        // 이동 명령

        Map<String, int[]> cmd_parser = new HashMap<>();
        int[] R = new int[] { 1, 0 };
        int[] L = new int[] { -1, 0 };
        int[] B = new int[] { 0, 1 };
        int[] T = new int[] { 0, -1 };
        int[] RT = new int[] { 1, -1 };
        int[] LT = new int[] { -1, -1 };
        int[] RB = new int[] { 1, 1 };
        int[] LB = new int[] { -1, 1 };

        cmd_parser.put("R", R);
        cmd_parser.put("L", L);
        cmd_parser.put("B", B);
        cmd_parser.put("T", T);
        cmd_parser.put("RT", RT);
        cmd_parser.put("LT", LT);
        cmd_parser.put("RB", RB);
        cmd_parser.put("LB", LB);

        Pos[] king_stone = new Pos[] { king, stone };
        for (String cmd : cmds) {
            king_stone = move_act(cmd, king_stone, cmd_parser);
        }

        Pos ans_king = king_stone[0];
        Pos ans_stone = king_stone[1];

        bw.write(str_parser(ans_king, pos_parser) + "\n");
        bw.write(str_parser(ans_stone, pos_parser));
        bw.flush();

    }

}
