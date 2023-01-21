package bj_2562;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class Correct_answer {

    // 입력값 받기
    static ArrayList<Integer> getData() throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> list_origin = new ArrayList<>();

        int n = 0;

        for (int i = 0; i < 9; i++) {
            n = Integer.parseInt(br.readLine());
            list_origin.add(n);
        }

        System.out.println(Arrays.deepToString(list_origin.toArray()));

        return list_origin;
    }

    // 최댓값 찾기
    static int checkMax(ArrayList list_origin) {

        int Max = 0;

        ArrayList<Integer> list_sort = (ArrayList<Integer>) list_origin.clone();

        System.out.println(list_origin == list_sort);

        list_sort.sort(Comparator.naturalOrder());

        System.out.println(Arrays.deepToString(list_sort.toArray()));

        Max = (int) list_sort.get(list_sort.size() - 1);

        return Max;
    }

    // 최댓값 위치 찾기
    static int findIndex(ArrayList list_origin, int Max) {

        int idx = 0;

        // n번째 수를 찾는 것이므로 인덱스+1
        idx = list_origin.indexOf(Max) + 1;

        return idx;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 입력값 받기
        ArrayList<Integer> list_origin = getData();
        // 최댓값 찾기
        int Max = checkMax(list_origin);
        // 최댓값 위치 찾기
        int idx = findIndex(list_origin, Max);

        // 답 출력하기
        bw.append(Max + "\n");
        bw.append(Integer.toString(idx));
        bw.flush();

    }

}
