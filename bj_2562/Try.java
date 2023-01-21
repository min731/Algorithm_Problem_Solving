package bj_2562;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class Try {

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

    static int checkMax(ArrayList list_origin) {

        int Max = 0;

        ArrayList<Integer> list_sort = (ArrayList<Integer>) list_origin.clone();

        System.out.println(list_origin == list_sort);

        list_sort.sort(Comparator.naturalOrder());

        System.out.println(Arrays.deepToString(list_sort.toArray()));

        Max = (int) list_sort.get(list_sort.size() - 1);

        return Max;
    }

    static int findIndex(ArrayList list_origin, int Max) {

        int idx = 0;

        idx = list_origin.indexOf(Max) + 1;

        return idx;
    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayList<Integer> list_origin = getData();
        int Max = checkMax(list_origin);
        int idx = findIndex(list_origin, Max);

        bw.append(Max + "\n");
        bw.append(Integer.toString(idx));
        bw.flush();

    }

}
