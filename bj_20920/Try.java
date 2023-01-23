package bj_20920;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class getData {

    int m = 0;
    HashMap<String, Integer> map1 = new HashMap<>();

    public int getm() {
		return this.m;
	}

    public void setm(int m) {
        this.m = m;
    }

    public HashMap<String, Integer> getmap1() {
        return this.map1 = map1;
    }

    public void setmap1(HashMap<String, Integer> map1) {
        this.map1 = map1;
    }

}

public class Try {

    static getData getData() throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        getData getData = new getData();

        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        getData.m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            if (!getData.map1.containsKey(word)) {
                getData.map1.put(word, 1);
                continue;
            }
            getData.map1.put(word, getData.map1.get(word) + 1);
        }

        return getData;
    }

    static void getAns(getData getData) {

        ArrayList<Integer> cntList = new ArrayList<>();

        for (String key : getData.map1.keySet()) {

        }
    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        getData getData = getData();
        System.out.println(getData.m);
        System.out.println(getData.map1);

    }

}
