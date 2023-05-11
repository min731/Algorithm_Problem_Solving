package bj_1991;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Node {

    String data;
    Node left;
    Node right;

    Node (String data){
        this.data = data;
    }

}

class BinaryTree {

    Node root;
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    void createNode(String data, String leftdata, String rightdata){

        if (root == null)
        {
            root = new Node(data);  
            if (!leftdata.equals(".")){
                root.left = new Node(leftdata);
            }
            if (!rightdata.equals(".")){
                root.right = new Node(rightdata);
            }

        }
        else {
            searchNode(root, data, leftdata, rightdata);
        }
    }

    void searchNode(Node node, String data, String leftdata, String rightdata){

        if (node == null){

            return;

        }
        else if (node.data.equals(data)){

            if (!leftdata.equals(".")){
                node.left = new Node(leftdata);
            }
            if (!rightdata.equals(".")){
                node.right = new Node(rightdata);
            }
        }
        else{

            searchNode(node.left, data, leftdata, rightdata);
            searchNode(node.right, data, leftdata, rightdata);

        }

    }

    void preOrder(Node node) throws IOException{
        
        if (node != null){
            bw.write(node.data+"");
            bw.flush();
            if (node.left != null){
                preOrder(node.left);
            }
            if (node.right != null){
                preOrder(node.right);
            }
        }

    }

    void inOrder(Node node) throws IOException{

        if (node != null){

            if (node.left != null){
                inOrder(node.left);
            }
            bw.write(node.data+"");
            bw.flush();
            if (node.right != null){
                inOrder(node.right);
            }
        }

    }

    void postOrder(Node node) throws IOException{

        if (node != null){
            
            if(node.left != null){
                postOrder(node.left);
            }
            if(node.right != null){
                postOrder(node.right);
            }
            bw.write(node.data+"");
            bw.flush();
        }

    }

}







public class Try {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        BinaryTree binaryTree = new BinaryTree();
        
        String a;
        String b;
        String c;

        for (int i=0; i<N; i++){
            
            st = new StringTokenizer(br.readLine());
            a = st.nextToken();
            b = st.nextToken();
            c = st.nextToken();
            binaryTree.createNode(a, b, c);
        }

        binaryTree.preOrder(binaryTree.root);
        bw.write("\n");
        bw.flush();
        binaryTree.inOrder(binaryTree.root);
        bw.write("\n");
        bw.flush();
        binaryTree.postOrder(binaryTree.root);

    }
}
