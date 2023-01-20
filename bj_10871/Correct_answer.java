package bj_10871;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 입력데이터 받기 위한 클래스
final class inputData {

    private int X;
    private ArrayList list1;

    inputData(int X, ArrayList list1) {
        this.X = X;
        this.list1 = list1;
    }

    public int getX() {
        return this.X;
    }

    public void setX(int X) {
        this.X = X;
    }

    public ArrayList getlist1() {
        return this.list1;
    }

    public void setArrayList(ArrayList list1) {
        this.list1 = list1;
    }

}

public class Correct_answer {

    // 입력데이터 받기
    static inputData getData() throws IOException {

        ArrayList<Integer> list1 = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int N = 0;
        int X = 0;

        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int el;
        for (int i = 0; i < N; i++) {
            el = Integer.parseInt(st.nextToken());
            list1.add(el);
        }

        inputData data = new inputData(X, list1);

        return data;
    }

    // X보다 작은수 체크하기
    static ArrayList check(ArrayList<Integer> list1, int X, BufferedWriter bw) throws IOException {

        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = 0; i < list1.size(); i++) {
            if (list1.get(i) < X) {
                ans.add(list1.get(i));
            }
        }

        return ans;
    }

    // 답 출력하기
    static void getAns(ArrayList<Integer> ans, BufferedWriter bw) throws IOException {

        for (int i = 0; i < ans.size(); i++) {
            bw.write(Integer.toString(ans.get(i)) + " ");
        }
        bw.flush();

    }

    public static void main(String[] args) throws IOException {
        // bw : 출력해주는 객체
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // 입력데이터 받기
        inputData data = getData();
        // X보다 작은수 체크하기
        ArrayList<Integer> ans = check(data.getlist1(), data.getX(), bw);
        // 답 출력하기
        getAns(ans, bw);

    }
}