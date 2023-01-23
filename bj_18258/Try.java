package bj_18258;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

class ringQue {

    public int[] que;
    private int front;
    private int rear;
    private int capacity;
    private int num;

    ringQue() {

        que = new int[27];
        capacity = 27;
        front = 0;
        rear = 0;
        num = 0;
    }

    public int push(int x) {
        if (num >= capacity) {
            System.out.println("큐가 꽉 찼음");
            return -1;
        }

        que[rear++] = x;
        System.out.println("rear: " + rear);
        num++;
        if (rear == capacity) {
            rear = 0;
        }

        return x;
    }

    public int pop() {
        if (num <= 0) {
            System.out.println("큐에 아무 것도 없음");
            return -1;
        }

        int x = que[front++];
        que[front - 1] = 0;
        num--;
        if (front == capacity) {
            front = 0;
        }
        return x;
    }

    public int size() {
        return num;
    }

    public int empty() {
        return num <= 0 ? 1 : 0;
    }

    public int front() {
        int x = que[front];
        if (x == 0) {
            return -1;
        }
        return x;
    }

    public int back() {
        int x;
        if (rear == 0) {
            x=que[capacity-1];
        }
        else{
            x = que[rear - 1];
        }
        if (x == 0) {
            return -1;
        }
        return x;
    }

}

public class Try {

    static ArrayList<String> getData() throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        ArrayList<String> list1 = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("push")) {
                String num = st.nextToken();
                list1.add(command + num);
            } else {
                list1.add(command);
            }
        }

        System.out.println(Arrays.deepToString(list1.toArray()));
        return list1;
    }

    static void getAns(ArrayList<String> list1, ringQue ringQue) {
        StringBuilder sb = new StringBuilder();

        for (String command : list1) {
            String cmd = command.replaceAll("[0-9]", "");

            switch (cmd) {
                case "push":
                    sb.append("push" + "\n");
                    ringQue.push(Integer.parseInt(command.replaceAll("[^0-9]", "")));
                    break;
                case "pop":
                    sb.append("pop" + "\n");
                    sb.append(ringQue.pop() + "\n");
                    break;
                case "size":
                    sb.append("size" + "\n");
                    sb.append(ringQue.size() + "\n");
                    break;
                case "empty":
                    sb.append("empty" + "\n");
                    sb.append(ringQue.empty() + "\n");
                    break;
                case "front":
                    sb.append("front" + "\n");
                    sb.append(ringQue.front() + "\n");
                    break;
                case "back":
                    sb.append("back" + "\n");
                    sb.append(ringQue.back() + "\n");
                    break;
            }
            sb.append(Arrays.toString(ringQue.que) + "\n");
        }
        System.out.println(sb.toString());

    }

    public static void main(String[] args) throws NumberFormatException, IOException {

        ArrayList<String> list1 = new ArrayList<>();
        list1 = getData();

        ringQue ringque1 = new ringQue();

        getAns(list1, ringque1);

    }

}
