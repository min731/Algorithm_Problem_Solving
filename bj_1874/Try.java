package bj_1874;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Stack;

public class Try {

    static Stack<Integer> makeStack() throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> stack1 = new Stack<>();

        bw.write("n 입력:");
        bw.flush();
        int N = Integer.parseInt(br.readLine());

        for (int i = N; i > 0; i--) {
            stack1.push(i);
        }

        return stack1;
    }

    static void getAns(Stack<Integer> stack1) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> stack2 = new Stack<>();
        stack2.push(0);
        ArrayList list1 = new ArrayList<>();

        int n = stack1.size();
        int m;

        for (int i = 0; i < n; i++) {
            System.out.println("m 입력:");
            m = Integer.parseInt(br.readLine());
            list1.add(m);
        }

        int o = -1;
        for (int i = 0; i < n; i++) {
            o = (int) list1.get(i);
            while (stack2.peek() != o) {
                if (stack2.peek() > o) {
                    // bw = new BufferedWriter(new OutputStreamWriter(System.out));
                    // bw.write("NO");
                    System.out.println("NO");
                    return;
                }
                stack2.push(stack1.pop());
                bw.write("+");
                bw.newLine();
            }
            stack2.pop();
            bw.write("-");
            bw.newLine();
        }

        bw.flush();
        return;

    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Stack<Integer> stack1 = makeStack();
        getAns(stack1);
    }

}
