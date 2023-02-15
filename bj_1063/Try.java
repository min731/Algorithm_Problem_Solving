package bj_1063;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Try {

    public static void main(String[] args) throws IOException {

        // 입력 받기

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        // 1) 킹,돌 위치
        st = new StringTokenizer(br.readLine());
        String [] info = new String[2];

        for(int i=0;i<info.length;i++){
            info[i] = st.nextToken();
        }

        // 2) 명령 갯수
        int num_cmd = Integer.parseInt(st.nextToken());
        String [] cmds = new String[num_cmd];

        // 3) 명령어 받기
        for(int i=0;i<cmds.length;i++){
            cmds[i] = br.readLine();
        }

        // board, parser 만들기
        String[][] board = new String[8][8];
        Map<String,int[]> parser = new HashMap<>();

        String num_str = "12345678";
        String alphabet_str = "abcdefgh".toUpperCase();
        StringBuffer sb = new StringBuffer(num_str);
        num_str = sb.reverse().toString();

        for (int i = 0; i < 8; i++) {
            String num = num_str.substring(i, i + 1);
            for (int j = 0; j < 8; j++) {
                String alphabet = alphabet_str.substring(j, j + 1);
                board[i][j] = alphabet + num;
                int [] tmp = new int[]{i,j};
                parser.put(board[i][j], tmp);
            }
            System.out.println(Arrays.toString(board[i]));
        }

        // 킹,돌 처음위치로


        
        // 이동

        for(String move : cmds){

        }




    }

}
