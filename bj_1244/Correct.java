package bj_1244;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Correct {

    static int one_zero_parser(int one_or_zero) {

        // 2 % (1+1) => result = 0
        // 2 % (0+1) => result = 1
        int result = (one_or_zero + 1) % 2;
        return result;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] switches = new int[n];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            switches[i] = Integer.parseInt(st.nextToken());
        }

        // 학생 수
        int std_num = Integer.parseInt(br.readLine());

        // 학생 수 만큼 반복
        for (int i = 0; i < std_num; i++) {

            st = new StringTokenizer(br.readLine());

            // 성별
            int gender = Integer.parseInt(st.nextToken());

            // 번호
            int number = Integer.parseInt(st.nextToken());

            // 남자일 때
            if (gender == 1) {

                for (int j = number; j < n; j += (number)) {
                    switches[j - 1] = one_zero_parser(switches[j - 1]);
                }
            }

            // 여자일 때
            else {
                switches[number - 1] = one_zero_parser(switches[number - 1]);

                // 번호가 중간 이상 or 이하인지 확인
                boolean higher = false;

                if (number > n / 2) {
                    higher = true;
                }

                int gap = 0;
                // 중간 이상 일때
                if (higher) {

                    while (number + gap < n) {
                        gap++;
                        if (switches[number + gap - 1] == switches[number - gap - 1]) {
                            switches[number + gap - 1] = one_zero_parser(switches[number + gap - 1]);
                            switches[number - gap - 1] = one_zero_parser(switches[number - gap - 1]);
                        } else {
                            break;
                        }
                    }

                }

                // 중간 이하일때
                else {

                    while (number + gap > 1) {
                        gap--;
                        if (switches[number + gap - 1] == switches[number - gap - 1]) {
                            switches[number + gap - 1] = one_zero_parser(switches[number + gap - 1]);
                            switches[number - gap - 1] = one_zero_parser(switches[number - gap - 1]);
                        } else {
                            break;
                        }
                    }

                }

            }

        }

        // 출력
        // i=19(20번째), i=38(40번째)
        for (int i = 0; i < n; i++) {
            if (i != 0 && i % 20 == 0) {
                bw.write("\n");
            }
            bw.write(switches[i] + " ");
        }
        bw.flush();

    }
}
