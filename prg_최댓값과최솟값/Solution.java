package prg_최댓값과최솟값;

class Solution {
    
    static int getMax(String [] S){
        int Max = Integer.parseInt(S[0]);
        
        for(int i=0; i<S.length;i++){
            int tmp = Integer.parseInt(S[i]);
            if (Max < Integer.parseInt(S[i])){
                Max = tmp;
            }
        }
        
        return Max;
    }
                            
    static int getMin(String [] S){
        int Min = Integer.parseInt(S[0]);
        
        for(int i=0; i<S.length;i++){
            int tmp = Integer.parseInt(S[i]);
            if (Min > Integer.parseInt(S[i])){
                Min = tmp;
            }
        }
        
        return Min;
    }
    
    public String solution(String s) {
        
        int Max = 0;
        int Min = 0;
        
        String [] S = s.split(" ");
        
        Max = getMax(S);
        Min = getMin(S);
        
        String answer = "";
        
        answer = Integer.toString(Min) + " " + Integer.toString(Max);
        
        return answer;
    }
}