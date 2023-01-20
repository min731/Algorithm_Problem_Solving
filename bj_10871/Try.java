package bj_10871;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

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

public class Try {

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

    static ArrayList check(ArrayList<Integer> list1,int X,BufferedWriter bw) throws IOException{

        ArrayList<Integer> ans = new ArrayList<>();

        for(int i=0;i<list1.size();i++){
            if(list1.get(i) < X){
                ans.add(list1.get(i));
            }
        }

        return ans;
    }

    static void getAns(ArrayList<Integer> ans, BufferedWriter bw) throws IOException{

        for (int i=0; i<ans.size();i++){
            bw.write(Integer.toString(ans.get(i))+" ");
        }
        bw.flush();

    }

    public static void main(String[] args) throws IOException {

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        inputData data = getData();
        ArrayList<Integer> ans = check(data.getlist1(),data.getX(), bw);

        getAns(ans,bw);

        // bw.write(Integer.toString(data.getX())+"\n");
        // bw.flush();

        // for (int i = 0; i < data.getlist1().size(); i++) {
        //     bw.write(String.valueOf(data.getlist1().get(i))+" ");
        // }
        // bw.flush();




    }
}
