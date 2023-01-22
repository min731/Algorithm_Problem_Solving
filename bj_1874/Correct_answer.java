package bj_1874;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;

public class Correct_answer {

    static Stack<Integer> makeStack(BufferedReader br) throws NumberFormatException, IOException {

        Stack<Integer> stack1 = new Stack<>();

        int N = Integer.parseInt(br.readLine());

        for (int i = N; i > 0; i--) {
            stack1.push(i);
        }

        return stack1;
    }

    static void getAns(Stack<Integer> stack1, BufferedReader br) throws NumberFormatException, IOException {

        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack2 = new Stack<>();
        stack2.push(0);
        ArrayList list1 = new ArrayList<>();

        int n = stack1.size();
        int m;

        for (int i = 0; i < n; i++) {
            m = Integer.parseInt(br.readLine());
            list1.add(m);
        }

        int o = -1;
        for (int i = 0; i < n; i++) {
            o = (int) list1.get(i);
            while (!stack2.peek().equals(o)) {
                if (stack2.peek() > o) {
                    System.out.println("NO");
                    return;
                }
                stack2.push(stack1.pop());
                sb.append("+" + "\n");
            }
            stack2.pop();
            sb.append("-" + "\n");
        }

        System.out.println(sb.toString());
        return;

    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack1 = makeStack(br);
        getAns(stack1, br);
    }

}